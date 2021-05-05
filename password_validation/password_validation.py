import getpass

password = getpass.getpass(prompt='What is the password? ')
if password == 'TaNgY':
    print ('Welcome!')
else:
    print ("I don't know you!")