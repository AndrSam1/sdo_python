# This program is the final project for the course "Programming in Python".
# The program's functionality includes reading a file (a text file located in the program folder - task_file.txt)'
# containing information about employees, generating email addresses for employees based on this data, generating
# secure passwords for email login, adding information to this file, and overwriting it.

import random
import string
import re

# Function for creating email addresses

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


# Function for generating passwords

def generate_password(letters=8, digits=2, punctuation=2):
    password = list(random.choice(string.ascii_letters) for i in range(letters))
    password += list(random.choice(string.digits) for i in range(digits))
    password += list(random.choice('!#$%^&*()_-+=[]{}\|/?><.') for i in range(punctuation))
    password = random.sample(password, len(password))
    return ''.join(password)

# Main program

print ('Start program'.center(100, '='))

file = open('task_file.txt')
lst = list()
for line in file:
    line = line.rstrip()
    lst.append(line.split(','))

print('Total lines in input file:', len(lst)-1)

result_lst = list()
error_lst = list()
for i in range(1, len(lst)):
    if re.match(r'^[A-Z]{1}[a-z]{2,}', lst[i][1].strip()) \
            and re.match(r'^[A-Z]{1}[a-z]{2,}', lst[i][2].strip()) \
            and len(lst[i][3].strip()) >= 7 \
            and not re.match(r'^[0]{1,}', lst[i][3].strip()):
        result_lst.append([lst[i][1].strip(),
                           lst[i][2].strip(),
                           lst[i][3].strip(),
                           lst[i][4].strip()])
    else:
        error_lst.append([lst[i][1].strip(),
                          lst[i][2].strip(),
                          lst[i][3].strip(),
                          lst[i][4].strip()])

print('Total correct lines:', len(result_lst))
print('Total lines with errors:', len(error_lst))

e_mail_lst = email_gen(result_lst)

# Write a file with the correct data, add e-mail and password

print ('Write to output files'.center(100, '='))

file = open('output.txt', 'wt')
print("EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY", file=file)
for i in range(len(result_lst)):
    print(f'{e_mail_lst[i]}, '
          f'{generate_password()}, '
          f'{result_lst[i][0]}, '
          f'{result_lst[i][1]}, '
          f'{result_lst[i][2]}, '
          f'{result_lst[i][3]}',
          file=file)
file.close()
print('Total write lines to file output.txt:', i + 1)

file = open('errors.txt', 'wt')
print("EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY", file=file)
for i in range(len(error_lst)):
    print(f', , {error_lst[i][0]}, '
          f'{error_lst[i][1]}, '
          f'{error_lst[i][2]}, '
          f'{error_lst[i][3]}',
          file=file)
file.close()
print('Total write lines to file error.txt:', i + 1)

print('End program'.center(100, '='))