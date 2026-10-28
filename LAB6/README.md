# L6_L7_59 — Phone Repair Quote

Lab 6: Code and Branch Coverage Analysis

## Student Details
- **Course:** Software Engineering (SE)
- **Lab:** Lab 6 (Code and Branch Coverage)
- **Name:** Ashwin C H
- **SRN:** PES1UG24AM900

## About
A Python module that computes quotes for phone repairs by part, brand tier, warranty status, and express handling, estimates repair turnaround days based on technician availability and spare parts stock, and evaluates trade-in values for pre-owned devices.

## Files

| File | Description |
|---|---|
| `phone_repair_quote.py` | The application module under test |
| `test_phone_repair_quote.py` | Primary comprehensive test suite |
| `CodeCoverageTest_phone_repair_quote.py` | Test suite targeted for >=90% statement/line coverage (achieved 100%) |
| `BranchCoverageTest_phone_repair_quote.py` | Test suite targeted for >=90% branch coverage (achieved 100%) |
| `screenshots/` | Terminal output screenshots showing coverage reports |

## Running Coverage Analysis

### 1. Line/Statement Coverage
Run tests and measure statement coverage:
```bash
coverage run -m pytest CodeCoverageTest_phone_repair_quote.py
coverage report -m
```

### 2. Branch Coverage
Run tests and measure branch coverage:
```bash
coverage run --branch -m pytest BranchCoverageTest_phone_repair_quote.py
coverage report -m
```

## Coverage Results Summary

| Metric | Initial Test Suite | Improved Test Suite | Target |
|---|---|---|---|
| **Statement Coverage** | 45% (22 missed lines) | **100%** (0 missed lines) | >= 90% |
| **Branch Coverage** | 38% (8 partial branches) | **100%** (28/28 branches) | >= 90% |
| **Tests Passed** | 2 passed | **19 passed** | All passed |
