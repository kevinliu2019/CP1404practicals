def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        acknowledge = input("Is your name {}? (Y/n) ".format(name))
        if acknowledge.upper() != "Y" and acknowledge != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    part = prefix.split('.')
    name = " ".join(part).title()
    return name


main()