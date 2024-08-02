#-------------------------------------
# Reading in the passwords
#-------------------------------------

# Import the CSV module
import csv

# Import the JSON module
import json

# Create a list of users whose passwords have been compromised
compromised_users = []

# Open passwords.csv
with open('passwords.csv') as password_file:
    # Parse the file
    password_csv = csv.DictReader(password_file)
    # Iterate through each of the lines in the CSV
    for password_row in password_csv:
         # Print username of the person whose password was compromised
         # print(password_row['Username'])
         # Add each username to compromised_users
         compromised_users.append(password_row['Username'])

# Open compromised_users.txt in write-mode
with open('compromised_users.txt', 'w') as compromised_user_file:
     # Iterate over each of the compromised users
     for compromised_user in compromised_user_file:
          # Write the username of each compromised_user in compromised_users to compromised_user_file
          compromised_user_file.write(compromised_user)

#-------------------------------------
# Notifying the Boss
#-------------------------------------

# Open a new JSON file in write-mode
with open('boss_message.json', 'w') as boss_message:
    # Create a boss_message_dict dictionary
    boss_message_dict = {
         "Recipient": "The Boss", 
         "Message": "Mission Success"
    }
    # Write out boss_message_dict to boss_message
    json.dump(boss_message_dict, boss_message)

#-------------------------------------
# Scrambling the Password
#-------------------------------------

# Open new_passwords.csv in write-mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
    # Save signature as multiline string
    slash_null_sig = '''
     _  _     ___   __  ____             
    / )( \   / __) /  \(_  _)            
    ) \/ (  ( (_ \(  O ) )(              
    \____/   \___/ \__/ (__)             
     _  _   __    ___  __ _  ____  ____  
    / )( \ / _\  / __)(  / )(  __)(    \ 
    ) __ (/    \( (__  )  (  ) _)  ) D ( 
    \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
            ____  __     __   ____  _  _ 
     ___   / ___)(  )   / _\ / ___)/ )( \
    (___)  \___ \/ (_/\/    \\___ \) __ (
           (____/\____/\_/\_/(____/\_)(_/
     __ _  _  _  __    __                
    (  ( \/ )( \(  )  (  )               
    /    /) \/ (/ (_/\/ (_/\             
    \_)__)\____/\____/\____/
    '''
    # Write the signature to new_passwords_obj
    new_passwords_obj.write(slash_null_sig)