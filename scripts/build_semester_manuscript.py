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

def run(cmd: list[str]) -> None:
    print('+', ' '.join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=ROOT)

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

if __name__ == '__main__':
    main()
