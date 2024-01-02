def validate_email(email):
    if not isinstance(email, str):
        return False

    if "@" not in email or "." not in email:
        return False

    username, domain = email.split("@")

    if domain not in ["gmail.com", "outlook.com"]:
        return False

    if not username.isalnum():
        return False

    return True

email = input("Enter A Valid Email Address: ")
if validate_email(email):
    print("🌟 The Email Address", email, "Is Valid!")
else:
    print("❌ Ughh! The Email You Provided Is Not Valid!")
    exit()

def validate_password(password):
    if not isinstance(password, str):
        return False

    if len(password) < 5 or len(password) > 14:
        return False

    capital_found = False
    number_found = False

    for char in password:
        if char.isupper():
            capital_found = True
        elif char.isdigit():
            number_found = True
        elif not char.isalnum():
            return False

    if not capital_found or not number_found:
        return False

    return True

password = input("Enter A Valid Password: ")
if validate_password(password):
    print("🌟 The Password", password, "Is Valid!")
else:
    print("❌ Ughh! The Password You Provided Is Not Strong Enough!")
    exit()

username = input("Enter Your Account Name: ")
print("🌟 Congratulations! Here Are The Credentials Of Your Account:\nEmail Address:", email, "\nAccount Password:", password, "\nAccount Username:", username)
