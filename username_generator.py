def resolve_duplicate(username, usernames_list):
    counter = 0
    while True:
        counter += 1
        new_username = username + str(counter)
        if new_username not in usernames_list:
            return new_username

students = {
    60254: 'John Smith',
    60255: 'Gert Du-Cart',
    60256: 'Sun Po',
    60257:'Bort Woods',
    60258: 'Andrew Butters',
    60259: 'Betty Ho',
    60260: 'Jane Smitt',
    60261: 'Sha Po',
    60262: 'Jane Smith'
    }

usernames_list = []
for key, value in students.items():
    username = value.lower().replace('-', '') # converts name to lower, removes dashes
    firstname_lastname = username.split()
    firstname = firstname_lastname[0][0] # extracting 1st letter of first name
    lastname = firstname_lastname[-1][0:4] # extracting 1st 4 letters of last name
    username = firstname + lastname
    username = username.ljust(5, '0') # using ljust instead of len(), to fill zeros
    if username in usernames_list:
        username = resolve_duplicate(username, usernames_list)
    usernames_list.append(username)

print(usernames_list)
