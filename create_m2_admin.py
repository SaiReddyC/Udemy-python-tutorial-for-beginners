#!/usr/bin/python3

""" Create M2 admin user from the command line using an email address as input.
    You need to have pwgen install.
    DEBBase = apt -y install pwgen
    RMPBase = yum -y install pwgen or dnf -y install pwgen.
    >> What is get generated below.

    USERNAME="example.example"
    PASSWORD="Anah8nee0ahgh4se"
    EMAIL="example.example@example.com"
    FIRSTNAME="example"
    LASTNAME="example"
    <<
    Copy this to your server this will import them as variables.
    Then run this command below to create the user.
    >>>>:>
        n98-magerun2.phar admin:user:create  --admin-user=${USERNAME}  --admin-password=${PASSWORD}
          --admin-email=${EMAIL} --admin-firstname=${FIRSTNAME}  --admin-lastname=${LASTNAME}
"""


import os
import sys

try:
    email = sys.argv[1]
except IndexError:
    email = input("Please enter email address : ")

USERNAME = email.split("@")[0]
PASSWORD = os.popen("pwgen -1 16").read().split("\n")[0]
EMAIL = email
FIRSTNAME = USERNAME.split(".")[0]
LASTNAME = USERNAME.split(".")[1]

print("USERNAME=" + '"' + USERNAME + '"')
print("PASSWORD=" + '"' + str(PASSWORD) + '"')
print("EMAIL=" + '"' + EMAIL + '"')
print("FIRSTNAME=" + '"' + FIRSTNAME + '"')
print("LASTNAME=" + '"' + LASTNAME + '"')
