import datetime


# Lists
actions = ['New Entry', 'Delete Entry', 'Log Out', 'Read Entry']
journal_entry_titles = []
journal_entry_list = []

# Element Storage
user_state = "Logged Out"
username = ""
user_action = ""
journal_entry = ""
delete_journal_entry = ""
read_journal_entry = ""


def log_in():
        
        user = input("Are you a new user here?   ")
        global user_state

        if user == 'no' or 'yes':
                username = input("Please enter a new username here...")
                print(username)
                user_state = 'Logged in'
        else:
                print("Please enter your username here")
                print(username)
                user_state = 'Logged in'


def new_journal_entry():
        user_state = 'journal_entry'
        print(user_state)
        new_journal = input("Please enter a title")                                
        journal_entry_titles.append(new_journal)
        print(journal_entry_titles[-1])
        journal_entry = input("Please write your journal entry here...")
        journal_entry_list.append(journal_entry)

def read_journal():
        user_state = 'read_journal_entry'
        print(user_state)
        print("Which journal entry would you like to read?")
        print(journal_entry_titles)
        read_journal_entry = input("")
        if read_journal_entry == journal_entry_titles[0]:
                print(journal_entry_list[0])
        elif read_journal_entry == journal_entry_titles[1]:
                print(journal_entry_list[1])
        elif read_journal_entry == journal_entry_titles[1]:
                print(journal_entry_list[1])
        

def journal_delete():
        print("Which journal entry would you like to delete?")
        print(journal_entry_titles)
        delete_journal_entry = input("")
        if delete_journal_entry == journal_entry_titles[0]:
                del journal_entry_titles[0]
                del journal_entry_list[0]
        elif delete_journal_entry == journal_entry_titles[1]:
                del journal_entry_titles[1]
                del journal_entry_list[1]
        elif delete_journal_entry == journal_entry_titles[2]:
                del journal_entry_titles[2]
                del journal_entry_list[2]

while user_state == 'Logged Out':
        print("Welcome to your personal journal")

        log_in()

        while user_state == 'Logged in':
                print('What would you like to do?', actions)
                user_action = input('Please choose one of the options from above....')
                if user_action == actions[0]:
                        new_journal_entry()
                
                if user_action == actions[1] and journal_entry_titles != []:
                        journal_delete()

                if user_action == actions[3] and journal_entry_titles != []:
                        read_journal()
        
                if user_action == actions[2]:
                        user_state = 'Logged Out'
                
                

