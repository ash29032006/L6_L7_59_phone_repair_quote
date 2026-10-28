import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# ============================================================================
# Branch Coverage Tests for repair_quote
# ============================================================================

def test_branch_part_invalid():
    # Branch: part not in PART_COST -> True
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("housing", "budget", False, False)


def test_branch_part_valid_tier_invalid():
    # Branch: part in PART_COST -> False; brand_tier not in (...) -> True
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "luxury", False, False)


def test_branch_budget_screen_no_warranty_standard():
    # part=="screen" (True, labour=600), brand=="flagship" (False),
    # under_warranty (False), express (False)
    assert repair_quote("screen", "budget", False, False) == 4600


def test_branch_flagship_non_screen_no_warranty_express():
    # brand=="flagship" (True, cost*2), part=="screen" (False, labour=300),
    # under_warranty (False), express (True, +500)
    # camera: 2500 * 2 + 300 + 500 = 5800
    assert repair_quote("camera", "flagship", False, True) == 5800


def test_branch_warranty_screen_not_waived():
    # under_warranty (True) AND part != "screen" (False) -> cost is NOT zeroed
    # screen warranty exception: 4000 + 600 = 4600
    assert repair_quote("screen", "budget", True, False) == 4600


def test_branch_warranty_non_screen_waived():
    # under_warranty (True) AND part != "screen" (True) -> cost = 0
    # charging_port: 0 + 300 = 300
    assert repair_quote("charging_port", "budget", True, False) == 300


# ============================================================================
# Branch Coverage Tests for repair_days
# ============================================================================

def test_branch_technicians_busy_in_stock():
    # technicians_free == 0 (True -> 3 days), parts_in_stock (True)
    assert repair_days("screen", True, 0) == 3


def test_branch_technicians_free_in_stock():
    # technicians_free != 0 (False -> 1 day), parts_in_stock (True)
    assert repair_days("battery", True, 3) == 1


def test_branch_out_of_stock_screen():
    # parts_in_stock == False (True), part == "screen" (True -> +5 days)
    # 1 + 5 = 6
    assert repair_days("screen", False, 1) == 6


def test_branch_out_of_stock_camera():
    # parts_in_stock == False (True), part == "screen" (False), part == "camera" (True -> +5 days)
    # 1 + 5 = 6
    assert repair_days("camera", False, 1) == 6


def test_branch_out_of_stock_other_part():
    # parts_in_stock == False (True), part neither screen nor camera (False -> +2 days)
    # 1 + 2 = 3
    assert repair_days("battery", False, 1) == 3


# ============================================================================
# Branch Coverage Tests for trade_in_value
# ============================================================================

def test_branch_trade_in_invalid_price_zero():
    # original_price <= 0 (True)
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 10, False)


def test_branch_trade_in_invalid_price_negative():
    # original_price < 0 (True)
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(-500, 10, False)


def test_branch_trade_in_invalid_age_negative():
    # original_price > 0 (False), age_months < 0 (True)
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(20000, -2, False)


def test_branch_trade_in_age_over_48():
    # age_months > 48 (True) -> return 0
    assert trade_in_value(30000, 49, False) == 0


def test_branch_trade_in_age_boundary_12_uncracked():
    # age_months <= 12 (True, 60%), screen_cracked (False)
    # 40000 * 60 // 100 = 24000
    assert trade_in_value(40000, 12, False) == 24000


def test_branch_trade_in_age_boundary_24_uncracked():
    # age_months <= 24 (True, 40%), screen_cracked (False)
    # 40000 * 40 // 100 = 16000
    assert trade_in_value(40000, 24, False) == 16000


def test_branch_trade_in_age_boundary_48_uncracked():
    # age_months > 24 (False), age_months <= 48 (True, 20%), screen_cracked (False)
    # 40000 * 20 // 100 = 8000
    assert trade_in_value(40000, 48, False) == 8000


def test_branch_trade_in_screen_cracked():
    # screen_cracked (True) -> value // 2
    # 40000 * 60 // 100 // 2 = 12000
    assert trade_in_value(40000, 5, True) == 12000
