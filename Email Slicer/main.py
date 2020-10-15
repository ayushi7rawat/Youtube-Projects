'''
Email Slicer with Python
Author: Ayushi Rawat
'''

# Get the user's email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@")+1:]

# Format message
res = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display the result message
print(res)