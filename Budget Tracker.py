# -*- coding: utf-8 -*-
"""
Personal Budget Tracker

What it does:
- Tracks monthly income, expenses, and debts
- Calculates savings rate and debt-to-income (DTI)
- Highlights spending patterns by category
- Gives plain English recommendations
- Saves a snapshot to a text file

Author: Deniz Diloglu
Section: 9
Student ID: 501399127
"""

# Categories for tracking - using tuple since these won't change
spending_categories = (
    "Housing", "Food", "Transportation", "Utilities",
    "Entertainment", "Healthcare", "Education", "Other"
)

loan_categories = (
    "Credit Card", "Student Loan", "Car Loan", 
    "Personal Loan", "Mortgage", "Other Debt"
)

# Warning thresholds for financial health
critical_dti_threshold = 0.43


def ask_for_amount(message):
    """
    Get dollar amounts from user with validation.
    Keep looping with while until we get valid positive number.
    """
    while True:
        try:
            user_input = float(input(message))
            if user_input < 0:
                print("Please enter a positive amount.")
            else:
                return user_input
        except ValueError:
            print("That is not a number. Try again.")


def collect_expenses():
    """
    Go through each category and ask how much was spent.
    Store in dictionary with category names as keys.
    """
    expenses = {}
    print("\nEnter your monthly expenses:")
    
    # For loop through each category
    for category in spending_categories:
        amount = ask_for_amount(f"{category}: $")
        expenses[category] = amount
    
    return expenses


def collect_debts():
    """
    Let user add debts with numbered menu.
    Uses while loop so user can keep adding until done.
    """
    debts = []
    print("\nEnter your debts and loans:\n")
    
    # While loop for adding multiple debts
    while True:
        print("\nDebt types:")
        # Enumerate gives us automatic numbering
        for num, loan_type in enumerate(loan_categories, 1):
            print(f"{num}. {loan_type}")
        print("0. Done adding debts")
        
        # Get choice with validation
        while True:
            try:
                choice = int(input("\nSelect debt type (0 to finish): "))
                if choice == 0:
                    return debts
                elif 1 <= choice <= len(loan_categories):
                    selected = loan_categories[choice - 1]
                    break
                else:
                    print(f"Enter number between 0 and {len(loan_categories)}.")
            except ValueError:
                print("Enter a valid number.")

        # Get debt details
        balance = ask_for_amount(f"Balance for {selected}: $")
        if balance == 0:
            continue
        rate = ask_for_amount(f"Interest rate for {selected} (%): ")
        payment = ask_for_amount(f"Monthly payment for {selected}: $")

        # Store in dictionary and add to list
        debt = {
            "type": selected,
            "balance": balance,
            "rate": rate,
            "payment": payment
        }
        debts.append(debt)
        print(f"Added {selected}.")


def show_summary(income, expenses, debts):
    """
    Display financial summary with calculations and recommendations.
    This is the main analysis function that does all the work.
    """
    print("\n" + "=" * 50)
    print("           Financial Summary")
    print("=" * 50)

    # Calculate totals using arithmetic expressions
    total_expenses = sum(expenses.values())
    total_debt_payments = sum(d["payment"] for d in debts)
    total_obligations = total_expenses + total_debt_payments
    remaining = income - total_obligations

    # Show main numbers
    print(f"\nMonthly income:        ${income:,.2f}")
    print(f"Total expenses:        ${total_expenses:,.2f}")
    print(f"Debt payments:         ${total_debt_payments:,.2f}")
    print(f"Remaining:             ${remaining:,.2f}")

    # Calculate percentages
    if income > 0:
        savings_rate = (remaining / income) * 100
        print(f"Savings rate:          {savings_rate:.1f}%")
        
        if total_debt_payments > 0:
            dti = (total_debt_payments / income) * 100
            print(f"Debt-to-income:        {dti:.1f}%")

    # Show expense breakdown with bars
    print("\n" + "-" * 50)
    print("Expenses by category:")
    print("-" * 50)

    # Sort from highest to lowest using sorted and lambda
    sorted_expenses = sorted(expenses.items(), key=lambda x: x[1], reverse=True)
    
    for category, amount in sorted_expenses:
        pct = (amount / income * 100) if income > 0 else 0
        bar_len = int(pct / 2)
        bar = "█" * bar_len
        print(f"{category:15s}: ${amount:7.2f} ({pct:5.1f}%) {bar}")

    # Show debt summary if exists
    if len(debts) > 0:
        print("\n" + "-" * 50)
        print("Debt summary:")
        print("-" * 50)
        
        for d in debts:
            print(f"{d['type']:15s}: ${d['balance']:9,.2f} | "
                  f"{d['rate']:5.1f}% | ${d['payment']:7.2f}/mo")
        
        total_owed = sum(d["balance"] for d in debts)
        print(f"\nTotal debt: ${total_owed:,.2f}")

    # Spending analysis
    print("\n" + "-" * 50)
    print("Spending notes:")
    print("-" * 50)
    
    for category, amount in expenses.items():
        if income > 0:
            pct = (amount / income) * 100
            # Use if/elif/else to categorize spending
            if pct >= 30:
                print(f"HIGH: {category} is {pct:.1f}% of income")
            elif pct >= 15:
                print(f"Moderate: {category} is {pct:.1f}%")

    # Debt analysis if applicable
    if len(debts) > 0:
        print("\n" + "-" * 50)
        print("Debt notes:")
        print("-" * 50)
        
        if income > 0:
            dti = total_debt_payments / income
        else:
            dti = 0
        
        # Use if/elif/else for DTI evaluation
        if dti >= 0.50:
            print("CRITICAL: DTI above 50%. Take action now.")
        elif dti >= critical_dti_threshold:
            print("HIGH: DTI above 43%. Focus on debt reduction.")
        elif dti >= 0.36:
            print("MODERATE: DTI 36-43%. Manageable.")
        else:
            print("GOOD: DTI below 36%. Healthy level.")

    # Recommendations
    print("\n" + "-" * 50)
    print("Recommendations:")
    print("-" * 50)

    # Calculate savings for recommendations
    if income > 0:
        savings_pct = (remaining / income) * 100
    else:
        savings_pct = 0

    # Check for high interest debts using list comprehension
    if len(debts) > 0:
        high_interest = [d for d in debts if d["rate"] >= 15]
        if len(high_interest) > 0:
            print("Pay down high interest debts first.")

    # Savings advice using if/elif/else
    if savings_pct >= 20:
        print("Excellent savings rate. Consider long term investing.")
    elif savings_pct >= 10:
        print("Good savings. Try to increase to 20%.")
    elif savings_pct > 0:
        print("Saving but below 10%. Look for areas to cut.")
    else:
        print("Spending exceeds income. Reduce expenses.")

    print("=" * 50)


def save_to_file(income, expenses, debts):
    """
    Save financial data to text file for record keeping.
    Demonstrates file output as required by assignment.
    """
    try:
        # Open file for writing
        with open("budget_data.txt", "w") as f:
            f.write("=== Budget Tracker Data ===\n\n")
            f.write(f"Income: ${income:.2f}\n\n")
            
            f.write("Expenses:\n")
            for cat, amt in expenses.items():
                f.write(f"  {cat}: ${amt:.2f}\n")
            
            total_exp = sum(expenses.values())
            f.write(f"\nTotal expenses: ${total_exp:.2f}\n")
            
            f.write("\nDebts:\n")
            if len(debts) == 0:
                f.write("  None\n")
            else:
                for d in debts:
                    f.write(f"  {d['type']}: ${d['balance']:.2f} "
                           f"at {d['rate']:.1f}%\n")
            
            total_debt = sum(d["payment"] for d in debts) if debts else 0
            remaining = income - total_exp - total_debt
            f.write(f"\nRemaining: ${remaining:.2f}\n")
        
        print("\nData saved to budget_data.txt")
    except IOError:
        print("Error: Could not save file")


def main():
    """
    Main function - controls program flow.
    Gets user input and calls other functions to process data.
    """
    print("=" * 50)
    print("      Personal Budget Tracker")
    print("=" * 50)
    print("\nTrack your income, expenses, and debts.")
    print("Get instant analysis and recommendations.\n")

    # Get income first
    income = ask_for_amount("Enter your monthly income: $")
    
    # Collect expenses using function
    expenses = collect_expenses()
    
    # Ask about debts with validation
    # Had a bug here where any input besides y counted as no
    # Fixed by adding a while loop to validate
    while True:
        has_debts = input("\nDo you have debts to track? (y/n): ").lower().strip()
        if has_debts == 'y':
            debts = collect_debts()
            break
        elif has_debts == 'n':
            debts = []
            print("No debts recorded.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    # Show complete summary with all calculations
    show_summary(income, expenses, debts)
    
    # Save everything to file
    save_to_file(income, expenses, debts)
    
    print("\nThanks for using Budget Tracker!")


# Program entry point
if __name__ == "__main__":
    main()