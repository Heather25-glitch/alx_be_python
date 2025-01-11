# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global factor for conversion
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global factor for conversion
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

# Main function to handle user input and call the appropriate conversion function
def main():
    try:
        # Get user input for temperature value
        temperature = float(input("Enter the temperature to convert: "))
        
        # Get user input for whether the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Validate user input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Perform conversion based on the user's input
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
    
    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
