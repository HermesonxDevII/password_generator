from password import (
    generate_password,
    create_validator,
    validate_password,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_symbol
)

def test_generation():
    print("=== Generation Test ===")
    pwd = generate_password(12, True, True, True, True)
    print(f"Generated password: {pwd}")

def test_validation():
    print("\n=== Validation Test ===")
    test_pwd = "XV:o3=Dg{D_R|u:|UdBT"
    validator = create_validator(20, [has_uppercase, has_lowercase, has_digit, has_symbol])
    print(f"Password '{test_pwd}' is valid? {validate_password(test_pwd, [validator])}")

if __name__ == "__main__":
    test_generation()
    test_validation()