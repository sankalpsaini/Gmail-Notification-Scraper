# imaplib program to access gmail servers
import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')

# get login and password information from user (can also adapt to get user input)
login = 'sankalp_volunteer@solaralberta.ca'
password = 'seCxo7-repnyn-rogkib'

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
print("The total amount of unread emails in " + login + " is:\n\n" + str(unreadCount) + '\n')