from password import (
    generate_password,
    create_validator,
    validate_password,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol
)

if __name__ == "__main__":
    print("=== Password Generator & Validator ===")

    length = int(input("Enter password length: "))
    use_uppercase = input("Use uppercase? (y/n): ").lower() == "y"
    use_lowercase = input("Use lowercase? (y/n): ").lower() == "y"
    use_digits = input("Use digits? (y/n): ").lower() == "y"
    use_symbols = input("Use symbols? (y/n): ").lower() == "y"

    pwd = generate_password(
        length,
        use_uppercase,
        use_lowercase,
        use_digits,
        use_symbols
    )
    print(f"\nGenerated password: {pwd}")

    validator = create_validator(
        length,
        [crit for crit, use in [
            (has_uppercase, use_uppercase),
            (has_lowercase, use_lowercase),
            (has_digit, use_digits),
            (has_symbol, use_symbols)
        ] if use]
    )

    if validate_password(pwd, [validator]):
        print("Password meets the criteria.")
    else:
        print("Password does NOT meet the criteria.")
