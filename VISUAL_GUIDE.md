# Stop Loss & Take Profit Calculation - Visual Summary

## The Three Key Prices

```
                         📈 UPSIDE (PROFIT)
                              ↑
                              |
                         $55,000  ← TAKE PROFIT
                              |  Target: +10% from entry
                              |  Profit: +$2,500
                              |
                         $50,000  ← ENTRY PRICE
                         (Current)
                              |
                         $47,500  ← STOP LOSS
                              |  Risk: -5% from entry
                              |  Loss: -$1,250
                              ↓
                         📉 DOWNSIDE (RISK)
```

---

## Stop Loss Calculation in Detail

### What is Stop Loss?
- A **protective exit** if the trade goes against you
- Set **below** the entry price
- Limits your **maximum loss**

### Formula
```
Stop Loss = Entry Price × (1 - Stop Loss % / 100)
```

### Example With Numbers

**Your Setup:**
```
Entry Price:      $50,000
Stop Loss %:      5%
```

**Step 1: Convert percentage to decimal**
```
1 - 5/100 = 1 - 0.05 = 0.95
```

**Step 2: Multiply entry price by decimal**
```
$50,000 × 0.95 = $47,500
```

**Result:**
```
Stop Loss Price = $47,500
```

### What It Means

| When Price | Action | Your Result |
|-----------|--------|-------------|
| > $47,500 | Still holding | Trade open |
| = $47,500 | SELL (auto) | Lose $1,250 |
| < $47,500 | Already sold | Loss locked |

---

## Take Profit Calculation in Detail

### What is Take Profit?
- A **profit-taking exit** if the trade goes in your favor
- Set **above** the entry price
- Locks in your **target profit**

### Formula
```
Take Profit = Entry Price × (1 + Target Profit % / 100)
```

### Example With Numbers

**Your Setup:**
```
Entry Price:          $50,000
Target Profit %:      10%
```

**Step 1: Convert percentage to decimal**
```
1 + 10/100 = 1 + 0.10 = 1.10
```

**Step 2: Multiply entry price by decimal**
```
$50,000 × 1.10 = $55,000
```

**Result:**
```
Take Profit Price = $55,000
```

### What It Means

| When Price | Action | Your Result |
|-----------|--------|-------------|
| < $55,000 | Still holding | Trade open |
| = $55,000 | SELL (auto) | Gain $2,500 |
| > $55,000 | Already sold | Profit locked |

---

## Side-By-Side Comparison

```
STOP LOSS (DOWNSIDE PROTECTION)    VS    TAKE PROFIT (PROFIT TARGET)

Formula: Entry × (1 - %)           VS    Formula: Entry × (1 + %)
$50,000 × (1 - 0.05)               VS    $50,000 × (1 + 0.10)
$50,000 × 0.95                     VS    $50,000 × 1.10
= $47,500                          VS    = $55,000

Moves DOWN from entry              VS    Moves UP from entry
Below $50,000                      VS    Above $50,000
Limit loss to 5%                   VS    Target profit of 10%
Max loss: $1,250                   VS    Max profit: $2,500
```

---

## Real Trade Outcomes

```
SCENARIO 1: Price Goes DOWN to $47,500
┌─────────────────────────────────────┐
│ Entry:        $50,000               │
│ Current:      $47,500 ← STOP HIT!   │
│                                     │
│ Action: AUTOMATIC SELL              │
│ Loss: $1,250 (5% of $25,000)       │
│ New Balance: $25,000 - $1,250       │
│           = $23,750                 │
│                                     │
│ ❌ Trade closed with loss           │
└─────────────────────────────────────┘

SCENARIO 2: Price Goes UP to $55,000
┌─────────────────────────────────────┐
│ Entry:        $50,000               │
│ Current:      $55,000 ← PROFIT HIT! │
│                                     │
│ Action: AUTOMATIC SELL              │
│ Profit: $2,500 (10% of $25,000)    │
│ New Balance: $25,000 + $2,500       │
│           = $27,500                 │
│                                     │
│ ✅ Trade closed with profit         │
└─────────────────────────────────────┘

SCENARIO 3: Price Stays in Between
┌─────────────────────────────────────┐
│ Stop Loss:    $47,500               │
│ Entry:        $50,000               │
│ Current:      $52,000 ← HERE        │
│ Take Profit:  $55,000               │
│                                     │
│ Action: NONE (still open)           │
│ P&L: +$500 (unrealized)            │
│                                     │
│ ⏳ Waiting for price to move        │
│    to either target                 │
└─────────────────────────────────────┘
```

---

## The Math Breakdown

### How Stop Loss % Translates to Dollar Loss

```
Stop Loss % = 5%

On your INVESTMENT ($25,000):
Loss = $25,000 × 5% = $1,250

On your POSITION ($250,000 effective):
Loss = $250,000 × 0.5% = $1,250

(Note: With x10 leverage, 0.5% on position = 5% on investment)
```

### How Profit Target % Translates to Dollar Profit

```
Profit Target % = 10%

On your INVESTMENT ($25,000):
Profit = $25,000 × 10% = $2,500

On your POSITION ($250,000 effective):
Profit = $250,000 × 1% = $2,500

(Note: With x10 leverage, 1% on position = 10% on investment)
```

---

## Formula Cheat Sheet

### Quick Reference

```
┌─────────────────────────────────────────────────────┐
│ STOP LOSS = Entry × (1 - Stop % / 100)             │
│ Example: $50K × (1 - 5/100) = $47,500              │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ TAKE PROFIT = Entry × (1 + Profit % / 100)         │
│ Example: $50K × (1 + 10/100) = $55,000             │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ LOSS AMOUNT = Investment × (Stop % / 100)          │
│ Example: $25K × (5/100) = $1,250                   │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ PROFIT AMOUNT = Investment × (Profit % / 100)      │
│ Example: $25K × (10/100) = $2,500                  │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ RISK/REWARD = Profit Amount / Loss Amount          │
│ Example: $2,500 / $1,250 = 2.00 (or 1:2)           │
└─────────────────────────────────────────────────────┘
```

---

## Common Mistakes to Avoid

### ❌ WRONG: "5% stop means price drops to $47,500"
- **Why it's wrong**: You're calculating 5% of the position, not the entry price
- **Right way**: Entry × (1 - 0.05) = $50,000 × 0.95 = $47,500 ✓

### ❌ WRONG: "My loss is 5% of my position ($250,000)"
- **Why it's wrong**: Your RISK is always on your INVESTMENT, not the leveraged position
- **Right way**: 5% × $25,000 = $1,250 loss ✓

### ❌ WRONG: "With x10 leverage, I can make 10x profit!"
- **Why it's wrong**: Leverage magnifies RISK equally
- **Right way**: You make 10x on price % but risk 10x too ✓

### ❌ WRONG: "Stop loss is a guarantee"
- **Why it's wrong**: In flash crashes, price can gap through your stop
- **Right way**: Stops work most of the time but aren't guaranteed ✓

---

## When to Use These Calculations

✅ **BEFORE you enter a trade**
- Calculate your risk
- Verify the risk/reward ratio is good
- Set your exact exit prices

✅ **WHEN you enter a trade**
- Set stop loss at the calculated price
- Set take profit at the calculated price
- Don't move them (unless rare circumstances)

❌ **AFTER the trade is open**
- Don't move stops "to avoid losses"
- Don't change profit targets on emotion
- Let the plan execute

---

## Learning Progression

### Level 1: Understand the Concept
- Stop loss = exit if losing
- Take profit = exit if winning
- Set both BEFORE entering

### Level 2: Know the Formulas
- SL = Entry × (1 - %)
- TP = Entry × (1 + %)
- These are the ONLY formulas you need

### Level 3: Apply to Real Trading
- Enter your values into the script
- See your exact prices
- Execute your plan

### Level 4: Optimize Your Strategy
- Test different stop loss percentages
- Test different profit targets
- Find what works for YOUR trading style

---

## Testing Your Understanding

**Question 1**: If Bitcoin is at $48,000 and you want a 3% stop loss, what's your stop loss price?

<details>
<summary>Click to reveal answer</summary>

Stop Loss = $48,000 × (1 - 3/100)
         = $48,000 × 0.97
         = $46,560

Answer: **$46,560**

</details>

**Question 2**: If you invest $10,000 with a 5% stop loss, how much can you lose?

<details>
<summary>Click to reveal answer</summary>

Loss = $10,000 × (5/100)
     = $10,000 × 0.05
     = $500

Answer: **$500**

</details>

**Question 3**: If entry is $45,000 with a 12% take profit target, what's your TP?

<details>
<summary>Click to reveal answer</summary>

Take Profit = $45,000 × (1 + 12/100)
            = $45,000 × 1.12
            = $50,400

Answer: **$50,400**

</details>

---

## Now You Understand! 🎓

You now know:
- ✓ How stop loss is calculated
- ✓ How take profit is calculated
- ✓ What each price means
- ✓ How to interpret the results
- ✓ How to apply these to real trading

**Next Step**: Run the script!

```bash
python crypto_leverage.py
```

Enter your values and see the calculations in action! 🚀
