"""
crypto_leverage.py
Calculate crypto trading position with x10 leverage.

Features:
  - Fetch real-time crypto prices from CoinGecko API
  - User selects which asset to trade (BTC, ETH, etc)
  - Prompts for investment amount, stop loss %, profit target %

Calculates and displays with formulas:
  - Position size (amount of crypto to buy)
  - Entry price (real-time)
  - Stop loss price and formula
  - Take profit price and formula
  - Risk/reward ratio and potential profit/loss

Usage:
    python crypto_leverage.py
"""

from __future__ import annotations

import sys
from typing import Optional

try:
    import requests
except ImportError:
    requests = None  # type: ignore


# Mapping of common crypto symbols to CoinGecko IDs
SYMBOL_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "ADA": "cardano",
    "XRP": "ripple",
    "DOT": "polkadot",
    "DOGE": "dogecoin",
    "MATIC": "matic-network",
    "AVAX": "avalanche-2",
    "ARB": "arbitrum",
    "OP": "optimism",
    "LINK": "chainlink",
    "UNI": "uniswap",
    "AAVE": "aave",
    "LTC": "litecoin",
    "BCH": "bitcoin-cash",
}


def validate_positive_number(value: str, name: str) -> float:
    """Validate and convert input to positive float."""
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{name} must be positive")
        return num
    except ValueError as e:
        raise ValueError(f"Invalid {name}: {e}")


def fetch_crypto_price(symbol: str) -> tuple[float, str, str]:
    """
    Fetch real-time crypto price from CoinGecko API.
    
    Args:
        symbol: Crypto symbol (BTC, ETH, SOL, etc)
    
    Returns:
        Tuple of (price, asset_name, symbol) or raises ValueError
    
    Raises:
        ValueError: If API fails or symbol not found
    """
    if requests is None:
        raise ValueError(
            "requests library not installed. "
            "Install with: pip install requests"
        )
    
    # Mapping of common symbols to CoinGecko IDs
    symbol_upper = symbol.upper()
    
    if symbol_upper not in SYMBOL_MAP:
        available = ", ".join(sorted(SYMBOL_MAP.keys()))
        raise ValueError(
            f"Asset '{symbol}' not found.\n"
            f"Available: {available}"
        )
    
    gecko_id = SYMBOL_MAP[symbol_upper]
    
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": gecko_id,
            "vs_currencies": "usd",
            "include_market_cap": "false",
            "include_24hr_vol": "false",
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if gecko_id not in data or "usd" not in data[gecko_id]:
            raise ValueError(f"Could not fetch price for {symbol}")
        
        price = data[gecko_id]["usd"]
        
        return price, SYMBOL_MAP[symbol_upper], symbol_upper
    
    except requests.exceptions.RequestException as e:
        raise ValueError(
            f"Failed to fetch price from API: {e}\n"
            f"Make sure you have internet connection.\n"
            f"Or enter price manually."
        )


def select_crypto_asset() -> tuple[float, str, str]:
    """
    Let user select a crypto asset and fetch real-time price.
    
    Returns:
        Tuple of (current_price, asset_name, symbol)
    """
    print("\n" + "=" * 60)
    print("🪙 SELECT CRYPTO ASSET")
    print("=" * 60 + "\n")
    
    print("Available assets:")
    print("  BTC, ETH, SOL, ADA, XRP, DOT, DOGE, MATIC, AVAX")
    print("  ARB, OP, LINK, UNI, AAVE, LTC, BCH")
    print()
    
    while True:
        symbol = input("📌 Enter asset symbol (e.g., BTC): ").strip().upper()
        
        if not symbol:
            print("❌ Please enter a symbol.\n")
            continue
        
        try:
            print(f"📡 Fetching price for {symbol}...")
            current_price, asset_name, symbol_upper = fetch_crypto_price(symbol)
            print(f"✅ {asset_name.upper()}: ${current_price:,.2f}\n")
            return current_price, asset_name, symbol_upper
        
        except ValueError as e:
            error_msg = str(e)
            if "not found" in error_msg:
                print(f"❌ {e}\n")
                continue
            else:
                # API/network error - offer manual input
                print(f"⚠️  {e}")
                print("   Switching to manual price input.\n")
                
                # Fallback to manual input
                while True:
                    try:
                        price = validate_positive_number(
                            input(f"💰 Enter {symbol} price in USD: $").strip(),
                            f"{symbol} price"
                        )
                        return price, SYMBOL_MAP.get(symbol, symbol), symbol
                    except ValueError as ve:
                        print(f"❌ {ve}. Please try again.\n")
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")
            print("⚠️  Switching to manual price input.\n")
            
            # Fallback to manual input
            while True:
                try:
                    price = validate_positive_number(
                        input(f"💰 Enter {symbol} price in USD: $").strip(),
                        f"{symbol} price"
                    )
                    return price, SYMBOL_MAP.get(symbol, symbol), symbol
                except ValueError as ve:
                    print(f"❌ {ve}. Please try again.\n")


def get_user_inputs() -> tuple[float, float, float, float, str, str]:
    """
    Get user inputs for crypto leverage calculation.
    
    Prompts for:
      1. Crypto asset selection (fetches real-time price)
      2. Investment amount
      3. Stop loss percentage
      4. Target profit percentage
    
    Returns: (current_price, investment_amount, stop_loss_percent, profit_target_percent, asset_name, symbol)
    """
    print("\n" + "=" * 60)
    print("🚀 CRYPTO LEVERAGE CALCULATOR (x10)")
    print("=" * 60 + "\n")

    # Select crypto asset and fetch price
    current_price, asset_name, symbol = select_crypto_asset()

    # Investment amount
    while True:
        try:
            investment_amount = validate_positive_number(
                input("💰 Enter investment amount in USD (e.g., 10000): ").strip(),
                "investment amount"
            )
            break
        except ValueError as e:
            print(f"❌ {e}. Please try again.\n")

    # Stop loss percentage
    while True:
        try:
            stop_loss_percent = validate_positive_number(
                input("🛑 Enter stop loss percentage (e.g., 5): ").strip(),
                "stop loss percentage"
            )
            if stop_loss_percent >= 100:
                print("❌ Stop loss percentage must be less than 100%. Please try again.\n")
                continue
            break
        except ValueError as e:
            print(f"❌ {e}. Please try again.\n")

    # Target profit percentage
    while True:
        try:
            profit_target_percent = validate_positive_number(
                input("📈 Enter target profit percentage (e.g., 10): ").strip(),
                "target profit percentage"
            )
            if profit_target_percent >= 100:
                print("❌ Target profit percentage must be less than 100%. Please try again.\n")
                continue
            break
        except ValueError as e:
            print(f"❌ {e}. Please try again.\n")

    return current_price, investment_amount, stop_loss_percent, profit_target_percent, asset_name, symbol


def calculate_position(
    current_price: float,
    investment_amount: float,
    leverage: int = 10
) -> dict[str, float]:
    """
    Calculate position size with leverage.
    
    With x10 leverage:
      - Effective buying power = investment_amount * leverage
      - Position size (crypto amount) = (investment_amount * leverage) / current_price
    
    Returns dict with:
      - position_size: amount of crypto to buy
      - entry_price: the price at which we enter
      - effective_capital: total buying power
    """
    effective_capital = investment_amount * leverage
    position_size = effective_capital / current_price

    return {
        "position_size": position_size,
        "entry_price": current_price,
        "effective_capital": effective_capital,
        "initial_capital": investment_amount,
    }


def calculate_stop_loss(
    entry_price: float,
    stop_loss_percent: float
) -> float:
    """
    Calculate stop loss price.
    
    Stop loss price = entry_price * (1 - stop_loss_percent / 100)
    
    Returns the price at which to stop loss.
    """
    stop_loss_price = entry_price * (1 - stop_loss_percent / 100)
    return stop_loss_price


def calculate_take_profit(
    entry_price: float,
    profit_percent: float = 10.0
) -> float:
    """
    Calculate take profit price based on desired profit percentage.
    
    Formula:
      Take Profit = Entry Price × (1 + Profit % / 100)
    
    Example with 10% target profit:
      TP = $50,000 × (1 + 10/100)
      TP = $50,000 × 1.10
      TP = $55,000
    
    With x10 leverage, 10% price move = 100% return on capital
    
    Args:
        entry_price: The entry price (current crypto value)
        profit_percent: Target profit percentage (default 10% with x10 leverage)
    
    Returns the price at which to take profit.
    """
    take_profit_price = entry_price * (1 + profit_percent / 100)
    return take_profit_price


def calculate_risk_reward_ratio(
    entry_price: float,
    stop_loss_price: float,
    take_profit_price: float
) -> float:
    """Calculate the risk/reward ratio."""
    risk = entry_price - stop_loss_price
    reward = take_profit_price - entry_price
    
    if risk <= 0:
        return 0
    
    return reward / risk


def display_results(
    current_price: float,
    investment_amount: float,
    stop_loss_percent: float,
    profit_target_percent: float,
    position_info: dict[str, float],
    stop_loss_price: float,
    take_profit_price: float,
) -> None:
    """Display calculated results with formulas and clear output formatting."""
    risk_reward = calculate_risk_reward_ratio(
        position_info["entry_price"],
        stop_loss_price,
        take_profit_price
    )

    print("\n" + "=" * 70)
    print("📈 CALCULATION RESULTS")
    print("=" * 70)

    # Show input values
    print("\n� YOUR INPUTS:")
    print(f"  Current Price (Entry):        ${position_info['entry_price']:,.2f}")
    print(f"  Investment Amount:            ${position_info['initial_capital']:,.2f}")
    print(f"  Stop Loss Tolerance:          {stop_loss_percent:.2f}%")
    print(f"  Target Profit Goal:           {profit_target_percent:.2f}%")
    print(f"  Leverage:                     x10")

    print("\n💼 POSITION DETAILS:")
    print(f"  Position Size (Crypto):       {position_info['position_size']:.8f} BTC/ETH")
    print(f"  Effective Capital:            ${position_info['effective_capital']:,.2f}")

    print("\n" + "-" * 70)
    print("🔢 CALCULATION FORMULAS:")
    print("-" * 70)

    # Stop Loss Calculation
    print(f"\n🛑 STOP LOSS PRICE:")
    print(f"  Formula: Entry Price × (1 - Stop Loss % / 100)")
    print(f"  Formula: ${position_info['entry_price']:,.2f} × (1 - {stop_loss_percent}/100)")
    print(f"  Formula: ${position_info['entry_price']:,.2f} × {1 - stop_loss_percent/100:.4f}")
    print(f"  ➜ Result: ${stop_loss_price:,.2f}")

    # Take Profit Calculation
    print(f"\n📈 TAKE PROFIT PRICE:")
    print(f"  Formula: Entry Price × (1 + Target Profit % / 100)")
    print(f"  Formula: ${position_info['entry_price']:,.2f} × (1 + {profit_target_percent}/100)")
    print(f"  Formula: ${position_info['entry_price']:,.2f} × {1 + profit_target_percent/100:.4f}")
    print(f"  ➜ Result: ${take_profit_price:,.2f}")

    print("\n" + "=" * 70)
    print("🎯 PRICE TARGETS:")
    print("=" * 70)
    print(f"  Entry Price:                  ${position_info['entry_price']:,.2f}")
    print(f"  Stop Loss Price:              ${stop_loss_price:,.2f}")
    print(f"  Take Profit Price:            ${take_profit_price:,.2f}")

    print("\n" + "=" * 70)
    print("📊 RISK/REWARD ANALYSIS:")
    print("=" * 70)

    loss_on_stop = position_info['initial_capital'] * (stop_loss_percent / 100)
    profit_on_tp = position_info['initial_capital'] * (profit_target_percent / 100)

    print(f"\n💸 POTENTIAL LOSS (at stop loss):")
    print(f"  Formula: Investment × (Stop Loss % / 100)")
    print(f"  Formula: ${position_info['initial_capital']:,.2f} × ({stop_loss_percent}/100)")
    print(f"  ➜ Result: ${loss_on_stop:,.2f}")

    print(f"\n💰 POTENTIAL PROFIT (at take profit):")
    print(f"  Formula: Investment × (Target Profit % / 100)")
    print(f"  Formula: ${position_info['initial_capital']:,.2f} × ({profit_target_percent}/100)")
    print(f"  ➜ Result: ${profit_on_tp:,.2f}")

    print(f"\n⚖️  RISK/REWARD RATIO:")
    print(f"  Formula: Reward / Risk")
    print(f"  Formula: {profit_on_tp:,.2f} / {loss_on_stop:,.2f}")
    print(f"  ➜ Result: 1:{risk_reward:.2f}")

    print("\n" + "=" * 70 + "\n")


def main(argv: list[str] | None = None) -> None:
    """Main interactive entry point."""
    try:
        current_price, investment_amount, stop_loss_percent, profit_target_percent, asset_name, symbol = get_user_inputs()

        # Calculate position
        position_info = calculate_position(current_price, investment_amount, leverage=10)

        # Calculate price targets
        stop_loss_price = calculate_stop_loss(position_info["entry_price"], stop_loss_percent)
        take_profit_price = calculate_take_profit(position_info["entry_price"], profit_target_percent)

        # Display results with formulas
        display_results(
            current_price,
            investment_amount,
            stop_loss_percent,
            profit_target_percent,
            position_info,
            stop_loss_price,
            take_profit_price,
            asset_name,
            symbol,
        )

    except KeyboardInterrupt:
        print("\n\n👋 Calculation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
