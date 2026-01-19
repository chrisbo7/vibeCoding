# Crypto Leverage Calculator - Project Files

## 📁 Project Structure

```
CODE test/
├── crypto_leverage.py              ← Main interactive calculator script
├── test_crypto_leverage.py         ← Unit tests (12 tests, all passing)
├── demo_crypto_leverage.py         ← Demo with example calculation
├── CRYPTO_LEVERAGE_README.md       ← Quick start guide
├── CRYPTO_LEVERAGE_GUIDE.md        ← Detailed explanation guide
├── CALCULATION_DETAILS.md          ← Step-by-step calculation walkthrough
└── [This file]
```

## 📄 File Descriptions

### 1. `crypto_leverage.py` ⭐ **START HERE**
**Main interactive script - this is what you run!**

**What it does:**
- Prompts for: Current price, Investment amount, Stop loss %, Profit target %
- Calculates: Position size, Stop loss price, Take profit price, Risk/reward ratio
- Shows all formulas and results clearly

**Run it:**
```bash
python crypto_leverage.py
```

**Features:**
- ✓ Input validation
- ✓ Shows calculation formulas
- ✓ Clear, formatted output
- ✓ Error handling

---

### 2. `test_crypto_leverage.py` 🧪 **TEST & VALIDATE**
**Unit test suite - 12 tests, all passing**

**What it tests:**
- Input validation (valid/invalid numbers)
- Position size calculations
- Stop loss calculations
- Take profit calculations
- Risk/reward ratio
- Full trading scenarios

**Run it:**
```bash
python test_crypto_leverage.py
```

**Output:**
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

### 3. `demo_crypto_leverage.py` 📊 **DEMO MODE**
**Shows a complete example with all calculations explained**

**What it does:**
- Uses fixed example values
- Shows each calculation step-by-step
- Explains the formulas
- Perfect for learning

**Run it:**
```bash
python demo_crypto_leverage.py
```

**Example Output:**
```
Entry Price:        $50,000.00
Investment:         $25,000.00
Stop Loss %:        5%
Target Profit %:    10%

Position Size = (25,000 × 10) / 50,000 = 5.00000000 BTC/ETH

Stop Loss Price = $50,000 × (1 - 5/100) = $47,500.00
  If price hits $47,500, you lose: $1,250.00

Take Profit Price = $50,000 × (1 + 10/100) = $55,000.00
  If price reaches $55,000, you make: $2,500.00

Risk/Reward Ratio = 2,500 / 1,250 = 1:2.00
  For every $1 you risk, you stand to make $2
```

---

### 4. `CRYPTO_LEVERAGE_README.md` 📖 **QUICK START**
**Fast guide to get started immediately**

**Contains:**
- Overview of features
- Basic usage instructions
- Example session
- Troubleshooting tips
- File list

**Read when:** You just want to start using it

---

### 5. `CRYPTO_LEVERAGE_GUIDE.md` 📘 **DETAILED EXPLANATION**
**Complete guide to understanding all calculations**

**Contains:**
- Full formula explanations for each calculation
- Step-by-step examples
- Common strategies table
- Risk/reward guidelines
- FAQ section
- Pro tips

**Read when:** You want to understand the "why" behind each formula

---

### 6. `CALCULATION_DETAILS.md` 🔢 **STEP-BY-STEP WALKTHROUGH**
**Exact breakdown of your specific example**

**Contains:**
- Complete walkthrough with $50K entry, $25K investment
- Position size calculation
- Stop loss calculation (5%)
- Take profit calculation (10%)
- Potential loss/profit calculations
- Risk/reward ratio calculation
- Real trade outcomes

**Read when:** You want to see exactly how YOUR example is calculated

---

## 🚀 Quick Start

### 1️⃣ First Time? Run Demo

```bash
python demo_crypto_leverage.py
```

This shows you exactly how calculations work with a real example.

### 2️⃣ Ready to Use It? Run Interactive

```bash
python crypto_leverage.py
```

Then enter your values:
- Current crypto value
- Investment amount
- Stop loss percentage
- Target profit percentage

### 3️⃣ Want to Verify? Run Tests

```bash
python test_crypto_leverage.py
```

Confirms all calculations are correct (12 tests pass).

---

## 📊 The Calculations At A Glance

| Calculation | Formula | What It Means |
|-------------|---------|---------------|
| **Position Size** | (Investment × Leverage) / Price | How much crypto you buy |
| **Stop Loss** | Entry × (1 - Stop %) | Price to exit if losing |
| **Take Profit** | Entry × (1 + Target Profit %) | Price to exit if winning |
| **Max Loss** | Investment × Stop % | Actual $ you lose if stopped |
| **Max Profit** | Investment × Target Profit % | Actual $ you make if TP hit |
| **Risk/Reward** | Max Profit / Max Loss | Quality of your trade |

---

## 🎯 Example Scenario

**You want to trade Bitcoin:**
- Current price: $50,000
- You have: $25,000 to invest
- Max loss tolerance: 5%
- Profit target: 10%

**What the script calculates:**

| Value | Calculation | Result |
|-------|-------------|--------|
| Position Size | ($25K × 10) / $50K | 5 BTC |
| Stop Loss | $50K × 0.95 | $47,500 |
| Take Profit | $50K × 1.10 | $55,000 |
| Max Loss | $25K × 5% | $1,250 |
| Max Profit | $25K × 10% | $2,500 |
| Risk/Reward | $2,500 / $1,250 | 1:2.00 ✓ Good! |

---

## 🔍 Understanding the Output

When you run the calculator, you see:

```
📥 YOUR INPUTS:
  Current Price (Entry):        $50,000.00
  Investment Amount:            $25,000.00
  Stop Loss Tolerance:          5.00%
  Target Profit Goal:           10.00%
  Leverage:                     x10

💼 POSITION DETAILS:
  Position Size (Crypto):       5.00000000 BTC/ETH
  Effective Capital:            $250,000.00

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

💸 POTENTIAL LOSS (at stop loss):
  Formula: Investment × (Stop Loss % / 100)
  Formula: $25,000.00 × (5/100)
  ➜ Result: $1,250.00

💰 POTENTIAL PROFIT (at take profit):
  Formula: Investment × (Target Profit % / 100)
  Formula: $25,000.00 × (10/100)
  ➜ Result: $2,500.00

⚖️  RISK/REWARD RATIO:
  Formula: Reward / Risk
  Formula: $2,500.00 / $1,250.00
  ➜ Result: 1:2.00
```

---

## 📚 Documentation Guide

| Want to... | Read... |
|------------|---------|
| Start using immediately | `CRYPTO_LEVERAGE_README.md` |
| Understand formulas | `CRYPTO_LEVERAGE_GUIDE.md` |
| See calculation steps | `CALCULATION_DETAILS.md` |
| See example output | `demo_crypto_leverage.py` |
| Verify correctness | `test_crypto_leverage.py` |

---

## ⚡ Command Reference

```bash
# Interactive calculator (what you'll use most)
python crypto_leverage.py

# See demo with example values
python demo_crypto_leverage.py

# Run all unit tests
python test_crypto_leverage.py

# On Windows with virtualenv
C:\Users\cmpotsiar\.virtualenvs\YOUR_DJANGO_PROJECT-2y_e-DLS\Scripts\python.exe crypto_leverage.py
```

---

## ✅ Status

- ✓ Main script complete
- ✓ All 12 unit tests passing
- ✓ Documentation complete
- ✓ Ready to use!

---

## 🎓 Learning Path

1. **Start**: `python demo_crypto_leverage.py` (see example)
2. **Learn**: Read `CALCULATION_DETAILS.md` (understand steps)
3. **Use**: `python crypto_leverage.py` (calculate your trades)
4. **Verify**: `python test_crypto_leverage.py` (check accuracy)

---

Enjoy calculating your trades! 🚀📈

**Questions?** Check the FAQ in `CRYPTO_LEVERAGE_GUIDE.md`
