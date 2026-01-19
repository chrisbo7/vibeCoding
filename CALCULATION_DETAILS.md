# Crypto Leverage Calculator - Calculation Summary

## Complete Walkthrough with Your Example

Here's exactly how the script calculates stop loss and take profit when you enter values:

### Your Inputs

```
Current Crypto Value:    $50,000
Investment Amount:       $25,000
Stop Loss Percentage:    5%
Target Profit Percentage: 10%
Leverage:               x10
```

---

## Step 1: Calculate Position Size

**What it answers**: "How much crypto can I buy with x10 leverage?"

**Formula:**
```
Position Size = (Investment Amount × Leverage) / Current Price
```

**Your Calculation:**
```
Position Size = ($25,000 × 10) / $50,000
Position Size = $250,000 / $50,000
Position Size = 5 BTC/ETH
```

**What this means:**
- You control **5 BTC/ETH** with only **$25,000** investment
- Your effective buying power is **$250,000**
- But your maximum loss is still limited to your **$25,000** investment (if stop loss is hit)

---

## Step 2: Calculate Stop Loss Price

**What it answers**: "At what exact price should I sell to limit my loss to 5%?"

**Formula:**
```
Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)
```

**Breaking it down:**

| Step | Calculation | Result |
|------|-------------|--------|
| Entry Price | $50,000 | $50,000 |
| Stop Loss % | 5 | 5% |
| Convert % to decimal | 1 - 5/100 | 0.95 |
| Multiply | $50,000 × 0.95 | **$47,500** |

**Your Calculation:**
```
Stop Loss Price = $50,000 × (1 - 5/100)
Stop Loss Price = $50,000 × (1 - 0.05)
Stop Loss Price = $50,000 × 0.95
Stop Loss Price = $47,500
```

**What this means:**
- If price drops to **$47,500**, you automatically sell
- This is a **$2,500 drop** from entry ($50,000 - $47,500)
- At $50,000 entry price, $2,500 = **5% loss** on your position
- On your $25,000 investment, 5% = **$1,250 loss**

**Visual:**
```
Entry: $50,000 ────────────┐
                            │ Stop Loss
                            │ Zone
Stop:  $47,500 ────────────┘ (Price drops 5%)
```

---

## Step 3: Calculate Take Profit Price

**What it answers**: "At what exact price should I sell to lock in my 10% profit?"

**Formula:**
```
Take Profit Price = Entry Price × (1 + Target Profit % / 100)
```

**Breaking it down:**

| Step | Calculation | Result |
|------|-------------|--------|
| Entry Price | $50,000 | $50,000 |
| Profit Target % | 10 | 10% |
| Convert % to decimal | 1 + 10/100 | 1.10 |
| Multiply | $50,000 × 1.10 | **$55,000** |

**Your Calculation:**
```
Take Profit Price = $50,000 × (1 + 10/100)
Take Profit Price = $50,000 × (1 + 0.10)
Take Profit Price = $50,000 × 1.10
Take Profit Price = $55,000
```

**What this means:**
- If price rises to **$55,000**, you automatically sell
- This is a **$5,000 rise** from entry ($55,000 - $50,000)
- At $50,000 entry price, $5,000 = **10% gain** on your position
- On your $25,000 investment, 10% = **$2,500 profit**

**Visual:**
```
Take:  $55,000 ────────────┐
                            │ Take Profit
                            │ Zone
Entry: $50,000 ────────────┘ (Price rises 10%)
```

---

## Step 4: Calculate Potential Loss

**What it answers**: "How much money do I actually lose if stop loss is hit?"

**Formula:**
```
Potential Loss = Investment Amount × (Stop Loss % / 100)
```

**Your Calculation:**
```
Potential Loss = $25,000 × (5 / 100)
Potential Loss = $25,000 × 0.05
Potential Loss = $1,250
```

**What this means:**
- Maximum loss if stop hit: **$1,250**
- Your new balance if stopped out: $25,000 - $1,250 = **$23,750**

---

## Step 5: Calculate Potential Profit

**What it answers**: "How much money do I actually make if take profit is hit?"

**Formula:**
```
Potential Profit = Investment Amount × (Target Profit % / 100)
```

**Your Calculation:**
```
Potential Profit = $25,000 × (10 / 100)
Potential Profit = $25,000 × 0.10
Potential Profit = $2,500
```

**What this means:**
- Maximum profit if TP hit: **$2,500**
- Your new balance if take profit: $25,000 + $2,500 = **$27,500**

---

## Step 6: Calculate Risk/Reward Ratio

**What it answers**: "For every $1 I risk, how much can I make?"

**Formula:**
```
Risk/Reward Ratio = Potential Profit / Potential Loss
```

**Your Calculation:**
```
Risk/Reward Ratio = $2,500 / $1,250
Risk/Reward Ratio = 2.0
```

**What this means:**
- Ratio is **1:2** (or just "2")
- For every **$1 you risk**, you stand to make **$2**
- This is a **good trade** (2:1 ratio is ideal)

**Trade Quality Scale:**
- ❌ < 1:1 = Poor (losing bet)
- ⚠️ 1:1 = Neutral (break-even)
- ✓ 1:1.5 = Good (make 1.5x your risk)
- ✓✓ 1:2 = Very good (make 2x your risk)
- ✓✓✓ 1:3+ = Excellent (make 3x+ your risk)

---

## Complete Trade Summary

```
═══════════════════════════════════════════════════════════
                     TRADE PLAN
═══════════════════════════════════════════════════════════

YOUR INPUTS:
  Entry Price:        $50,000
  Investment:         $25,000
  Stop Loss %:        5%
  Profit Target %:    10%
  Leverage:           x10

CALCULATED VALUES:
  Position Size:      5.00000000 BTC/ETH
  Effective Capital:  $250,000

PRICE TARGETS:
  Stop Loss:          $47,500  (lose $1,250 if hit)
  Take Profit:        $55,000  (gain $2,500 if hit)

RISK ANALYSIS:
  Max Risk:           $1,250
  Max Reward:         $2,500
  Risk/Reward:        1:2.00  ✓ Good ratio!

TRADE OUTCOMES:

  Scenario 1: Price → $55,000
    You sell at take profit
    Profit: +$2,500
    New balance: $27,500

  Scenario 2: Price → $47,500
    You sell at stop loss
    Loss: -$1,250
    New balance: $23,750

  Scenario 3: Price stays between $47,500-$55,000
    Trade is still open
    You're waiting for price to hit target

═══════════════════════════════════════════════════════════
```

---

## The Real-Time Prompt Flow

When you run `python crypto_leverage.py`, here's what happens:

```
📊 Enter current crypto value (e.g., 45000): 50000
💰 Enter investment amount in USD (e.g., 10000): 25000
🛑 Enter stop loss percentage (e.g., 5): 5
📈 Enter target profit percentage (e.g., 10): 10

[Script calculates everything...]

OUTPUT SHOWS:
  ✓ Position size calculation
  ✓ Stop loss formula and result
  ✓ Take profit formula and result
  ✓ Risk/reward ratio
  ✓ Potential profit and loss amounts
```

---

## Key Formulas Reference

| What | Formula | Example |
|------|---------|---------|
| **Position Size** | (Investment × Leverage) / Price | ($25K × 10) / $50K = 5 BTC |
| **Stop Loss** | Entry × (1 - SL% / 100) | $50K × 0.95 = $47,500 |
| **Take Profit** | Entry × (1 + TP% / 100) | $50K × 1.10 = $55,000 |
| **Max Loss** | Investment × (SL% / 100) | $25K × 0.05 = $1,250 |
| **Max Profit** | Investment × (TP% / 100) | $25K × 0.10 = $2,500 |
| **Risk/Reward** | Max Profit / Max Loss | $2,500 / $1,250 = 2.0 |

---

## Important Notes

1. **Stop Loss = Downward Movement**: 5% stop = price drops 5% from entry
2. **Take Profit = Upward Movement**: 10% TP = price rises 10% from entry
3. **Loss = On Investment**: 5% loss on $25K = $1,250 (NOT $1,250,000!)
4. **With Leverage**: You control 10x your investment, but risk is real
5. **No Guarantee**: Actual prices may be different due to slippage/gaps

---

## Running the Script

```bash
# Interactive mode (prompts for all values)
python crypto_leverage.py

# View demo calculation
python demo_crypto_leverage.py

# Run tests
python test_crypto_leverage.py
```

Now you see exactly how the calculations work! 🎯
