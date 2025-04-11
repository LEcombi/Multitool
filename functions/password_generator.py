import random
import string

def generate_password(length=12):
    """Generates a secure password with the specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # At least one character from each category
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to randomize the order
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(16))