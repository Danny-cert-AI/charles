import math
import pytest

def shares_to_trade(target_percentage, current_percentage, share_price, total_investment=100_000):
    if share_price <= 0:
        raise ValueError("share price invalid")

    difference_percentage = current_percentage - target_percentage
    difference_in_dollars = difference_percentage / 100 * total_investment
    raw_shares = difference_in_dollars / share_price
    return math.ceil(raw_shares)

# security, target, current, unit_price, expected signed shares
SECURITIES = [
    ("IBM", 20, 10, 150, -66),
    ("MSFT", 20, 20, 90, 0),
    ("ORCL", 20, 30, 220, 46),
    ("AAPL", 20, 20, 450, 0),
    ("HD", 20, 20, 70, 0),
]

@pytest.mark.parametrize("name, target_pct, current_pct, unit_price, expected", SECURITIES)
def test_shares_to_trade_matches_expected(name, target_pct, current_pct, unit_price, expected):
    assert shares_to_trade(target_pct, current_pct, unit_price) == expected

def test_too_few_shares_buy():
    # IBM is under target (10% held vs 20% target)
    result = shares_to_trade(target_percentage=20, current_percentage=10, share_price=150)
    assert result < 0

def test_too_many_shares_sell():
    # ORCL is over target (30% held vs 20% target)
    result = shares_to_trade(target_percentage=20, current_percentage=30, share_price=220)
    assert result > 0

def test_20_percent_no_trade():
    # MSFT, AAPL and HD shouldn't change
    result = shares_to_trade(target_percentage=20, current_percentage=20, share_price=90)
    assert result == 0

def test_fractional_shares_round_up():
    # $10,000 / $220 = 45.4545  verify rounding up works correctly.
    result = shares_to_trade(target_percentage=20, current_percentage=30, share_price=220)
    assert result == 46



def test_invalid_shareprice_is_rejected():
    with pytest.raises(ValueError):
        shares_to_trade(target_percentage=20, current_percentage=10, share_price=0)
