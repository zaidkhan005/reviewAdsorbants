#!/usr/bin/env python3
"""Validate the structure and minimum data-quality rules for research registers.

This checks bookkeeping integrity only. It does not validate scientific claims,
paper relevance, or whether a journal is genuinely Q1; those require source review.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

SCREENING_REQUIRED = [
    "Candidate ID", "Category", "Paper", "Year", "Journal", "DOI or URL",
    "Study type", "Relevance to continuum", "Q1 provider", "Q1 year",
    "Q1 category", "Q1 quartile", "Q1 verification source", "Full text checked",
    "Decision", "Notes",
]
CORPUS_SCREENING_REQUIRED = [
    "Candidate ID", "Category (preliminary)", "Paper", "Year", "Journal",
    "DOI or URL", "Study type (preliminary)", "Relevance to continuum",
    "Q1 quartile", "Full text checked", "Decision", "Notes",
]

EVIDENCE_REQUIRED = [
    "Paper", "Year", "DOI", "Material", "Antibiotic", "Stage",
    "Main reported evidence", "Real water", "Regeneration", "Data-quality caveat",
]
VALID_QUARTILES = {"Q1", "Q2", "Q3", "Q4", "PENDING", "PENDING VERIFICATION", "N/A", "NOT APPLICABLE", ""}


def load_csv(path: Path, required: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"Missing required file: {path.relative_to(ROOT)}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        missing = [name for name in required if name not in headers]
        if missing:
            raise ValueError(f"{path.relative_to(ROOT)}: missing columns: {missing}")
        rows = []
        for line_no, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: extra fields; check CSV quoting")
            if not any((value or "").strip() for value in row.values()):
                continue
            rows.append(row)
    if not rows:
        raise ValueError(f"{path.relative_to(ROOT)}: no data rows found")
    return rows


def validate_year(row: dict[str, str], key: str, path: Path, line_no: int) -> None:
    value = (row.get(key) or "").strip()
    if not value.isdigit() or not (1900 <= int(value) <= 2027):
        raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: invalid {key}: {value!r}")


def validate_screening() -> int:
    path = ROOT / "data" / "paper-screening-register.csv"
    rows = load_csv(path, SCREENING_REQUIRED)
    seen: set[str] = set()
    for line_no, row in enumerate(rows, start=2):
        candidate_id = (row.get("Candidate ID") or "").strip()
        if not candidate_id:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Candidate ID is required")
        if candidate_id in seen:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: duplicate Candidate ID {candidate_id}")
        seen.add(candidate_id)
        if not (row.get("Paper") or "").strip():
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Paper title is required")
        validate_year(row, "Year", path, line_no)

        link = (row.get("DOI or URL") or "").strip()
        parsed = urlparse(link)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: DOI or URL must be a full http(s) URL")

        quartile = (row.get("Q1 quartile") or "").strip().upper()
        if quartile not in VALID_QUARTILES:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: unsupported quartile value {quartile!r}")
        if quartile == "Q1":
            q1_fields = ["Q1 provider", "Q1 year", "Q1 category", "Q1 verification source"]
            missing = [key for key in q1_fields if not (row.get(key) or "").strip()]
            if missing:
                raise ValueError(
                    f"{path.relative_to(ROOT)}:{line_no}: Q1 requires provider/year/category/source; missing {missing}"
                )
            q1_source = urlparse((row.get("Q1 verification source") or "").strip())
            if q1_source.scheme not in {"http", "https"} or not q1_source.netloc:
                raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Q1 verification source must be a full URL")
    return len(rows)


def validate_corpus_screening() -> int:
    """Validate the unified downloaded/discovered literature corpus register."""
    path = ROOT / "data" / "corpus-screening-register.csv"
    rows = load_csv(path, CORPUS_SCREENING_REQUIRED)
    seen: set[str] = set()
    for line_no, row in enumerate(rows, start=2):
        candidate_id = (row.get("Candidate ID") or "").strip()
        if not candidate_id:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Candidate ID is required")
        if candidate_id in seen:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: duplicate Candidate ID {candidate_id}")
        seen.add(candidate_id)
        if not (row.get("Paper") or "").strip():
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Paper title is required")
        validate_year(row, "Year", path, line_no)
        link = (row.get("DOI or URL") or "").strip()
        parsed = urlparse(link)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: DOI or URL must be a full http(s) URL")
        quartile = (row.get("Q1 quartile") or "").strip().upper()
        if quartile not in VALID_QUARTILES:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: unsupported quartile value {quartile!r}")
        if quartile == "Q1":
            q1_fields = ["Q1 provider", "Q1 year", "Q1 category", "Q1 verification source"]
            missing = [key for key in q1_fields if not (row.get(key) or "").strip()]
            if missing:
                raise ValueError(
                    f"{path.relative_to(ROOT)}:{line_no}: Q1 requires provider/year/category/source; missing {missing}"
                )
            q1_source = urlparse((row.get("Q1 verification source") or "").strip())
            if q1_source.scheme not in {"http", "https"} or not q1_source.netloc:
                raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Q1 verification source must be a full URL")
    return len(rows)


def validate_evidence() -> int:
    path = ROOT / "data" / "master-evidence.csv"
    rows = load_csv(path, EVIDENCE_REQUIRED)
    seen: set[tuple[str, str]] = set()
    for line_no, row in enumerate(rows, start=2):
        paper = (row.get("Paper") or "").strip()
        if not paper:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: Paper is required")
        validate_year(row, "Year", path, line_no)
        key = (paper.casefold(), (row.get("Year") or "").strip())
        if key in seen:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: duplicate paper/year entry {key}")
        seen.add(key)
        doi = (row.get("DOI") or "").strip()
        if doi and not (doi.startswith("10.") or doi.startswith("https://doi.org/")):
            raise ValueError(f"{path.relative_to(ROOT)}:{line_no}: DOI should be a DOI string or doi.org URL")
    return len(rows)


def main() -> int:
    try:
        screening_count = validate_screening()
        corpus_count = validate_corpus_screening()
        evidence_count = validate_evidence()
    except (OSError, csv.Error, ValueError) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"Validation passed: {screening_count} interim candidates; {corpus_count} full-corpus/discovery records; {evidence_count} historical core evidence records.")
    print("Reminder: this validates register structure only, not scientific accuracy or Q1 status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
