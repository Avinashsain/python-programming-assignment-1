import string

def check_password_strength(password):
    # Conditions
    # It checks whether the password length is at least 8 characters.
    has_min_length = len(password) >= 8
    # It checks whether the password contains at least one uppercase (A–Z) letter.
    has_upper = any(char.isupper() for char in password)
    # It checks whether the password contains at least one lowercase (a–z) letter.
    has_lower = any(char.islower() for char in password)
    # It checks if the password contains at least one number (0–9).
    has_digit = any(char.isdigit() for char in password)
    # It checks whether the password contains at least one special character
    has_special = any(char in string.punctuation for char in password)

    return has_min_length and has_upper and has_lower and has_digit and has_special

password = input("Enter your password: ")

if check_password_strength(password):
    print("✅ Password is strong!")
else:
    print("❌ Weak password! Your password must contain:")
    print("- At least 8 characters")
    print("- Uppercase and lowercase letters")
    print("- At least one digit (0–9)")
    print("- At least one special character (!,@,#,$,%, etc.)")