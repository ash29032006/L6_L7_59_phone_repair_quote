import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# --- Tests for repair_quote ---

def test_repair_quote_budget_screen():
    # screen, budget, no warranty, no express -> 4000 + 600 = 4600
    assert repair_quote("screen", "budget", False, False) == 4600


def test_repair_quote_flagship_express():
    # battery (1500 * 2 = 3000), labour 300, express 500 -> 3800
    assert repair_quote("battery", "flagship", False, True) == 3800


def test_repair_quote_under_warranty_non_screen():
    # battery under warranty -> cost waived (0) + labour 300 = 300
    assert repair_quote("battery", "budget", True, False) == 300


def test_repair_quote_invalid_part():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("motherboard", "budget", False, False)


def test_repair_quote_invalid_brand_tier():
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "midrange", False, False)


# --- Tests for repair_days ---

def test_repair_days_technicians_busy():
    # technicians_free == 0 -> 3 days, in stock -> 3
    assert repair_days("screen", True, 0) == 3


def test_repair_days_technicians_free_in_stock():
    # technicians_free > 0 -> 1 day, in stock -> 1
    assert repair_days("battery", True, 2) == 1


def test_repair_days_screen_out_of_stock():
    # 1 + 5 = 6 days
    assert repair_days("screen", False, 1) == 6


def test_repair_days_other_part_out_of_stock():
    # battery out of stock -> 1 + 2 = 3 days
    assert repair_days("battery", False, 1) == 3


# --- Tests for trade_in_value ---

def test_trade_in_invalid_price():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 10, False)


def test_trade_in_invalid_age():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(20000, -1, False)


def test_trade_in_over_48_months():
    assert trade_in_value(30000, 50, False) == 0


def test_trade_in_under_12_months():
    # 50000 * 0.60 = 30000
    assert trade_in_value(50000, 6, False) == 30000


def test_trade_in_13_to_24_months():
    # 50000 * 0.40 = 20000
    assert trade_in_value(50000, 18, False) == 20000


def test_trade_in_25_to_48_months():
    # 50000 * 0.20 = 10000
    assert trade_in_value(50000, 36, False) == 10000


def test_trade_in_screen_cracked():
    # 50000 * 0.60 // 2 = 15000
    assert trade_in_value(50000, 10, True) == 15000
