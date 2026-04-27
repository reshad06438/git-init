# first line ensures user put numerical values only for the statement block 
def get_float(prompt, min_value=0, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Enter a value greater than or equal to {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Enter a value less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Let's user choose choose what financial route to select(looking to add more)
def get_risk_profile():
    print("\nChoose your financial style:")
    print("1. Safe")
    print("2. Balanced")
    print("3. Aggressive")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return "Safe", {"Checking": 40, "Savings": 40, "Bonds": 15, "Stocks": 5}
    elif choice == "2":
        return "Balanced", {"Checking": 35, "Savings": 30, "Bonds": 15, "Stocks": 20}
    elif choice == "3":
        return "Aggressive", {"Checking": 25, "Savings": 20, "Bonds": 15, "Stocks": 40}
    else:
        print("Invalid choice. Balanced profile selected by default.")
        return "Balanced", {"Checking": 35, "Savings": 30, "Bonds": 15, "Stocks": 20}

# based of gpa it calculates the percentage of the reward
# (future looking at data to approximate percentage)

def calculate_gpa_reward(gpa, max_reward_percent):
    if gpa >= 3.8:
        level = "Well Done"
        reward = max_reward_percent
    elif gpa >= 3.5:
        level = "Phenomonal Job"
        reward = max_reward_percent * 0.75
    elif gpa >= 3.0:
        level = "Solid Performance"
        reward = max_reward_percent * 0.50
    elif gpa >= 2.5:
        level = "Needs Imporvement"
        reward = max_reward_percent * 0.25
    else:
        level = "No Reward"
        reward = 0

    return level, reward


def calculate_allocations(amount, allocation_rules):
    results = {}

    for category, percent in allocation_rules.items():
        results[category] = amount * (percent / 100)

    return results

# nice visualization to see bar chart
def show_bar(label, amount, total):
    if total == 0:
        blocks = 0
    else:
        blocks = int((amount / total) * 30)

    bar = "█" * blocks
    print(f"{label:<10} | {bar:<30} ${amount:,.2f}")


def main():
    print("=" * 50)
    print("        SMART GPA-BASED FINANCE PLANNER")
    print("=" * 50)

    while True:
        income = get_float("\nEnter your monthly/bi-weekly/weekly income: $", 1)
        gpa = get_float("Enter your GPA out of 4.0: ", 0, 4.0)

        base_misc_percent = get_float("Enter your miscellaneous spending percent: ", 0, 100)
        max_reward_percent = get_float("Enter max GPA reward percent: ", 0, 100)

        goal_name = input("\nEnter a savings goal name: ")
        goal_amount = get_float(f"Enter target amount for {goal_name}: $", 1)

        profile_name, allocation_rules = get_risk_profile()

        performance_level, reward_percent = calculate_gpa_reward(gpa, max_reward_percent)

        total_misc_percent = base_misc_percent + reward_percent

        if total_misc_percent > 60:
            print("\nWarning: Misc spending is very high, so it was capped at 60%.")
            total_misc_percent = 60

        misc_amount = income * (total_misc_percent / 100)
        leftover = income - misc_amount

        allocations = calculate_allocations(leftover, allocation_rules)

        monthly_savings = allocations["Savings"]

        if monthly_savings > 0:
            months_to_goal = goal_amount / monthly_savings
        else:
            months_to_goal = 0

        print("\n" + "=" * 50)
        print("                 FINANCE REPORT")
        print("=" * 50)

        print(f"Income: ${income:,.2f}")
        print(f"GPA: {gpa:.2f}")
        print(f"Performance Level: {performance_level}")
        print(f"Risk Profile: {profile_name}")

        print("\nMisc Spending:")
        print(f"Base Misc Percent: {base_misc_percent:.2f}%")
        print(f"GPA Reward Added: {reward_percent:.2f}%")
        print(f"Final Misc Percent: {total_misc_percent:.2f}%")
        print(f"Misc Allowance: ${misc_amount:,.2f}")

        print("\nRemaining Money Allocation:")
        for category, amount in allocations.items():
            print(f"{category}: ${amount:,.2f}")

        print("\nVisual Allocation Chart:")
        for category, amount in allocations.items():
            show_bar(category, amount, leftover)

        print("\nSavings Goal Tracker:")
        print(f"Goal: {goal_name}")
        print(f"Target Amount: ${goal_amount:,.2f}")
        print(f"Monthly Savings Contribution: ${monthly_savings:,.2f}")
        print(f"Estimated Months to Reach Goal: {months_to_goal:.1f}")

        print("\nSmart Recommendation:")
        if gpa >= 3.5 and monthly_savings > misc_amount:
            print("Excellent balance: strong grades and strong savings behavior.")
        elif misc_amount > monthly_savings:
            print("Consider lowering misc spending to reach your goal faster.")
        else:
            print("Your budget is balanced and moving in a good direction.")

        again = input("\nRun another plan? yes/no: ").lower()

        if again != "yes":
            print("\nProgram ended. Great work building your finance plan.")
            break


main()

#(looking forward to additional features for users to use 