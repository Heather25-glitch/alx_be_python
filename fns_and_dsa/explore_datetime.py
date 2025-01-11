from datetime import datetime, timedelta  # Importing the necessary functions

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')  # Format the date and time
    print(f"Current date and time: {formatted_date}")  # Print the formatted date and time

# Part 2: Calculate a Future Date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))  # Get number of days from user
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Add the entered days to the current date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")  # Print the future date in the required format

def main():
    display_current_datetime()  # Call to display the current date and time
    calculate_future_date()  # Call to calculate and display the future date

if __name__ == "__main__":
    main()  # Run the main function when the script is executed


