"""
Day 12 - 2026-10-18
Tool: Simple Interest Calculator
What it does: Works out simple interest on a loan or deposit, the total
amount to repay or receive, and the monthly interest - so anyone can
check a bank offer, a micro-loan, or savings growth in seconds.
Who it helps: Anyone taking a small loan, keeping money in a deposit
scheme, or comparing interest rates before signing anything.
"""


def simple_interest(principal, annual_rate_percent, years):
    """Interest = principal x rate x time / 100."""
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_rate_percent < 0:
        raise ValueError("Rate cannot be negative.")
    if years < 0:
        raise ValueError("Years cannot be negative.")
    return round(principal * annual_rate_percent * years / 100, 2)


def total_amount(principal, annual_rate_percent, years):
    """Principal plus the interest earned or owed."""
    return round(principal + simple_interest(principal, annual_rate_percent, years), 2)


def monthly_interest(principal, annual_rate_percent):
    """Interest earned or owed in one month."""
    return round(simple_interest(principal, annual_rate_percent, 1) / 12, 2)


if __name__ == "__main__":
    # Example 1: 50,000 taka deposit at 8% for 3 years
    print("Deposit 50000 at 8% for 3 years - interest:",
          simple_interest(50000, 8, 3), "- total:", total_amount(50000, 8, 3))

    # Example 2: a 20,000 taka loan at 12% for 2 years
    print("Loan 20000 at 12% for 2 years - interest:",
          simple_interest(20000, 12, 2), "- repay:", total_amount(20000, 12, 2))

    # Example 3: monthly interest on 100,000 taka at 9%
    print("Monthly interest on 100000 at 9%:", monthly_interest(100000, 9))
