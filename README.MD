Journal Entry - Terminal Application

Features:

This system will have a very basic log in/log out system, achieved by assigning 'user states' and having the entire code base contained within a while loop. With this, depending on the users state the loop will place the user at a position, creating a logged in and logged out effect. 

Using lists, the user will be able to create a journal entry which will have both a title and written entry. Whilst I cannot store the journal entry in the title, later on in different user menu actions a for loop can be used to index the two lists together and link them for cross functionality. 

Users will also be able to delete their journal entries. Going back to the previously mentioned for loop system to link data from both the journal title and journal entry lists, the user can can select a title of an entry they want to delete and then the cross indexed entry will list will be removed. 

Journal entries will also be readable after being created, simply printing the indexed entries based off what the user requests from the list. 

While all of this is happening, control statements are controlling the flow of the application, to where if it gets to the point where the user selects to log out of the system, the while loop that contains everything will trigger and the whole loop will reset, prompting the user to log in again.



Development Plan

My development plan for the application will simply follow the order of operation of standard use throughout the app. The reason being for this is a lot of the user actions that will be available are based off another function in one way or another. The project application itself should take no longer than two hours, If I can get this lower while presenting a highly functional application that meets the guide spec, I will spend more time investigating further features, however simple yet functional is what I am looking to with this application.

Login / User State system

The first step for development is to get the 'log in' system functioning, as this is going to be the base for the rest of the code. This while loop will serve as the beginning of the code, with everything else contained in the app being further nested inside this system. Ensuring this works from the get go is my first task as once this works, anything contained inside will seemlessly operate as intended with the log in/log out function. The system itself isn't too complex so I would like to get this done in about <20~ minutes.

User Action Menu

The user action will be made up several options stored inside a list that will be presented to the user. Based off what the user inputs, control statements will dictate the next stage of the application based off of any of the following menu options: New Entry, Delete Entry, Read Entry, Log Out. Again this segment of the application is very simple and should take no longer than 20 minutes. 

New Journal Entry

The journal entry whilst simple in its own right and should not take too long to develop is also the next stage where things begin to develop further and ensuring that this is correct is very important as functionality of later options will all be linked to the lists that are created here. Behind this code there is an empty list for two different things, journal titles and entries, the user will be prompted for both things and these lists will be implemented based off of their input. 

Read Journal

This is action is where I expect to have a few potential problems, ensuring that the two lists previously created in the journal entry section, the correct indexes will need to be printed in accordance to what the user has requested. I expect to be using a for loop as this allows direct calling on indexes in created lists, and if I can link the titles and entries list accordingly, this function will operate as intended. The code here will also serve as a good base for the next action.

Delete Entry

As stated in the last step of the development plan, the code base can be reused with some minor modifications. Instead of printing and ammending the list, the list will have whatever index referenced which is entered, removed. Not only the title will be removed but also the entry as well.

Log Out

The log out action is what will close off the while loop created in the first stage. Once this action has been entered, the user state will change to logged out and the whole program will run back to the beginning. 