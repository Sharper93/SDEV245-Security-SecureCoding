"""
RBAC and AUTHENTICATION Assignement
Security and Secure Coding SDEV 245
Author: Smantha Harper
Date: 08/27/2025

Summary: This script demostrates the principle of Confidentiality from the CIA Triad. 
Confidentialty ensures that sensitive information and functions are only accessible by authorized users. 
In this example, role-based access control restricts access to
the admin and user portals, preventing unauthorized use and protecting data.
"""


def adminPortal():
    """
        Function to call upon login to Admin Portal.
    """
    print("~~~Welcome Admin!~~~")
    
def userPortal():
    """
        Function to call upon login to User Portal.
    """
    print("~~~Welcome User!~~~")
        
def main():
    # define input for user's username 
    username = input("Enter Username: ")

    # dictionary of allowed user/admin
    users = {
        "Sammi": "admin",
        "Brian": "user"
    }

    # define role to be assoicated with username
    role = users.get (username, None)

    # if-else to determine if the username is accepted 
    if role:
        print (f"Welcome {username}, you are a {role}.")
        if role == "admin":
            print("You can access the admin portal.")
            adminPortal()
        else:
            print("You can access the user portal.")
            userPortal()
    else:
        print("ERROR! Unknown username! Access denied!")


if __name__ == "__main__":
    main()
