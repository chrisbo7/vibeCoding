# Crypto Leverage Calculator (x10)

A Python CLI tool that calculates crypto trading positions with x10 leverage. Perfect for planning your trades with accurate stop loss and take profit levels.

## Features

- 📊 **User-friendly CLI** that guides you through the calculation
- 💰 **x10 Leverage calculations** for maximum trading potential
- 🎯 **Accurate price targets**:
  - Entry price
  - Stop loss price (based on your chosen percentage)
  - Take profit price (10% move = 100% return on capital with x10 leverage)
- 📈 **Risk/Reward ratio** analysis
- ✓ **Fully tested** with 12 comprehensive unit tests
- ✅ **Input validation** with error handling

## How It Works

The calculator uses x10 leverage to amplify your position size:

```
With x10 Leverage:
  Effective Capital = Investment Amount × 10
  Position Size = Effective Capital ÷ Current Price
  
Stop Loss Price = Entry Price × (1 - Stop Loss %)
Take Profit Price = Entry Price × 1.10  (10% move)
```

### Example

- **Current Price**: $45,000
- **Investment**: $10,000
- **Stop Loss**: 5%

**Results:**
- **Effective Capital**: $100,000 (10,000 × 10)
- **Position Size**: 2.222 BTC/ETH
- **Entry Price**: $45,000
- **Stop Loss**: $42,750 (5% below entry)
- **Take Profit**: $49,500 (10% above entry)
- **Max Loss**: $500 (5% of $10,000)
- **Max Profit**: $1,000+ (depends on leverage at TP)

## Usage

### Run the Interactive Calculator

```bash
python crypto_leverage.py
```

You'll be prompted to enter:
1. **Current crypto value** - The price you want to buy at (e.g., 45000)
2. **Investment amount** - How much to invest in USD (e.g., 10000)
3. **Stop loss percentage** - Your max loss tolerance (e.g., 5)

The script will then display:
- Position size (amount of crypto you can control)
- Entry, stop loss, and take profit prices
- Potential loss and profit amounts
- Risk/reward ratio

### Example Session

```
============================================================
🚀 CRYPTO LEVERAGE CALCULATOR (x10)
============================================================

📊 Enter current crypto value (e.g., 45000): 50000
💰 Enter investment amount in USD (e.g., 10000): 25000
🛑 Enter stop loss percentage (e.g., 5): 3

============================================================
📈 CALCULATION RESULTS
============================================================

💼 POSITION INFO:
  Current Price (Entry):        $50,000.00
  Investment Amount:            $25,000.00
  Leverage:                     x10
  Effective Capital:            $250,000.00
  Position Size (Crypto):       5.00000000 BTC/ETH

🎯 PRICE TARGETS:
  Entry Price:                  $50,000.00
  Stop Loss Price:              $48,500.00
  Take Profit Price:            $55,000.00

📊 RISK ANALYSIS:
  Stop Loss Percentage:         3.00%
  Potential Loss (at stop):     $750.00
  Potential Profit (at TP):     $1,250.00+
  Risk/Reward Ratio:            1:1.67
```

## Files Included

- `crypto_leverage.py` — Main calculator script with CLI
- `test_crypto_leverage.py` — 12 comprehensive unit tests
- `README.md` — This documentation

## Testing

Run all unit tests to verify the calculations:

```bash
python test_crypto_leverage.py
```

### Test Coverage (12 tests)

- ✓ Input validation (valid/invalid numbers, edge cases)
- ✓ Position size calculations
- ✓ Stop loss price calculations (multiple percentages)
- ✓ Take profit calculations (multiple leverage levels)
- ✓ Risk/reward ratio analysis
- ✓ Full trading scenarios (small & large investments)

All tests passing ✅

## Important Notes ⚠️

**Disclaimer**: This is a calculation tool for planning purposes only.

1. **Real Trading Risks**: Leverage trading is high-risk. Always use proper risk management.
2. **Slippage**: Real execution prices may differ from calculated prices.
3. **Liquidation**: With leverage, if price moves against you beyond stop loss, you can be liquidated.
4. **Exchange Fees**: This calculator does not account for trading fees or maker/taker fees.
5. **Volatility**: Crypto is extremely volatile. Past performance ≠ future results.

## Common Stop Loss Percentages

- **Conservative**: 3-5% (less risk, smaller gains)
- **Moderate**: 5-10% (balanced risk/reward)
- **Aggressive**: 10-20% (higher risk for larger potential gains)

## How to Run

### On Windows (cmd)

```cmd
cd "c:\Users\cmpotsiar\OneDrive - OTE\Desktop\IT ARCHITECTURE PROJECTS\CODE test"
python crypto_leverage.py
```

Or with virtualenv:

```cmd
C:\Users\cmpotsiar\.virtualenvs\YOUR_DJANGO_PROJECT-2y_e-DLS\Scripts\python.exe crypto_leverage.py
```

### On macOS/Linux

```bash
python3 crypto_leverage.py
```

## Future Enhancements

- [ ] Support for multiple leverage levels (5x, 20x, 100x)
- [ ] Save/load trading plans
- [ ] Integration with real-time price APIs
- [ ] Portfolio tracking across multiple trades
- [ ] Tax reporting for realized gains
- [ ] Trading history log
- [ ] Automated alerts at price levels

## Questions?

If you encounter any issues or want to add features, feel free to modify the script!

---

**Happy Trading! 🚀📈**
