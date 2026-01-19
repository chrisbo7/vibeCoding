"""
test_crypto_leverage.py
Unit tests for crypto_leverage.py calculation functions.
"""

from crypto_leverage import (
    validate_positive_number,
    calculate_position,
    calculate_stop_loss,
    calculate_take_profit,
    calculate_risk_reward_ratio,
)


def test_validate_positive_number_valid():
    """Test validation with valid inputs."""
    assert validate_positive_number("100", "test") == 100.0
    assert validate_positive_number("45000.50", "test") == 45000.50
    print("✓ Valid number validation works")


def test_validate_positive_number_invalid():
    """Test validation rejects invalid inputs."""
    try:
        validate_positive_number("abc", "test")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Rejects non-numeric input")

    try:
        validate_positive_number("-100", "test")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Rejects negative numbers")

    try:
        validate_positive_number("0", "test")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Rejects zero")


def test_calculate_position_basic():
    """Test position calculation with basic values."""
    result = calculate_position(current_price=50000, investment_amount=10000, leverage=10)
    
    assert result["entry_price"] == 50000
    assert result["initial_capital"] == 10000
    assert result["effective_capital"] == 100000  # 10000 * 10
    assert result["position_size"] == 2.0  # 100000 / 50000
    print("✓ Basic position calculation correct")


def test_calculate_position_fractional():
    """Test position calculation with fractional results."""
    result = calculate_position(current_price=45000, investment_amount=5000, leverage=10)
    
    expected_position = (5000 * 10) / 45000  # ~1.111...
    assert abs(result["position_size"] - expected_position) < 0.0001
    print("✓ Fractional position calculation correct")


def test_calculate_stop_loss_5_percent():
    """Test stop loss calculation for 5% stop loss."""
    stop_loss = calculate_stop_loss(entry_price=50000, stop_loss_percent=5)
    
    expected = 50000 * 0.95  # 47500
    assert stop_loss == expected
    print("✓ 5% stop loss calculation correct")


def test_calculate_stop_loss_10_percent():
    """Test stop loss calculation for 10% stop loss."""
    stop_loss = calculate_stop_loss(entry_price=45000, stop_loss_percent=10)
    
    expected = 45000 * 0.90  # 40500
    assert stop_loss == expected
    print("✓ 10% stop loss calculation correct")


def test_calculate_take_profit_x10():
    """Test take profit calculation for 10% profit target."""
    tp = calculate_take_profit(entry_price=50000, profit_percent=10.0)
    
    # TP = 50000 * (1 + 10/100) = 50000 * 1.1 = 55000
    expected = 50000 * 1.1
    assert abs(tp - expected) < 0.01
    print("✓ Take profit (10% target) calculation correct")


def test_calculate_take_profit_x5():
    """Test take profit calculation for 20% profit target."""
    tp = calculate_take_profit(entry_price=40000, profit_percent=20.0)
    
    # TP = 40000 * (1 + 20/100) = 40000 * 1.2 = 48000
    expected = 40000 * 1.2
    assert abs(tp - expected) < 0.01
    print("✓ Take profit (20% target) calculation correct")


def test_calculate_risk_reward_ratio():
    """Test risk/reward ratio calculation."""
    entry = 50000
    stop_loss = 47500  # 5% below entry
    take_profit = 55000  # 10% above entry
    
    ratio = calculate_risk_reward_ratio(entry, stop_loss, take_profit)
    
    # Risk = 2500, Reward = 5000, Ratio = 5000/2500 = 2.0
    assert ratio == 2.0
    print("✓ Risk/reward ratio calculation correct")


def test_calculate_risk_reward_ratio_edge_case():
    """Test risk/reward with equal risk and reward."""
    entry = 10000
    stop_loss = 9500  # 5% loss
    take_profit = 10500  # 5% gain
    
    ratio = calculate_risk_reward_ratio(entry, stop_loss, take_profit)
    
    # Risk = 500, Reward = 500, Ratio = 1.0
    assert ratio == 1.0
    print("✓ 1:1 risk/reward ratio correct")


def test_full_scenario_small_investment():
    """Test complete scenario with small investment."""
    # Entry: $45,000, Investment: $1,000, Stop loss: 5%, Profit target: 10%
    current_price = 45000
    investment = 1000
    stop_loss_pct = 5
    profit_target_pct = 10

    position = calculate_position(current_price, investment, leverage=10)
    stop_loss = calculate_stop_loss(current_price, stop_loss_pct)
    take_profit = calculate_take_profit(current_price, profit_target_pct)

    # Position size = 10000 / 45000 = 0.222...
    assert abs(position["position_size"] - (10000 / 45000)) < 0.0001
    
    # Stop loss = 45000 * 0.95 = 42750
    assert abs(stop_loss - 42750) < 0.01
    
    # Take profit = 45000 * 1.1 = 49500
    assert abs(take_profit - 49500) < 0.01
    
    print("✓ Full scenario (small investment) works correctly")


def test_full_scenario_large_investment():
    """Test complete scenario with large investment."""
    # Entry: $50,000, Investment: $100,000, Stop loss: 3%, Profit target: 15%
    current_price = 50000
    investment = 100000
    stop_loss_pct = 3
    profit_target_pct = 15

    position = calculate_position(current_price, investment, leverage=10)
    stop_loss = calculate_stop_loss(current_price, stop_loss_pct)
    take_profit = calculate_take_profit(current_price, profit_target_pct)

    # Position size = 1000000 / 50000 = 20
    assert abs(position["position_size"] - 20.0) < 0.0001
    
    # Stop loss = 50000 * 0.97 = 48500
    assert abs(stop_loss - 48500) < 0.01
    
    # Take profit = 50000 * 1.15 = 57500
    assert abs(take_profit - 57500) < 0.01
    
    print("✓ Full scenario (large investment) works correctly")


if __name__ == "__main__":
    tests = [
        test_validate_positive_number_valid,
        test_validate_positive_number_invalid,
        test_calculate_position_basic,
        test_calculate_position_fractional,
        test_calculate_stop_loss_5_percent,
        test_calculate_stop_loss_10_percent,
        test_calculate_take_profit_x10,
        test_calculate_take_profit_x5,
        test_calculate_risk_reward_ratio,
        test_calculate_risk_reward_ratio_edge_case,
        test_full_scenario_small_investment,
        test_full_scenario_large_investment,
    ]

    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {type(e).__name__}: {e}")
            failed += 1

    print()
    if failed:
        print(f"❌ {failed}/{len(tests)} tests failed")
        exit(1)
    else:
        print(f"✅ All {len(tests)} tests passed!")
