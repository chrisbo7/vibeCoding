# 🚀 QUICK START GUIDE - Crypto Leverage Calculator

## What Is This?

A Python script that calculates **stop loss and take profit prices** for crypto trading with x10 leverage.

You enter:
1. Current crypto price
2. How much to invest
3. Max loss % (stop loss)
4. Profit target %

It calculates:
- Stop loss price
- Take profit price
- Position size
- Risk/reward ratio

---

## Start Here (5 Minutes)

### Step 1: See an Example

```bash
python demo_crypto_leverage.py
```

This shows a complete example with all calculations.

### Step 2: Use It

```bash
python crypto_leverage.py
```

Enter your values and get your trade plan.

### Step 3: Verify It Works

```bash
python test_crypto_leverage.py
```

Confirms all 12 tests pass.

---

## What You'll See

```
🛑 STOP LOSS CALCULATION:
  Formula: Stop Loss Price = Entry Price × (1 - Stop Loss % / 100)
  Formula: $50,000.00 × (1 - 5/100)
  Formula: $50,000.00 × 0.95
  ➜ Result: $47,500.00

  If price hits $47,500.00, you lose: $1,250.00

📈 TAKE PROFIT CALCULATION:
  Formula: Take Profit Price = Entry Price × (1 + Target Profit % / 100)
  Formula: $50,000.00 × (1 + 10/100)
  Formula: $50,000.00 × 1.10
  ➜ Result: $55,000.00

  If price reaches $55,000.00, you make: $2,500.00
```

---

## The Two Formulas You Need

### Stop Loss
```
Stop Loss = Entry × (1 - Stop %)

Example:
$50,000 × (1 - 5/100) = $47,500
```

### Take Profit
```
Take Profit = Entry × (1 + Profit %)

Example:
$50,000 × (1 + 10/100) = $55,000
```

---

## Real Example

**Your Plan:**
- Entry: $50,000
- Invest: $25,000
- Max Loss: 5%
- Profit Target: 10%

**Script Calculates:**
```
Position Size:  5 BTC (with x10 leverage)
Stop Loss:      $47,500 (lose $1,250)
Take Profit:    $55,000 (gain $2,500)
Risk/Reward:    1:2 (good trade!)
```

---

## Files

| File | What It Does |
|------|---|
| `crypto_leverage.py` | Main calculator (run this!) |
| `demo_crypto_leverage.py` | Shows example |
| `test_crypto_leverage.py` | Tests all calculations |
| `CALCULATION_DETAILS.md` | Explains step-by-step |
| `VISUAL_GUIDE.md` | Shows visually |
| `OUTPUT_REFERENCE.md` | Shows output format |

---

## One Command to Run

```bash
python crypto_leverage.py
```

Then:
1. Enter current price: `50000`
2. Enter investment: `25000`
3. Enter stop loss %: `5`
4. Enter profit target %: `10`

Done! See your calculations. 📊

---

## Key Concepts

### Stop Loss
- Price where you exit if **losing**
- **Below** entry price
- Limits your max loss

### Take Profit
- Price where you exit if **winning**
- **Above** entry price
- Locks in your profit

### Leverage x10
- Control 10x your investment
- Position size = (Investment × 10) / Price
- Risk is real - same as position size

### Risk/Reward
- Should be ≥ 1:1.5 (make 1.5x your risk)
- Best if ≥ 1:2 (make 2x your risk)
- Tells you if trade is worth taking

---

## Common Questions

**Q: What do I do with these prices?**
A: Set them in your exchange app:
- Entry: Buy at current price
- Stop: Auto-sell if price drops
- TP: Auto-sell if price rises

**Q: Can I use different stop loss %?**
A: Yes! The script asks for YOUR preference each time.

**Q: What if I want 15% profit target instead of 10%?**
A: Enter 15 when the script asks. You control it!

**Q: Is this real trading?**
A: This calculates prices. You still need an exchange account and actual crypto.

**Q: Can I lose my entire $25,000?**
A: Yes. If liquidated before stop loss. This is why leverage is risky. Always use stops!

---

## Pro Tips

✓ Always calculate BEFORE you enter
✓ Set stop loss IMMEDIATELY after entry
✓ Don't move your stop loss (discipline!)
✓ Start with small amounts while learning
✓ Risk only what you can afford to lose

---

## One More Thing

This script only **calculates prices**. It doesn't:
- Execute trades
- Connect to exchanges
- Buy/sell crypto
- Guarantee profits

It just helps you **plan** your trades mathematically.

---

## Ready?

```bash
python crypto_leverage.py
```

🚀 Let's go!
