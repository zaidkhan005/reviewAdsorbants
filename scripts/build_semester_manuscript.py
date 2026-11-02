#!/usr/bin/env python3
"""Build a Word/PDF draft of the semester manuscript from the repository source."""
from __future__ import annotations
import json, re, shutil, subprocess, sys, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'manuscript' / 'SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md'
BIB = ROOT / 'semester-manuscript-cited-references-49-selected-plus-4-context.bib'
CSL = ROOT / 'references' / 'american-chemical-society-2026.csl'
OUT = ROOT / 'build' / 'semester-manuscript'
FIG = OUT / 'figures'
S1_SOURCE = ROOT / 'manuscript' / 'SEMESTER_SUPPLEMENTARY_TABLE_S1_49_REFERENCE_COVERAGE.md'

def run(cmd: list[str]) -> None:
    print('+', ' '.join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_supplementary_s1(pandoc: str) -> None:
    """Build a separate S1 file with a concise index and study-wise evidence notes."""
    if not S1_SOURCE.exists():
        raise SystemExit(f'Missing required supplement source: {S1_SOURCE.relative_to(ROOT)}')
    source_lines = S1_SOURCE.read_text(encoding='utf-8').splitlines()
    data_rows = []
    for line in source_lines:
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 7 or cells[0] in ('Study (author–year)', 'Study'):
            continue
        citation_match = re.search(r'\\cite\{([^}]+)\}', cells[6])
        if not citation_match:
            raise SystemExit(f'Missing citation key for S1 row: {cells[0]}')
        data_rows.append({
            'study': cells[0],
            'title': cells[1],
            'target': cells[2],
            'material': re.split(r';\s*(?:Empirical primary study|Theory/mechanism context only|Review/background context only|Scope-boundary near-miss)', cells[3], maxsplit=1)[0].strip(),
            'source': cells[4],
            'guardrail': cells[5],
            'key': citation_match.group(1),
        })
    if len(data_rows) != 49:
        raise SystemExit(f'Expected 49 selected studies in S1, found {len(data_rows)}')
    labels = [row['study'] for row in data_rows]
    if len(set(labels)) != 49:
        raise SystemExit('Duplicate author-year labels detected in S1.')
    if any(re.search(r'\b(?:SEM|EV-SEM)-\d{3}\b', ' '.join(row.values())) for row in data_rows):
        raise SystemExit('Internal evidence identifiers found in reader-facing S1 data.')

    md = [
        '# Supplementary Table S1. Evidence coverage of the 49 selected references',
        '',
        '**Purpose.** This supplementary register documents the source basis and permitted evidential use of each selected reference. It is an evidence-coverage register, not a quantitative ranking. Abstract-only, preview-only, mirror-derived and internally inconsistent values are retained with explicit qualifications rather than promoted to comparable observed capacities.',
        '',
        '**How to read this file.** Part A provides a compact index. Part B records article titles, source-access tiers and study-specific numeric guardrails as separate labelled fields, rather than placing full paragraphs inside wide table cells. Author–year names are the reader-facing identifiers; project IDs remain in the internal audit crosswalk.',
        '',
        '## Part A. Selected-reference coverage index',
        '',
        '| Study (author–year) | Target | Material family / role |',
        '|---|---|---|',
    ]
    for row in data_rows:
        md.append(f"| {row['study']} | {row['target']} | {row['material']} |")
    md.extend([
        '',
        '## Part B. Study-by-study source and evidence notes',
        '',
    ])
    for idx, row in enumerate(data_rows, 1):
        md.extend([
            f"### {idx}. {row['study']}",
            '',
            f"*{row['title']}*",
            '',
            f"**Target:** {row['target']}",
            '',
            f"**Material family / role:** {row['material']}",
            '',
            f"**Source tier:** {row['source']}",
            '',
            f"**Permitted evidence use / numeric guardrail:** {row['guardrail']}",
            '',
            f"**Citation:** [@{row['key']}]",
            '',
        ])
    md.extend([
        '## Interpretation rules',
        '',
        '1. Source-reported observed qe, mass-balance-derived uptake, kinetic-model-fitted qe, fitted isotherm qmax/qm, removal percentage and column metrics are different endpoints. Do not merge or rank them without a valid common basis.',
        '2. Ciprofloxacin (CIP) is not pooled with norfloxacin or ofloxacin. Tetracycline (TC) is not pooled with chlortetracycline, oxytetracycline or doxycycline.',
        '3. Nguyen et al. (2024) is theory-only; Minale et al. (2020) is review/background only; Ghahremani et al. (2025) is an empirical scope-boundary near-miss and is not part of the core GO/rGO performance comparison.',
        '4. One candidate was omitted from the active 49-work set for administrative/time reasons. This was not a scientific rejection.',
        '5. Full candidate-level source notes, evidence IDs and detailed cautions remain in the internal project registers. They are intentionally not reproduced as reader-facing study identifiers.',
        '',
    ])
    OUT.mkdir(parents=True, exist_ok=True)
    source_md = OUT / 'SEMESTER_SUPPLEMENTARY_TABLE_S1_EVIDENCE_COVERAGE.md'
    source_md.write_text('\n'.join(md), encoding='utf-8')
    common = [
        '--from=markdown+pipe_tables+raw_tex+raw_attribute+tex_math_dollars+tex_math_single_backslash',
        '--citeproc', f'--bibliography={BIB}', f'--csl={CSL}',
        '--standalone', '-V', 'papersize:a4', '-V', 'geometry:margin=18mm',
        '-V', 'fontsize:9.5pt', '-V', 'mainfont:DejaVu Serif',
        '-V', 'sansfont:DejaVu Sans', '-V', 'monofont:DejaVu Sans Mono',
    ]
    docx = OUT / 'SEMESTER_SUPPLEMENTARY_TABLE_S1_EVIDENCE_COVERAGE.docx'
    pdf = OUT / 'SEMESTER_SUPPLEMENTARY_TABLE_S1_EVIDENCE_COVERAGE.pdf'
    run([pandoc, str(source_md)] + common + ['--to=docx', '-o', str(docx)])
    run([pandoc, str(source_md)] + common + ['--pdf-engine=xelatex', '-o', str(pdf)])
    print(f'Supplementary S1 built from {len(data_rows)} selected-study records: {docx}, {pdf}', flush=True)

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
    if len(diagrams) != 4:
        raise SystemExit(f'Expected 4 complete figure blocks, found {len(diagrams)}')
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
    # Table 1D follows the full-page Table 1C. This OpenXML break caused an
    # additional blank Word page, so remove it in DOCX only; PDF is unchanged.
    md_docx = re.sub(
        r'(?s)\n\x60{3}{=openxml}\s*<w:p><w:r><w:br w:type="page"/></w:r></w:p>\s*\x60{3}\s*(?=## Table 1D\. Fitted isotherm-model outputs)',
        '\n',
        md_docx,
    )
    md_pdf = re.sub(r'(?s)\x60{3}{=openxml}.*?\x60{3}', '', md)
    prepared_docx.write_text(md_docx, encoding='utf-8')
    prepared_pdf.write_text(md_pdf, encoding='utf-8')
    common = [
        '--from=markdown+pipe_tables+raw_tex+raw_attribute+tex_math_dollars+tex_math_single_backslash',
        '--citeproc', f'--bibliography={BIB}', f'--csl={CSL}',
        '--resource-path=' + str(OUT), '--standalone',
        '-V', 'papersize:a4', '-V', 'geometry:margin=22mm',
        '-V', 'fontsize:10pt', '-V', 'mainfont:DejaVu Serif',
        '-V', 'sansfont:DejaVu Sans', '-V', 'monofont:DejaVu Sans Mono',
    ]
    docx = OUT / 'SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.docx'
    pdf = OUT / 'SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.pdf'
    run([pandoc, str(prepared_docx)] + common + ['--to=docx', '-o', str(docx)])
    run([pandoc, str(prepared_pdf)] + common + ['--pdf-engine=xelatex', '-o', str(pdf)])
    # Keep the condition-dense Table 1B readable but compact enough to remain
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
                    raise SystemExit('Could not identify Table 1B for compact Word styling.')
                payload = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            output_zip.writestr(item, payload)
    docx_tmp.replace(docx)
    # Keep a concise build manifest next to the outputs.
    (OUT / 'BUILD_INFO.txt').write_text(
        'Working manuscript V2 build\n'
        'Citation style: ACS Guide 2026 (provisional; confirm against AMU/supervisor requirements)\n'
        'Source: manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md\n'
        'Bibliography: semester-manuscript-cited-references-49-selected-plus-4-context.bib\n'
        'Four Mermaid diagrams converted to embedded PNG images.\n'
        'DOCX/PDF require manual full-page visual review before submission.\n',
        encoding='utf-8')
    print('Build complete:', docx, pdf, flush=True)
    build_supplementary_s1(pandoc)

if __name__ == '__main__':
    main()
