import re, string, random

def main():
    while True:
        print('''Do you want to:
              1. Check Password
              2. Generate Password''')
        user_choice = input("Enter 1 or 2: ")
        
        if user_choice == "1":
            check_password()
            break
        elif user_choice == "2":
            generate_password_flow()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def check_password():
    common_passwords = ["password", "12345678", "qwerty", "abc123", "password1", "098765"]

    while True:
        urpass = input("Enter a Password: ")
        if urpass.lower() in common_passwords:
            print("Password is too common. Please choose a different one.")
            continue
        elif is_strong_password(urpass):
            print("Password is strong.")
            break
        else:
            print("Password is not strong enough. Please try again.")

def is_strong_password(password):
    if len(password) < 8:
        print("Password should at least contain 8 characters!")
        return False

    lowercase_pattern = re.compile(r'[a-z]')
    uppercase_pattern = re.compile(r'[A-Z]')
    digit_pattern = re.compile(r'\d')
    special_char_pattern = re.compile(r'[!@#$%^&*()_\-+=\[\]{}|;:\'",.<>?/]')

    if (lowercase_pattern.search(password) is None or
        uppercase_pattern.search(password) is None or
        digit_pattern.search(password) is None or
        special_char_pattern.search(password) is None):
        return False
    
    return True

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd

def generate_password_flow():
    min_length = int(input("Enter the minimum length: "))
    has_number = input("Do you want to include numbers? (y/n) ").lower() == "y"
    has_special = input("Do you want to include special characters? (y/n) ").lower() == "y"
    pwd = generate_password(min_length, has_number, has_special)
    print("Generated Password: " + pwd)

# start
main()
