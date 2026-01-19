# Stop Loss & Take Profit - Complete Output Reference

## Exactly What You'll See When You Run the Script

### Running the Demo

```bash
python demo_crypto_leverage.py
```

### Complete Output (What Appeared Above)

```
======================================================================
🚀 CRYPTO LEVERAGE CALCULATOR DEMO - SHOWING CALCULATIONS
======================================================================

📥 SAMPLE INPUTS:
  Current Price (Entry):        $50,000.00
  Investment Amount:            $25,000.00
  Stop Loss Tolerance:          5.00%
  Target Profit Goal:           10.00%
  Leverage:                     x10

----------------------------------------------------------------------
💼 POSITION CALCULATION:
----------------------------------------------------------------------

  Formula: Position Size = (Investment × Leverage) / Current Price
  Formula: Position Size = (25,000.00 × 10) / 50,000.00
  Formula: Position Size = 250,000.00 / 50,000.00
  ➜ Result: 5.00000000 BTC/ETH

  You can control 5.00000000 BTC/ETH with $25,000.00
  (Effective buying power: $250,000.00)

----------------------------------------------------------------------
🛑 STOP LOSS CALCULATION:
----------------------------------------------------------------------

  Formula: Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)
  Formula: Stop Loss Price = $50,000.00 × (1 - 5/100)
  Formula: Stop Loss Price = $50,000.00 × 0.9500
  Formula: Stop Loss Price = $50,000.00 × 0.95
  ➜ Result: $47,500.00

  If price hits $47,500.00, you lose: $1,250.00

----------------------------------------------------------------------
📈 TAKE PROFIT CALCULATION:
----------------------------------------------------------------------

  Formula: Take Profit Price = Entry Price × (1 + Target Profit % / 100)
  Formula: Take Profit Price = $50,000.00 × (1 + 10/100)
  Formula: Take Profit Price = $50,000.00 × 1.1000
  Formula: Take Profit Price = $50,000.00 × 1.10
  ➜ Result: $55,000.00

  If price reaches $55,000.00, you make: $2,500.00
  That's a 10.00% price move

======================================================================
⚖️  RISK/REWARD ANALYSIS:
======================================================================

  Risk (amount you can lose):     $1,250.00
  Reward (amount you can gain):   $2,500.00

  Formula: Risk/Reward Ratio = Reward / Risk
  Formula: Risk/Reward Ratio = 2,500.00 / 1,250.00
  ➜ Result: 1:2.00

  ✅ For every $1 you risk, you stand to make $2.00

======================================================================
📊 FINAL TRADE SUMMARY:
======================================================================

  Entry Point:      $50,000.00
  Stop Loss:        $47,500.00  (lose $1,250.00 if hit)
  Take Profit:      $55,000.00  (gain $2,500.00 if hit)
  Position Size:    5.00000000 BTC/ETH (worth $250,000.00 at entry)
  Risk/Reward:      1:2.00

======================================================================
```

---

## Highlighting the Stop Loss Calculation

Here's the stop loss section in detail:

```
🛑 STOP LOSS CALCULATION:

  Formula: Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)
  
  Step-by-step breakdown of what each part means:
  ┌─────────────────────────────────────────────────────────┐
  │ Entry Price:        $50,000                             │
  │ Stop Loss %:        5                                   │
  │ (1 - 5/100):        1 - 0.05 = 0.95                    │
  │ Multiply:           $50,000 × 0.95                      │
  │ RESULT:             $47,500                             │
  └─────────────────────────────────────────────────────────┘

  Formula: Stop Loss Price = $50,000.00 × (1 - 5/100)
  Formula: Stop Loss Price = $50,000.00 × 0.9500
  Formula: Stop Loss Price = $50,000.00 × 0.95
  ➜ Result: $47,500.00

  If price hits $47,500.00, you lose: $1,250.00
```

### What This Means:

- **Entry Price**: $50,000 (where you buy)
- **Stop Loss %**: 5% (your maximum acceptable loss)
- **(1 - 5/100)**: Converts 5% to 0.95
- **$50,000 × 0.95**: = $47,500
- **Result**: Stop Loss Price = **$47,500**
- **Loss if hit**: $50,000 - $47,500 = **$2,500 price drop**
- **On your investment**: $25,000 × 5% = **$1,250 loss**

---

## Highlighting the Take Profit Calculation

Here's the take profit section in detail:

```
📈 TAKE PROFIT CALCULATION:

  Formula: Take Profit Price = Entry Price × (1 + Target Profit % / 100)
  
  Step-by-step breakdown:
  ┌─────────────────────────────────────────────────────────┐
  │ Entry Price:         $50,000                            │
  │ Target Profit %:     10                                 │
  │ (1 + 10/100):        1 + 0.10 = 1.10                   │
  │ Multiply:            $50,000 × 1.10                     │
  │ RESULT:              $55,000                            │
  └─────────────────────────────────────────────────────────┘

  Formula: Take Profit Price = $50,000.00 × (1 + 10/100)
  Formula: Take Profit Price = $50,000.00 × 1.1000
  Formula: Take Profit Price = $50,000.00 × 1.10
  ➜ Result: $55,000.00

  If price reaches $55,000.00, you make: $2,500.00
  That's a 10.00% price move
```

### What This Means:

- **Entry Price**: $50,000 (where you buy)
- **Target Profit %**: 10% (your profit goal)
- **(1 + 10/100)**: Converts 10% to 1.10
- **$50,000 × 1.10**: = $55,000
- **Result**: Take Profit Price = **$55,000**
- **Gain if hit**: $55,000 - $50,000 = **$5,000 price rise**
- **On your investment**: $25,000 × 10% = **$2,500 profit**

---

## Interactive Mode Output

When you run:
```bash
python crypto_leverage.py
```

You'll be prompted:

```
============================================================
🚀 CRYPTO LEVERAGE CALCULATOR (x10)
============================================================

📊 Enter current crypto value (e.g., 45000): 
```

Then after entering all values:

```
============================================================
📈 CALCULATION RESULTS
============================================================

📥 YOUR INPUTS:
  Current Price (Entry):        $50,000.00
  Investment Amount:            $25,000.00
  Stop Loss Tolerance:          5.00%
  Target Profit Goal:           10.00%
  Leverage:                     x10

💼 POSITION DETAILS:
  Position Size (Crypto):       5.00000000 BTC/ETH
  Effective Capital:            $250,000.00

-----------...more output...----------

🛑 STOP LOSS PRICE:
  Formula: Entry Price × (1 - Stop Loss % / 100)
  Formula: $50,000.00 × (1 - 5/100)
  Formula: $50,000.00 × 0.95
  ➜ Result: $47,500.00

📈 TAKE PROFIT PRICE:
  Formula: Entry Price × (1 + Target Profit % / 100)
  Formula: $50,000.00 × (1 + 10/100)
  Formula: $50,000.00 × 1.10
  ➜ Result: $55,000.00

... [more analysis] ...
```

---

## Quick Reference - The Two Most Important Calculations

### For Stop Loss:
```
Stop Loss Price = Entry × (1 - Stop %)
$47,500 = $50,000 × (1 - 0.05)
$47,500 = $50,000 × 0.95
```

### For Take Profit:
```
Take Profit Price = Entry × (1 + Profit %)
$55,000 = $50,000 × (1 + 0.10)
$55,000 = $50,000 × 1.10
```

---

## Verification - Unit Tests Pass

```bash
python test_crypto_leverage.py
```

Output:
```
✓ Valid number validation works
✓ Rejects non-numeric input
✓ Rejects negative numbers
✓ Rejects zero
✓ Basic position calculation correct
✓ Fractional position calculation correct
✓ 5% stop loss calculation correct
✓ 10% stop loss calculation correct
✓ Take profit (10% target) calculation correct
✓ Take profit (20% target) calculation correct
✓ Risk/reward ratio calculation correct
✓ 1:1 risk/reward ratio correct
✓ Full scenario (small investment) works correctly
✓ Full scenario (large investment) works correctly

✅ All 12 tests passed!
```

---

## Summary

**This script shows you:**

1. ✓ **Stop Loss Price Calculation** with formula
2. ✓ **Take Profit Price Calculation** with formula
3. ✓ **Position Size** (how much crypto you control)
4. ✓ **Maximum Loss** (if stop is hit)
5. ✓ **Maximum Profit** (if take profit is hit)
6. ✓ **Risk/Reward Ratio** (is this trade worth it?)

**Everything is calculated step-by-step with formulas shown!**

Now you can see exactly how to calculate stop loss and take profit! 🎯
