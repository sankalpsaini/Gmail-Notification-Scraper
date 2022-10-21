# imaplib program to access gmail servers
import imaplib
from getpass import getpass
from os import system

mail = imaplib.IMAP4_SSL('imap.gmail.com')


def retrieveSaved():
    file = open("usernames.txt", "r")
    lines = file.readlines()
    usernames = {}
    count = 0
    for line in lines:
        count+=1
        username, password = line.split(":")
        usernames[str(count)] = ([username, password.strip()])
    file.close()
    return usernames

def newEntry(username,password):
    file = open("usernames.txt", "a")
    file.write("\n"+username+":"+password)
    file.close()

def getUsernames(usernameDict):
    for x in range(len(usernameDict)):
        print(str(x+1) + ": " + usernameDict[str(x+1)][0])

    rangeOfUsernames = []
    for i in range(len(usernameDict)):
        rangeOfUsernames.append(str(i+1))
    return rangeOfUsernames

def getInput(usernameDict):

    print("\n--------------------------------------------------------------------------\nPleast input a username for a gmail account, or select a pre-existing saved account (choose number)\n")
    print("Or enter 'exit' to quit the program\n\n")

    rangeOfUsernames = getUsernames(usernameDict)

    optionEntered = False

    while not optionEntered:
        login = input("\n:")
        if login.lower() == "exit":
            print("\nThank you for using the application!")
            optionEntered = True
            break
        elif login in rangeOfUsernames:
            print("\nYou have selected: " + usernameDict[login][0] + "\n")
            system('clear')
            print(".\n.\nConnecting to email\n.\n.")
            try:
                connectToEmail(usernameDict[login][0], usernameDict[login][1])
            except:
                print("\n################################\nThere was an error!\n\nEither the username/email was incorrect or your gmail account doesn't have permissions for Less Secure App Access.\n################################\n")
            stayOnApp = input("\nWould you like to access a difference email (Y/N)?")
            print("\n")
            if stayOnApp.lower() == "n":
                print("\nThank you for using the application!")
                optionEntered = True
                break
            else:
                system('clear')
                getUsernames(usernameDict)
        elif "@" in login:
            save = input("\nWould you like to save this email (Y/N)?")
            # password = input("Please enter the password for this email: ")
            password = getpass(prompt='Please enter the password for this email: ')
            system('clear')
            if save.lower() == "y":
                newEntry(login, password)
            print(".\n.\nConnecting to email\n.\n.")
            try:
                connectToEmail(login, password)
            except:
                print("\n################################\nThere was an error!\n\nEither the username/email was incorrect or your gmail account doesn't have permissions for Less Secure App Access.\n################################\n")
            stayOnApp = input("Would you like to access a difference email (Y/N)?")
            print("\n")
            if stayOnApp.lower() == "n":
                print("\nThank you for using the application!")
                optionEntered = True
                break
            else:
                system('clear')
                getUsernames(usernameDict)
        else:
            print("\nInvalid entry, please try again.")

def connectToEmail(login, password):
    
    #login using credentials
    mail.login(login, password)

    # connect to inbox
    mail.select("inbox")

    # sifts through inbox and returns list of unread emails
    unreadList = mail.search(None,'UnSeen')
    unreadAmount = unreadList[1][0]

    # convert list of unread emails from bytes to string
    unreadAmount = unreadAmount.decode()

    # split the string into a list of all of the unread emails
    unreadEmails = str.split(unreadAmount)

    # establish a counter and count all unread emails
    unreadCount = 0
    for email in unreadEmails:
        unreadCount += 1

    # print final count
    print("The total amount of unread emails in " + login + " is:\n\n" + str(unreadCount))

    return

if __name__ == "__main__":
    usernames = retrieveSaved()
    getInput(usernames)