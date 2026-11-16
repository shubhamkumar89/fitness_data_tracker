
import csv
import os
import matplotlib.pyplot as plt

# Daily step goal
STEP_GOAL = 10000
DATA_FILE = "fitness_records.csv"

# Lists to store daily fitness data
steps = []
calories = []


# Load previously saved records
def load_records():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    steps.append(int(row["steps"]))
                    calories.append(float(row["calories"]))

        except (ValueError, KeyError, OSError) as error:
            print("Error loading records:", error)


# Save records in CSV file
def save_records():
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["day", "steps", "calories"])

        for i in range(len(steps)):
            writer.writerow([i + 1, steps[i], calories[i]])


# Add daily fitness record
def add_record():
    print("\n--- Add Daily Record ---")

    try:
        day_steps = int(input("Enter steps walked today: "))
        day_calories = float(input("Enter calories burned: "))

        if day_steps < 0 or day_calories < 0:
            print("Invalid input! Values cannot be negative.")
            return

        steps.append(day_steps)
        calories.append(day_calories)

        save_records()

        percentage = (day_steps / STEP_GOAL) * 100

        print("\nRecord saved successfully!")
        print("Day:", len(steps))
        print("Steps:", day_steps)
        print("Calories:", day_calories)
        print("Goal Progress:", round(percentage, 2), "%")

        if day_steps >= STEP_GOAL:
            print("Goal Achieved: Yes")
        else:
            print("Goal Achieved: No")

    except ValueError:
        print("Please enter valid numeric values.")


# Display activity summary
def show_summary():
    print("\n--- Activity Summary ---")

    if len(steps) == 0:
        print("No records available. Add a record first.")
        return

    total_steps = sum(steps)
    average_steps = total_steps / len(steps)
    total_calories = sum(calories)

    best_day = steps.index(max(steps)) + 1

    goal_days = sum(1 for s in steps if s >= STEP_GOAL)

    print("Total Days:", len(steps))
    print("Total Steps:", total_steps)
    print("Average Steps:", round(average_steps, 2))
    print("Total Calories:", total_calories)
    print("Best Day: Day", best_day)
    print("Goal Achieved Days:", goal_days)

    
# View all previous records
def view_records():

    print("\n--- All Previous Records ---")

    if len(steps) == 0:
        print("No records available.")
        return

    for i in range(len(steps)):
        print(f"Day {i+1}: Steps = {steps[i]}, Calories = {calories[i]}")



# Calculate BMI
def calculate_bmi():
    print("\n--- BMI Calculator ---")

    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in metres: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = weight / (height * height)

        print("Your BMI:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError:
        print("Please enter valid numbers.")


# Display daily steps graph
def show_chart():
    if len(steps) == 0:
        print("No records available to display chart.")
        return

    days = [f"Day {i+1}" for i in range(len(steps))]

    plt.figure(figsize=(9, 5))

    plt.bar(days, steps)

    plt.axhline(
        y=STEP_GOAL,
        linestyle="--",
        label="10000 Steps Goal"
    )

    plt.title("Daily Steps")
    plt.xlabel("Day")
    plt.ylabel("Steps")
    plt.legend()
    plt.tight_layout()

    plt.show()


# Main menu

# Main Menu
def main():

    load_records()

    print("\nWelcome to Fitness Data Tracker!")

    while True:

        print("\n================================")
        print("       FITNESS DATA TRACKER")
        print("================================")
        print("1. Add Record")
        print("2. Summary")
        print("3. BMI Calculator")
        print("4. Daily Steps Chart")
        print("5. View All Previous Records")
        print("6. Exit")
        print("================================")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_record()

        elif choice == "2":
            show_summary()

        elif choice == "3":
            calculate_bmi()

        elif choice == "4":
            show_chart()

        elif choice == "5":
            view_records()

        elif choice == "6":
            save_records()
            print("Records saved successfully!")
            print("Thank you for using Fitness Data Tracker!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()
