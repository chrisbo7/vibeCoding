"""
demo_crypto_leverage.py
Demonstration script that runs the crypto leverage calculator with sample values
and shows the calculation step-by-step.
"""

from crypto_leverage import (
    calculate_position,
    calculate_stop_loss,
    calculate_take_profit,
    calculate_risk_reward_ratio,
)


def demo():
    """Run a demo with sample values."""
    print("\n" + "=" * 70)
    print("🚀 CRYPTO LEVERAGE CALCULATOR DEMO - SHOWING CALCULATIONS")
    print("=" * 70)

    # Sample inputs
    current_price = 50000
    investment_amount = 25000
    stop_loss_percent = 5
    profit_target_percent = 10

    print("\n📥 SAMPLE INPUTS:")
    print(f"  Current Price (Entry):        ${current_price:,.2f}")
    print(f"  Investment Amount:            ${investment_amount:,.2f}")
    print(f"  Stop Loss Tolerance:          {stop_loss_percent:.2f}%")
    print(f"  Target Profit Goal:           {profit_target_percent:.2f}%")
    print(f"  Leverage:                     x10")

    # Calculate position
    position_info = calculate_position(current_price, investment_amount, leverage=10)

    print("\n" + "-" * 70)
    print("💼 POSITION CALCULATION:")
    print("-" * 70)
    print(f"\n  Formula: Position Size = (Investment × Leverage) / Current Price")
    print(f"  Formula: Position Size = ({investment_amount:,.2f} × 10) / {current_price:,.2f}")
    print(f"  Formula: Position Size = {investment_amount * 10:,.2f} / {current_price:,.2f}")
    print(f"  ➜ Result: {position_info['position_size']:.8f} BTC/ETH")
    print(f"\n  You can control {position_info['position_size']:.8f} BTC/ETH with ${investment_amount:,.2f}")
    print(f"  (Effective buying power: ${position_info['effective_capital']:,.2f})")

    # Calculate stop loss
    stop_loss_price = calculate_stop_loss(current_price, stop_loss_percent)

    print("\n" + "-" * 70)
    print("🛑 STOP LOSS CALCULATION:")
    print("-" * 70)
    print(f"\n  Formula: Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)")
    print(f"  Formula: Stop Loss Price = ${current_price:,.2f} × (1 - {stop_loss_percent}/100)")
    print(f"  Formula: Stop Loss Price = ${current_price:,.2f} × {1 - stop_loss_percent/100:.4f}")
    print(f"  Formula: Stop Loss Price = ${current_price:,.2f} × 0.95")
    print(f"  ➜ Result: ${stop_loss_price:,.2f}")
    
    loss_amount = investment_amount * (stop_loss_percent / 100)
    print(f"\n  If price hits ${stop_loss_price:,.2f}, you lose: ${loss_amount:,.2f}")

    # Calculate take profit
    take_profit_price = calculate_take_profit(current_price, profit_target_percent)

    print("\n" + "-" * 70)
    print("📈 TAKE PROFIT CALCULATION:")
    print("-" * 70)
    print(f"\n  Formula: Take Profit Price = Entry Price × (1 + Target Profit % / 100)")
    print(f"  Formula: Take Profit Price = ${current_price:,.2f} × (1 + {profit_target_percent}/100)")
    print(f"  Formula: Take Profit Price = ${current_price:,.2f} × {1 + profit_target_percent/100:.4f}")
    print(f"  Formula: Take Profit Price = ${current_price:,.2f} × 1.10")
    print(f"  ➜ Result: ${take_profit_price:,.2f}")
    
    profit_amount = investment_amount * (profit_target_percent / 100)
    print(f"\n  If price reaches ${take_profit_price:,.2f}, you make: ${profit_amount:,.2f}")
    print(f"  That's a {(take_profit_price - current_price) / current_price * 100:.2f}% price move")

    # Calculate risk/reward ratio
    risk_reward = calculate_risk_reward_ratio(current_price, stop_loss_price, take_profit_price)

    print("\n" + "=" * 70)
    print("⚖️  RISK/REWARD ANALYSIS:")
    print("=" * 70)
    print(f"\n  Risk (amount you can lose):     ${loss_amount:,.2f}")
    print(f"  Reward (amount you can gain):   ${profit_amount:,.2f}")
    print(f"\n  Formula: Risk/Reward Ratio = Reward / Risk")
    print(f"  Formula: Risk/Reward Ratio = {profit_amount:,.2f} / {loss_amount:,.2f}")
    print(f"  ➜ Result: 1:{risk_reward:.2f}")
    print(f"\n  ✅ For every $1 you risk, you stand to make ${risk_reward:.2f}")

    print("\n" + "=" * 70)
    print("📊 FINAL TRADE SUMMARY:")
    print("=" * 70)
    print(f"\n  Entry Point:      ${current_price:,.2f}")
    print(f"  Stop Loss:        ${stop_loss_price:,.2f}  (lose ${loss_amount:,.2f} if hit)")
    print(f"  Take Profit:      ${take_profit_price:,.2f}  (gain ${profit_amount:,.2f} if hit)")
    print(f"  Position Size:    {position_info['position_size']:.8f} BTC/ETH (worth ${position_info['effective_capital']:,.2f} at entry)")
    print(f"  Risk/Reward:      1:{risk_reward:.2f}")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    demo()
