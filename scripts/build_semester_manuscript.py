#!/usr/bin/env python3
"""Build a Word/PDF draft of the semester manuscript from the repository source."""
from __future__ import annotations
import json, re, shutil, subprocess, sys, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'manuscript' / 'SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md'
BIB = ROOT / 'semester-manuscript-cited-references-49-selected-plus-11-context.bib'
CSL = ROOT / 'references' / 'american-chemical-society-2026.csl'
OUT = ROOT / 'build' / 'semester-manuscript'
FIG = OUT / 'figures'
TABLE1_SOURCE = ROOT / 'manuscript' / 'SEMESTER_TABLE_1_SEARCH_STRATEGY_SOURCE.md'
TABLE3_SOURCE = ROOT / 'manuscript' / 'SEMESTER_TABLE_3_EVIDENCE_COVERAGE_SOURCE.md'

def run(cmd: list[str]) -> None:
    print('+', ' '.join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_table_3_content() -> str:
    """Assemble Table 3's compact index and study-level evidence notes."""
    if not TABLE3_SOURCE.exists():
        raise SystemExit(f'Missing Table 3 source: {TABLE3_SOURCE.relative_to(ROOT)}')
    source_lines = TABLE3_SOURCE.read_text(encoding='utf-8').splitlines()
    data_rows = []
    for line in source_lines:
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 7 or cells[0] in ('Study (author–year)', 'Study'):
            continue
        citation_match = re.search(r'\\cite\{([^}]+)\}', cells[6])
        if not citation_match:
            raise SystemExit(f'Missing citation key for Table 3 row: {cells[0]}')
        data_rows.append({
            'study': cells[0],
            'title': cells[1],
            'target': cells[2],
            'material': re.split(r';\s*(?:Empirical primary study|Theory/mechanism context only|Review/background context only|Scope-boundary near-miss)', cells[3], maxsplit=1)[0].strip(),
            'source': cells[4],
            'evidence': cells[5],
            'key': citation_match.group(1),
        })
    if len(data_rows) != 49:
        raise SystemExit(f'Expected 49 selected references in Table 3, found {len(data_rows)}')
    labels = [row['study'] for row in data_rows]
    if len(set(labels)) != 49:
        raise SystemExit('Duplicate author-year labels detected in Table 3.')
    if any(re.search(r'\b(?:SEM|EV-SEM)-\d{3}\b', ' '.join(row.values())) for row in data_rows):
        raise SystemExit('Internal evidence identifiers found in reader-facing Table 3 data.')

    md = [
        '\\newpage',
        '',
        '```{=openxml}',
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
        '```',
        '',
        '## Table 3. Evidence coverage of the 49 selected references',
        '',
        'Table 3 records the target antibiotic, adsorbent and study role for each selected work, followed by source-tier and evidence-use notes. It is a coverage register, not a quantitative ranking. Abstract-only, preview-only, repository-hosted and internally inconsistent results retain their source qualifications.',
        '',
        '### Table 3A. Selected-reference index',
        '',
        '| Study (author–year) | Target | Adsorbent / study role |',
        '|---|---|---|',
    ]
    for row in data_rows:
        md.append(f"| {row['study']} | {row['target']} | {row['material']} |")
    md.extend([
        '',
        '### Study-level source and evidence notes',
        '',
        'The notes below separate source availability from the permitted use of each result. Numerical endpoints are retained as reported or explicitly identified as derived; fitted parameters, observed uptake and removal percentages are not interchangeable.',
        '',
    ])
    for idx, row in enumerate(data_rows, 1):
        md.extend([
            f"**{idx}. {row['study']}**",
            '',
            f"*{row['title']}*",
            '',
            f"**Target:** {row['target']}",
            '',
            f"**Adsorbent / study role:** {row['material']}",
            '',
            f"**Source tier:** {row['source']}",
            '',
            f"**Evidence and qualification:** {row['evidence']}",
            '',
            f"**Citation:** [@{row['key']}]",
            '',
        ])
    md.extend([
        '### Interpretation rules for Table 3',
        '',
        '1. Source-reported observed \\(q_e\\), mass-balance-derived uptake, kinetic-model-fitted \\(q_e\\), fitted isotherm \\(q_{\\max}/q_m\\), removal percentage and column metrics are different endpoints. Do not merge or rank them without a valid common basis.',
        '2. Ciprofloxacin (CIP) is not pooled with norfloxacin or ofloxacin. Tetracycline (TC) is not pooled with chlortetracycline, oxytetracycline or doxycycline.',
        '3. Theoretical, review and scope-related references provide context only and should not be interpreted as primary quantitative evidence of GO/rGO adsorption performance.',
        '',
    ])
    return '\n'.join(md)


def load_table_1_content() -> str:
    """Load the literature-search strategy table inserted into the manuscript."""
    if not TABLE1_SOURCE.exists():
        raise SystemExit(f'Missing Table 1 source: {TABLE1_SOURCE.relative_to(ROOT)}')
    return TABLE1_SOURCE.read_text(encoding='utf-8').strip()


def main() -> None:
    for p in (SOURCE, BIB, CSL):
        if not p.exists():
            raise SystemExit(f'Missing required build input: {p.relative_to(ROOT)}')
    pandoc = shutil.which('pandoc')
    mmdc = shutil.which('mmdc')
    xelatex = shutil.which('xelatex')
    if not pandoc or not mmdc or not xelatex:
        raise SystemExit('Build requires pandoc, mermaid-cli (mmdc), and xelatex.')
    if OUT.exists():
        shutil.rmtree(OUT)
    FIG.mkdir(parents=True)
    md = SOURCE.read_text(encoding='utf-8')
    for marker, content in (
        ('<!-- TABLE_1_SEARCH_STRATEGY -->', load_table_1_content()),
        ('<!-- TABLE_3_EVIDENCE_COVERAGE -->', build_table_3_content()),
    ):
        if md.count(marker) != 1:
            raise SystemExit(f'Expected one manuscript insertion marker: {marker}')
        md = md.replace(marker, content)
    # Keep internal evidence-traceability annotations in the repository source and
    # audit ledgers, but do not expose them in the reader-facing manuscript render.
    md = re.sub(r'\s*\[evidence:[^\]]+\]', '', md)
    md = re.sub(
        r'Existing source-linked evidence remains in CORP-031 / EV-B10-004–EV-B10-009; do not re-extract it as a duplicate\.\s*',
        '',
        md,
    )
    md = re.sub(r'\bCite with (?:the verified key )?(?=\\cite\{)', '', md)
    # Remove repository-production metadata from the reader-facing manuscript copy.
    md = re.sub(r'(?m)^\*\*Assembled working source V2[^\n]*\n?', '', md)
    md = re.sub(r'(?s)\n\*\*Consolidated bibliography:\*\*.*?(?=\n\n## Abstract)', '\n', md)
    # Convert each Mermaid diagram into a high-resolution PNG for DOCX/PDF portability.
    # Match the full authored figure block (title + caption + Mermaid source) so
    # the image caption is not duplicated by Pandoc's automatic figure label.
    pattern = re.compile(
        r'\*\*(Figure \d+\.[^\n]+)\*\*\s*\n\n\*([^\n]+)\*\s*\n\n```mermaid\s*\n(.*?)\n```',
        re.S
    )
    diagrams = list(pattern.finditer(md))
    if len(diagrams) != 5:
        raise SystemExit(f'Expected 5 complete figure blocks, found {len(diagrams)}')
    rendered = []
    puppeteer_config = OUT / 'puppeteer-config.json'
    puppeteer_config.write_text(json.dumps({'args': ['--no-sandbox', '--disable-setuid-sandbox']}), encoding='utf-8')
    for i, match in enumerate(diagrams, 1):
        src = FIG / f'figure_{i}.mmd'
        png = FIG / f'figure_{i}.png'
        src.write_text(match.group(3).strip() + '\n', encoding='utf-8')
        run([mmdc, '-p', str(puppeteer_config), '-i', str(src), '-o', str(png), '-t', 'neutral', '-b', 'white', '-s', '2'])
        rendered.append(png)
    def replace_diagram(match: re.Match[str], idx: int) -> str:
        return f'![{match.group(2).strip()}](figures/figure_{idx}.png)'
    pieces, cursor = [], 0
    for i, match in enumerate(diagrams, 1):
        pieces.append(md[cursor:match.start()])
        pieces.append(replace_diagram(match, i))
        cursor = match.end()
    pieces.append(md[cursor:])
    md = ''.join(pieces)
    # Convert the existing source-linked LaTeX citation commands to Pandoc citeproc syntax.
    cite_pattern = re.compile(r'\\cite\{([^}]+)\}')
    def cvt(m: re.Match[str]) -> str:
        keys = [x.strip() for x in m.group(1).split(',') if x.strip()]
        return '[' + '; '.join('@' + x for x in keys) + ']'
    md = cite_pattern.sub(cvt, md)
    # Word uses the explicit OpenXML page-break paragraphs; PDF uses LaTeX
    # \newpage commands. Keep one page-break mechanism per output to prevent
    # accidental blank pages in the DOCX.
    prepared_docx = OUT / 'rendered_manuscript_docx.md'
    prepared_pdf = OUT / 'rendered_manuscript_pdf.md'
    md_docx = re.sub(r'(?m)^\\newpage\s*$', '', md)
    # The assembled source contains double-escaped inline-math spans in the
    # SEM-010 dose-basis explanation. Pandoc treats the extra backslashes as
    # literal text in DOCX, so normalize delimiters and TeX commands inside
    # those spans to create native Word equations. The PDF source is unchanged.
    double_escaped_math = re.compile(r'\\\\\((.*?)\\\\\)', re.S)
    def normalize_docx_math(match: re.Match[str]) -> str:
        inner = match.group(1).replace('\\\\', '\\')
        return '\\(' + inner + '\\)'
    md_docx, normalized_math_count = double_escaped_math.subn(normalize_docx_math, md_docx)
    if normalized_math_count != 10 or re.search(r'\\\\\(', md_docx):
        raise SystemExit(
            f'Expected to normalize 10 double-escaped inline-math spans; found {normalized_math_count}.'
        )
    # Table 2D follows the full-page Table 2C. This OpenXML break caused an
    # additional blank Word page, so remove it in DOCX only; PDF is unchanged.
    md_docx = re.sub(
        r'(?s)\n\x60{3}{=openxml}\s*<w:p><w:r><w:br w:type="page"/></w:r></w:p>\s*\x60{3}\s*(?=## Table 2D\. Fitted isotherm-model outputs)',
        '\n',
        md_docx,
    )
    md_pdf = re.sub(r'(?s)\x60{3}{=openxml}.*?\x60{3}', '', md)
    # Keep Figure 2 in the methodological position where it is introduced.
    # Otherwise LaTeX may float this tall diagram past the start of Sections 2.4–2.5.
    figure2_image = re.search(
        r'!\[([^\]]+)\]\(figures/figure_2\.png\)',
        md_pdf,
    )
    if not figure2_image:
        raise SystemExit('Could not locate the rendered Figure 2 image for fixed PDF placement.')
    figure2_caption = figure2_image.group(1)
    fixed_figure2 = (
        r'\begin{figure}[H]' + '\n'
        r'\centering' + '\n'
        r'\includegraphics[width=0.96\linewidth]{' + str(FIG / 'figure_2.png') + '}' + '\n'
        r'\caption{' + figure2_caption + '}' + '\n'
        r'\end{figure}'
    )
    md_pdf = md_pdf.replace(figure2_image.group(0), fixed_figure2, 1)
    figure2_header_tex = OUT / 'figure2_float_header.tex'
    figure2_header_tex.write_text('\\usepackage{float}\n\\usepackage{etoolbox}\n\\AtBeginEnvironment{CSLReferences}{\\fontsize{8.5pt}{9.6pt}\\selectfont}\n', encoding='utf-8')
    prepared_docx.write_text(md_docx, encoding='utf-8')
    prepared_pdf.write_text(md_pdf, encoding='utf-8')
    common = [
        '--from=markdown+pipe_tables+raw_tex+raw_attribute+tex_math_dollars+tex_math_single_backslash',
        '--citeproc', '-M', 'reference-section-title=References', f'--bibliography={BIB}', f'--csl={CSL}',
        '--resource-path=' + str(OUT), '--standalone',
        '-V', 'papersize:a4', '-V', 'geometry:margin=22mm',
        '-V', 'fontsize:10pt', '-V', 'mainfont:DejaVu Serif',
        '-V', 'sansfont:DejaVu Sans', '-V', 'monofont:DejaVu Sans Mono',
    ]
    docx = OUT / 'SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.docx'
    pdf = OUT / 'SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.pdf'
    run([pandoc, str(prepared_docx)] + common + ['--to=docx', '-o', str(docx)])
    run([pandoc, str(prepared_pdf)] + common + ['--include-in-header', str(figure2_header_tex), '--pdf-engine=xelatex', '-o', str(pdf)])
    # Keep the condition-dense Table 2B readable but compact enough to remain
    # on one Word page after changing study labels to author-year format.
    docx_tmp = docx.with_suffix('.tmp.docx')
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    w = '{' + ns['w'] + '}'
    found_conditions_table = False
    with zipfile.ZipFile(docx, 'r') as source_zip, zipfile.ZipFile(docx_tmp, 'w', zipfile.ZIP_DEFLATED) as output_zip:
        for item in source_zip.infolist():
            payload = source_zip.read(item.filename)
            if item.filename == 'word/document.xml':
                root = ET.fromstring(payload)
                for table in root.findall('.//w:tbl', ns):
                    header = table.find('./w:tr', ns)
                    if header is None:
                        continue
                    header_cells = header.findall('./w:tc', ns)
                    header_text = [''.join(node.itertext()) for node in header_cells]
                    if 'Initial concentration / feed' in header_text and 'Contact / test time' in header_text:
                        for run_node in table.findall('.//w:r', ns):
                            rpr = run_node.find('./w:rPr', ns)
                            if rpr is None:
                                rpr = ET.Element(w + 'rPr')
                                run_node.insert(0, rpr)
                            for prop in ('sz', 'szCs'):
                                size = rpr.find('./w:' + prop, ns)
                                if size is None:
                                    size = ET.SubElement(rpr, w + prop)
                                size.set(w + 'val', '18')  # 9 pt
                        found_conditions_table = True
                        break
                if not found_conditions_table:
                    raise SystemExit('Could not identify Table 2B for compact Word styling.')

                # Keep each Table 3 study heading with its title and opening
                # metadata so no numbered study label is stranded at a page end.
                body = root.find('./w:body', ns)
                paragraphs = body.findall('./w:p', ns) if body is not None else []
                linked_study_blocks = 0
                for idx, paragraph in enumerate(paragraphs):
                    para_text = ''.join(node.text or '' for node in paragraph.findall('.//w:t', ns)).strip()
                    if not re.match(r'^\d{1,2}\.\s+.+\(\d{4}\)$', para_text):
                        continue
                    linked_study_blocks += 1
                    # Heading, article title, target, adsorbent and source tier.
                    for linked in paragraphs[idx:idx + 5]:
                        ppr = linked.find('./w:pPr', ns)
                        if ppr is None:
                            ppr = ET.Element(w + 'pPr')
                            linked.insert(0, ppr)
                        keep = ppr.find('./w:keepNext', ns)
                        if keep is None:
                            ET.SubElement(ppr, w + 'keepNext')
                if linked_study_blocks != 49:
                    raise SystemExit(
                        f'Expected to paginate 49 Table 3 study blocks, found {linked_study_blocks}.'
                    )

                # Compact bibliography entries slightly to avoid a single-reference
                # orphan page. Keep the same typeface and citation content.
                references_started = False
                bibliography_paragraphs = 0
                for paragraph in paragraphs:
                    para_text = ''.join(node.text or '' for node in paragraph.findall('.//w:t', ns)).strip()
                    if para_text == 'References':
                        references_started = True
                        continue
                    if not references_started:
                        continue
                    bibliography_paragraphs += 1
                    # Keep each reference entry together on one page. Without
                    # w:keepLines, a long title can split at the page boundary,
                    # leaving the continuation isolated at the top of the next page.
                    ppr = paragraph.find('./w:pPr', ns)
                    if ppr is None:
                        ppr = ET.Element(w + 'pPr')
                        paragraph.insert(0, ppr)
                    keep_lines = ppr.find('./w:keepLines', ns)
                    if keep_lines is None:
                        ET.SubElement(ppr, w + 'keepLines')
                    for run_node in paragraph.findall('.//w:r', ns):
                        rpr = run_node.find('./w:rPr', ns)
                        if rpr is None:
                            rpr = ET.Element(w + 'rPr')
                            run_node.insert(0, rpr)
                        for prop in ('sz', 'szCs'):
                            size = rpr.find('./w:' + prop, ns)
                            if size is None:
                                size = ET.SubElement(rpr, w + prop)
                            size.set(w + 'val', '17')  # 8.5 pt, references only
                if bibliography_paragraphs == 0:
                    raise SystemExit('Could not identify the bibliography block for compact styling.')

                # Set explicit A4 page geometry for Word. Pandoc's papersize
                # variable controls LaTeX/PDF but does not reliably set DOCX
                # section dimensions; without pgSz, Word may default to Letter.
                sect_pr = body.find('./w:sectPr', ns) if body is not None else None
                if sect_pr is None:
                    sect_pr = ET.Element(w + 'sectPr')
                    body.append(sect_pr)
                for tag in ('pgSz', 'pgMar'):
                    for existing in sect_pr.findall('./w:' + tag, ns):
                        sect_pr.remove(existing)
                page_size = ET.Element(w + 'pgSz', {
                    w + 'w': '11906',  # A4 width, twips
                    w + 'h': '16838',  # A4 height, twips
                    w + 'orient': 'portrait',
                })
                page_margins = ET.Element(w + 'pgMar', {
                    w + 'top': '1247',     # 22 mm
                    w + 'right': '1247',
                    w + 'bottom': '1247',
                    w + 'left': '1247',
                    w + 'header': '708',
                    w + 'footer': '708',
                    w + 'gutter': '0',
                })
                sect_pr.insert(0, page_size)
                sect_pr.insert(1, page_margins)
                payload = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            output_zip.writestr(item, payload)
    docx_tmp.replace(docx)
    # Keep a concise build manifest next to the outputs.
    (OUT / 'BUILD_INFO.txt').write_text(
        'Working manuscript V2 build\n'
        'Citation style: ACS Guide 2026 (provisional; confirm against AMU/supervisor requirements)\n'
        'Source: manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md\n'
        'Bibliography: semester-manuscript-cited-references-49-selected-plus-11-context.bib\n'
        'Five Mermaid diagrams converted to embedded PNG images.\n'
        'Tables 1, 2 and 3 are integrated into the single manuscript DOCX/PDF.\n'
        'DOCX page geometry: A4 portrait with 22 mm margins.\n'
        'PDF page geometry: A4 portrait with 22 mm margins.\n'
        'A dedicated References heading is included in both outputs.\n'
        'DOCX/PDF require manual full-page visual review before submission.\n',
        encoding='utf-8')
    print('Build complete:', docx, pdf, flush=True)

if __name__ == '__main__':
    main()
