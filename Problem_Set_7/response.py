#Valid or invalid mail NOT using re
#Instead using validators
#pip install validator-collection

from validator_collection import validators, checkers, errors

email_add = str(input("What's your email adress? "))
if checkers.is_email(email_add):
    print("Valid")
else:
    print("Invalid")