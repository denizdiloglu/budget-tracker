# 💰 Personal Budget Tracker

A command-line Python application that helps you manage your monthly finances by tracking income, expenses, and debts — then giving you instant analysis and plain-English recommendations.

---

## Features

- **Income & Expense Tracking** — Enter spending across 8 categories (Housing, Food, Transportation, Utilities, Entertainment, Healthcare, Education, Other)
- **Debt Management** — Log multiple debt types (Credit Card, Student Loan, Car Loan, Mortgage, etc.) with balance, interest rate, and monthly payment
- **Financial Analysis**
  - Savings rate calculation
  - Debt-to-Income (DTI) ratio evaluation
  - Visual spending breakdown with category bars
- **Smart Recommendations** — Flags high-interest debts, low savings rates, and over-budget categories
- **File Export** — Saves a snapshot of your financial data to `budget_data.txt`

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python Budget_Tracker.py
```

Follow the prompts to enter your:
1. Monthly income
2. Expenses by category
3. Any active debts (optional)

---

## Example Output

```
==================================================
           Financial Summary
==================================================

Monthly income:        $4,000.00
Total expenses:        $2,800.00
Debt payments:         $400.00
Remaining:             $800.00
Savings rate:          20.0%
Debt-to-income:        10.0%

--------------------------------------------------
Expenses by category:
--------------------------------------------------
Housing        :  $1200.00 ( 30.0%) ███████████████
Food           :   $500.00 ( 12.5%) ██████
...

Recommendations:
--------------------------------------------------
Excellent savings rate. Consider long term investing.
```

---

## Project Structure

```
budget-tracker/
│
├── Budget_Tracker.py   # Main application
└── budget_data.txt     # Auto-generated output file (after first run)
```

---

## Concepts Used

- Functions, loops, and conditionals
- Dictionaries and lists for data storage
- Tuples for fixed category data
- List comprehensions
- String formatting and file I/O
- Input validation with try/except

---

## Author

**Deniz Diloglu**  
[GitHub](https://github.com/Wyskoln)
