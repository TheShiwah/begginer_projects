# takes an email and slicers into username and domain
# also slices into username domain and extension
# collect email from user
# split email using @, first part is the username, the second part will be saved as domain
# split domain using .

def main():
    print("welcome to the email slicer ")
    print("")

    email_input = input("Input your email address:")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension", extension)


if __name__ == "__main__":
    main()
