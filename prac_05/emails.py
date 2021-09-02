"""
CP1404 - Practical 05
Emails
"""

YES_ANSWERS = ["", "Y", "YES"]
# NO_ANSWERS = ["N", "NO"]


def main():
    """Program that gets emails and names for a dictionary and prints it"""
    emails = {}
    email = get_valid_email()
    while email != "":
        name = find_name_from_email(email)
        answer = input(f"Is your name {name}? (Y/n) ").upper()

        # while answer not in YES_ANSWERS:
        #     if answer in NO_ANSWERS:
        #         name = input("Name: ").title()
        #         break
        #     else:
        #         print("Invalid answer")
        #         answer = input(f"Is your name {name}? (Y/n) ").upper()

        if answer not in YES_ANSWERS:
            name = input("Name: ")

        emails[email] = name
        email = get_valid_email()

    print()
    for email, name in emails.items():
        print(f"{name} ({email})")


def find_name_from_email(email):
    """Finds name from email"""
    email_tag = email[0:email.find("@")]
    email_tag_split = email_tag.split(".")
    email_tag_joined = " ".join(email_tag_split).title()
    return email_tag_joined


def get_valid_email():
    """Gets empty string or valid email with only 1 @"""
    email = input("Email: ")
    if email == "":
        return email
    while email.count("@") != 1:
        print("Invalid email; use only 1 @")
        email = input("Email: ")
    return email


main()
