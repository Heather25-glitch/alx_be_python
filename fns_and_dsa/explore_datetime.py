import datetime  # Ensure this line is present to import the datetime module

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')  # Format the date and time
    print(f"Current date and time: {formatted_date}")  # Print the formatted date and time

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask the user to input the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    current_date = datetime.datetime.now()  # Get the current date and time
    future_date = current_date + datetime.timedelta(days=days_to_add)  # Add days to the current date
    # Print the future date in the format "YYYY-MM-DD"
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to call the other functions
def main():
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()  # Run the main function when the script is executed


