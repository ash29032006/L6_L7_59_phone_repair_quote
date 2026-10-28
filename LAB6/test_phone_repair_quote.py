import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value

#Example test cases:
def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600

def test_in_stock_quick():
    assert repair_days("battery", True, 2) == 1

# Write the rest of the test cases so that the code is 90- 100% covered.

def test_repair_quote_flagship_express():
    assert repair_quote("battery", "flagship", False, True) == 3800

def test_repair_quote_warranty_non_screen():
    assert repair_quote("battery", "budget", True, False) == 300

def test_repair_quote_invalid_part():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("speaker", "budget", False, False)

def test_repair_quote_invalid_tier():
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "premium", False, False)

def test_repair_days_technicians_busy():
    assert repair_days("screen", True, 0) == 3

def test_repair_days_out_of_stock_screen():
    assert repair_days("screen", False, 1) == 6

def test_repair_days_out_of_stock_camera():
    assert repair_days("camera", False, 1) == 6

def test_repair_days_out_of_stock_other():
    assert repair_days("charging_port", False, 1) == 3

def test_trade_in_invalid_price():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 12, False)

def test_trade_in_invalid_age():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(10000, -1, False)

def test_trade_in_over_48():
    assert trade_in_value(25000, 50, False) == 0

def test_trade_in_under_12():
    assert trade_in_value(30000, 8, False) == 18000

def test_trade_in_13_to_24():
    assert trade_in_value(30000, 20, False) == 12000

def test_trade_in_25_to_48():
    assert trade_in_value(30000, 30, False) == 6000

def test_trade_in_cracked():
    assert trade_in_value(30000, 8, True) == 9000

