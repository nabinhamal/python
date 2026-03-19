# Temperature Threshold
HOT_THRESHOLD: float = 30.0

def check_temperature() -> None:
    """
    Asks the user for a temperature and checks if it's hot.
    """
    try:
        user_input: str = input("Enter the current temperature: ")
        temperature: float = float(user_input)
        if temperature > HOT_THRESHOLD:
            print(f"{temperature}°C is Hot!")
        else:
            print(f"{temperature}°C is Not Hot.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

check_temperature()


def add_two_number(a,b):
  return a+b

print(add_two_number(1,2))