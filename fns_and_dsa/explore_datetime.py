import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get current date and time
    # Format the date and time in "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Ask the user to input the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()  # Get current date
        # Calculate the future date by adding the specified number of days
        future_date = current_date + datetime.timedelta(days=days_to_add)
        # Print the future date in "YYYY-MM-DD" format
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        # Handle invalid input (non-integer input)
        print("Please enter a valid number of days.")

def main():
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()
