"""
THM Note
TryHackMe Note Creator
----------------------
Coder: Ash Noor (ryn0f1sh)
Site: www.AshNoor.me
Date: Feb/2022

Font: Calvin S
Site: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

Disclaimer:
This is an early version of this tool.
There is no error handling.
Hopefully that will be added in the future.
"""
# Imports
from time import sleep

# Title Function.
def title():
    # Font: Calvin S
    print("""
-----------------------
╔╦╗╦ ╦╔╦╗  ╔╗╔┌─┐┌┬┐┌─┐
 ║ ╠═╣║║║  ║║║│ │ │ ├┤ 
 ╩ ╩ ╩╩ ╩  ╝╚╝└─┘ ┴ └─┘
 -----------------------
    """)

    # Sleep for a couple of seconds.
    sleep(1)

    # Call the THM Notes Function.
    thm_notes_function()

# // --- End of Title Function.



# THM Notes Function.
def thm_notes_function():
    # The Ouput file list
    output_file = []
    # Clear the list
    output_file.clear()

    # Message to the user
    print("\nPlease fill out the following prompts.")
    sleep(1)

    # Room Name
    room_name = input("The Room Name : ")
    # URL
    room_url = input("The Room's Url : ")
    # Number of Tasks
    num_of_tasks = int(input("The number of tasks: "))

    # Setting up the room info
    # Add a couple of blank lines for IPs
    room_info =(
"""
******************
|  - THM Note -  |
******************
Room Name: {0} 
Room URL: {1}
 --//-- 
Attacker IP: 
Room IP:
******************
"""
    ).format(room_name, room_url)

    # Append the Output File list
    output_file.append(room_info)

    # Test print the room info
    #print(room_info)

    # Setting up the number of tasks
    for i in range(num_of_tasks):
        tasks=("""
===============
TASK """+str(i+1)+
"""
------------

===============
""")
        # Append the Output File list.
        output_file.append(tasks)
        #print(tasks)

        """# Test print the Output File list.
        for x in range(len(output_file)):
            print(output_file[x])"""

    # --------------
    # OUTPUT FILE
    # --------------
    # Message to the user
    print("\nYour THM Note is being created.")
    with open(room_name+"_THM_Notes.txt", 'a') as f:
        for x in range(len(output_file)):
            print(output_file[x], file=f)
        f.close()

    # Message to the user
    sleep(2)
    print("Your THM Note is ready.")


    sleep(1)
    # Call the "Again" function.
    again()
# // --- End of THM Notes Function.



# Again Function
def again():
    # To ask the user if they would like to create another note
    answer = input("\nWould you like make another note? [y/n]: ")
    if answer.lower()== 'y':
        # Call the THM notes function
        thm_notes_function()
    else:
        print("\nExiting Program in 3 seconds. \nHappy Hacking.")
        sleep(3)
        exit()
# // --- End of Again Function.



# Function Calls.
if __name__ == '__main__':
    title()