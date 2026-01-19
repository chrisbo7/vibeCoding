# Crypto Leverage Calculator - Full Documentation

## Overview

This is a Python CLI tool that calculates crypto trading positions with **x10 leverage**. It shows you exactly what prices to use for **stop loss** and **take profit**, with detailed formulas explained step-by-step.

## The Calculations Explained

### 1. Position Size Calculation

**What it does**: Determines how much crypto you can buy with x10 leverage.

**Formula:**
```
Position Size = (Investment Amount × Leverage) / Current Price
```

**Example:**
```
Investment:  $25,000
Leverage:    x10
Price:       $50,000

Position Size = (25,000 × 10) / 50,000
Position Size = 250,000 / 50,000
Position Size = 5 BTC/ETH
```

**What this means:**
- With x10 leverage, you can control **5 BTC** with only **$25,000** investment
- Your effective buying power is **$250,000** ($25,000 × 10)

---

### 2. Stop Loss Price Calculation

**What it does**: Calculates the exact price where you should exit if the trade goes against you.

**Formula:**
```
Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)
```

**Step-by-step calculation:**
```
Entry Price:         $50,000
Stop Loss %:         5%

Step 1: Convert percentage to decimal
        1 - 5/100 = 1 - 0.05 = 0.95

Step 2: Multiply entry price by the decimal
        $50,000 × 0.95 = $47,500

Stop Loss Price = $47,500
```

**What this means:**
- If the price drops to **$47,500**, you automatically exit
- A 5% drop in price = **$1,250 loss** on your $25,000 investment
- You lose 5% of your investment capital (NOT 5% of position value due to leverage)

**More examples:**

| Entry Price | Stop Loss % | Calculation | Stop Loss Price |
|-------------|------------|-------------|-----------------|
| $50,000 | 3% | $50,000 × 0.97 | $48,500 |
| $50,000 | 5% | $50,000 × 0.95 | $47,500 |
| $50,000 | 10% | $50,000 × 0.90 | $45,000 |
| $45,000 | 5% | $45,000 × 0.95 | $42,750 |

---

### 3. Take Profit Price Calculation

**What it does**: Calculates the exact price where you should sell to lock in your target profit.

**Formula:**
```
Take Profit Price = Entry Price × (1 + Target Profit % / 100)
```

**Step-by-step calculation:**
```
Entry Price:         $50,000
Target Profit %:     10%

Step 1: Convert percentage to decimal
        1 + 10/100 = 1 + 0.10 = 1.10

Step 2: Multiply entry price by the decimal
        $50,000 × 1.10 = $55,000

Take Profit Price = $55,000
```

**What this means:**
- If the price rises to **$55,000**, you automatically exit
- A 10% rise in price = **$2,500 profit** on your $25,000 investment
- You make 10% profit on your investment (NOT 10% of position value)

**More examples:**

| Entry Price | Profit Target % | Calculation | Take Profit Price |
|-------------|-----------------|-------------|-------------------|
| $50,000 | 5% | $50,000 × 1.05 | $52,500 |
| $50,000 | 10% | $50,000 × 1.10 | $55,000 |
| $50,000 | 15% | $50,000 × 1.15 | $57,500 |
| $45,000 | 10% | $45,000 × 1.10 | $49,500 |

---

### 4. Risk/Reward Ratio Calculation

**What it does**: Shows the relationship between your potential loss and potential gain.

**Formula:**
```
Risk/Reward Ratio = Potential Profit / Potential Loss
```

**Step-by-step calculation:**
```
Entry Price:      $50,000
Stop Loss Price:  $47,500
Take Profit:      $55,000
Investment:       $25,000

Potential Loss = Investment × (Stop Loss % / 100)
               = $25,000 × (5 / 100)
               = $25,000 × 0.05
               = $1,250

Potential Profit = Investment × (Profit Target % / 100)
                 = $25,000 × (10 / 100)
                 = $25,000 × 0.10
                 = $2,500

Risk/Reward Ratio = $2,500 / $1,250 = 2.00
```

**What this means:**
- For every **$1 you risk**, you stand to make **$2** in profit
- A ratio of **1:2** is considered good (you make 2x your risk)
- A ratio of **1:1** means equal risk and reward
- A ratio < 1:1 means you're risking more than you can make

---

## Example Trade Walkthrough

### Scenario: Bitcoin at $50,000

**Your Decision:**
- I'll invest **$25,000**
- I'll risk a **5% stop loss** ($1,250 max loss)
- I want a **10% profit target** ($2,500 target gain)

**The Calculation:**

```
POSITION SIZE:
  You control: (25,000 × 10) / 50,000 = 5 BTC
  Effective capital: $250,000

STOP LOSS:
  $50,000 × (1 - 5/100) = $50,000 × 0.95 = $47,500
  If price drops to $47,500: SELL (lose $1,250)

TAKE PROFIT:
  $50,000 × (1 + 10/100) = $50,000 × 1.10 = $55,000
  If price rises to $55,000: SELL (gain $2,500)

RISK/REWARD:
  $2,500 / $1,250 = 1:2.00
  For every $1 at risk, you make $2
```

**Three Possible Outcomes:**

1. **Price goes to $55,000** (best case)
   - You sell at take profit
   - Profit: **+$2,500** (10% return)
   - New balance: **$27,500**

2. **Price goes to $47,500** (worst case)
   - You sell at stop loss
   - Loss: **-$1,250** (5% loss)
   - New balance: **$23,750**

3. **Price stays between $47,500 - $55,000** (still open)
   - Trade is still open
   - Position is still at risk
   - Waiting for price to hit one of your targets

---

## Key Takeaways

### Stop Loss Formula
```
Stop Loss = Entry × (1 - Stop % / 100)
```
- Moves DOWN from entry price
- Always less than entry price
- Represents your maximum acceptable loss

### Take Profit Formula
```
Take Profit = Entry × (1 + Profit % / 100)
```
- Moves UP from entry price
- Always greater than entry price
- Represents your target profit goal

### Risk/Reward Formula
```
Ratio = Potential Profit / Potential Loss
```
- Should be ≥ 1.5 (you gain 1.5x your risk minimum)
- The higher, the better for your trading plan
- Helps decide if a trade is worth taking

---

## Common Stop Loss and Profit Target Strategies

| Strategy | Stop Loss | Profit Target | Risk/Reward | Best For |
|----------|-----------|---------------|-------------|----------|
| Ultra Safe | 2% | 5% | 1:2.5 | Scalping |
| Conservative | 3% | 8% | 1:2.7 | Swing trading |
| Balanced | 5% | 10% | 1:2.0 | General trading |
| Moderate Risk | 7% | 15% | 1:2.1 | Trend following |
| Aggressive | 10% | 20% | 1:2.0 | Volatile assets |

---

## How to Use the Calculator

### Interactive Mode

```bash
python crypto_leverage.py
```

You'll be prompted to enter:
1. **Current crypto value** - Price now
2. **Investment amount** - How much you'll invest
3. **Stop loss percentage** - Max loss tolerance
4. **Target profit percentage** - Profit goal

The script displays all calculations with formulas shown!

### Demo Mode (see example output)

```bash
python demo_crypto_leverage.py
```

Shows a complete example walkthrough with all calculations.

---

## Important Risk Warnings ⚠️

1. **Leverage Magnifies Risk**: x10 leverage means a small price move against you can wipe out your entire investment
2. **Liquidation Risk**: Many exchanges liquidate positions if margin requirements aren't met
3. **No Guarantee**: Stop losses may not execute at exact price during flash crashes
4. **Market Gaps**: Large price gaps can skip past your stop loss
5. **Slippage**: Actual execution price may differ from calculated price
6. **Emotional Trading**: Always stick to your plan (don't move stops to avoid losses!)

---

## Pro Tips

✅ **DO:**
- Always use a stop loss
- Calculate your risk before entering
- Use the risk/reward ratio to filter trades
- Scale in/out gradually
- Keep a trading journal

❌ **DON'T:**
- Risk more than 2% per trade
- Move your stop loss against you
- FOMO into trades without a plan
- Trade without leverage experience
- Ignore the risk/reward ratio

---

## Questions & Answers

**Q: Why does stop loss go DOWN and take profit go UP?**
A: Stop loss is set BELOW entry to minimize loss if price falls. Take profit is set ABOVE entry to lock in gains if price rises.

**Q: What if I want a different stop loss percentage?**
A: The formula stays the same! Just enter your preferred percentage. Lower % = less risk but tighter stop. Higher % = more room but bigger potential loss.

**Q: Does the profit percentage have to be 10%?**
A: No! You can use any percentage. The script asks for YOUR target profit. Common targets: 5%, 10%, 15%, 20%.

**Q: What's a good risk/reward ratio?**
A: At least 1:1.5 (make 1.5x your risk). Ideally 1:2 or better (make 2x your risk or more).

**Q: Why is position size so large with leverage?**
A: x10 leverage multiplies your buying power by 10. With $25,000, you can control $250,000 worth of crypto (5 BTC at $50,000). But the risk is REAL - you can lose all $25,000.

---

Enjoy calculating your trades! 🚀📈
