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
    print("=== Gerador de Senha ===")

    length = int(input("Quantos digitos precisa ter na senha?: "))
    use_uppercase = input("Contém letras maiusculas? (s/n): ").lower() == "s"
    use_lowercase = input("Contém letras minusculas? (s/n): ").lower() == "s"
    use_digits = input("Contém números? (s/n): ").lower() == "s"
    use_symbols = input("Contem caracteres especiais? (s/n): ").lower() == "s"

    pwd = generate_password(
        length,
        use_uppercase,
        use_lowercase,
        use_digits,
        use_symbols
    )
    print(f"\nSenha gerada: {pwd}")

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
        print("A senha atende aos critérios.")
    else:
        print("A senha NÃO atende aos critérios.")
