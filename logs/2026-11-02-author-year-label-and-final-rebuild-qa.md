# Author–year study labels and final manuscript build QA — 2 November 2026

## Reader-facing naming

The publication-facing manuscript uses author–year labels rather than internal study identifiers. Supplementary Table S1 contains 49 selected-study rows. Main-text Table 1 uses author–year labels in all study-linked panels. The manuscript narrative no longer exposes candidate IDs used as reader-facing labels.

The internal crosswalk remains at docs/SEMESTER_AUTHOR_YEAR_CROSSWALK.md, preserving the mapping between SEM-###, author–year labels and the consolidated bibliography citation keys. Internal evidence IDs and audit registers remain unchanged.

The computational rGO interaction work is labelled **Nguyen et al. (2024)** after correcting the BibTeX author order to match the publisher byline.

## Production identity

- GitHub Actions run: [41438565195](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41438565195) — success.
- Source commit: f3df2c2c3868a30fb9720e287d7836731d3edb9a.
- Artifact ID: 13138200918.
- Artifact digest: sha256:cc6ce7cac4ac6f6bb060ce549b61f3b1d8a14c3a26758809da8726c3336ea0ee.
- Output: 31-page A4 PDF and 39-page DOCX.

## Layout and output checks

- Word Table 1B fits 19 condition rows on one page with compact 9-pt table text.
- Table 1C fits all 28 separately labelled endpoint rows on one page.
- The redundant Word page break before Table 1D was removed; Table 1D begins on page 22 with no intervening blank page.
- PDF remains 31 pages and retains its own authored page breaks.
- PDF preflight passed: openable, searchable, unencrypted, no XFA.
- Exported PDF and DOCX contain none of these internal/editorial markers: SEM-###, EV-SEM-###, CORP-031, “Cite with”.
- DOCX accessibility audit: 0 high, 0 medium, 53 low. All low-severity findings are DOI hyperlinks displayed as raw URLs.

## Scope and remaining holds

The naming change did not alter reference selection, reported scientific values, model/observed endpoint distinctions, source tiers, caveats or study holds. The active selection remains 49 works plus four contextual references. ACS-numbered citation formatting remains provisional pending AMU/supervisor confirmation. The separate S1 file, author/declaration fields, language proof and final sentence-level source-pin pass remain outstanding.
