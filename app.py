from datetime import datetime


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



def log_in():
        
        user = input("Are you a new user here? yes/no ---  ")
        print("--------------------------------------------------")
        global user_state
        global username
        
        if user == 'yes':
                username = input("Please enter a new username here...")
                print(username)
                user_state = 'Logged in'
        elif user == 'no':
                print("Please enter your username here.   ")
                print(username)
                user_state = 'Logged in'
        else:
                print("Please enter a yes or no response.")
                print("--------------------------------------------------")

def new_journal_entry():
        user_state = 'journal_entry'
        print("--------------------------------------------------")
        new_journal = input("Please enter a title   ")                                
        journal_entry_titles.append(new_journal)
        print(journal_entry_titles[-1])
        print("Please write your journal entry here...")
        journal_entry = input("")
        journal_entry_list.append(journal_entry)

def read_journal():
        user_state = 'read_journal_entry'
        print("--------------------------------------------------")
        print("Which journal entry would you like to read?")
        print(journal_entry_titles)
        i = input("")
        e = journal_entry_titles.index(i)

        for x in journal_entry_titles:
                if x == e:
                        break
                print("--------------------------------------------------")
                print(journal_entry_titles[e])
                print(journal_entry_list[e])
                break

def journal_delete():
        print("--------------------------------------------------")
        print("Which journal entry would you like to delete?")
        print(journal_entry_titles)
        i = input("")
        e = journal_entry_titles.index(i)

        for x in journal_entry_titles:
                if x == e:
                        break
                del journal_entry_titles[e]
                del journal_entry_list[e]
                break  

while user_state == 'Logged Out':
        print("--------------------------------------------------")
        print("Welcome to your personal journal")
        print("--------------------------------------------------")

        log_in()

        while user_state == 'Logged in':
                print("--------------------------------------------------")
                print("Currently Logged in as: ", username)
                print("Today's date is: " + datetime.today().strftime('%d-%m-%y'))
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
                
                

