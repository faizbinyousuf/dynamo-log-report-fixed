import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_exists_and_is_valid_json():
    """Verifies success criterion 1: /app/report.json exists and contains valid JSON."""
    assert REPORT_PATH.exists(), "Expected /app/report.json to exist"
    report = load_report()
    assert isinstance(report, dict), "Expected report to be a JSON object"


def test_report_has_exact_expected_keys():
    """Verifies success criterion 1: the report has exactly the required keys."""
    report = load_report()
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies success criterion 2: total_requests equals the number of non-empty access log lines."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Verifies success criterion 3: unique_ips equals the number of distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Verifies success criterion 4: top_path equals the most frequently requested URL path."""
    report = load_report()
    assert report["top_path"] ==  "/index.html"
