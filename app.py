username = ""
user_state = "Logged Out"
actions = ['New Entry', 'Delete Entry', 'Log Out']
user_action = ""
journal_entry = []
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



while user_state == 'Logged Out':
        print("Welcome to your personal journal")

        log_in()

        while user_state == 'Logged in':
                print('What would you like to do?', actions)
                user_action = input('Please choose one of the options from above....')
                if user_action == actions[0]:
                        new_journal = input('Please enter the date for this entry')                                
                        journal_entry.append(new_journal)
                        print(journal_entry[-1])
                        print(journal_entry)
                elif user_action == actions[2]:
                        user_state = 'Logged Out'
                break
        

