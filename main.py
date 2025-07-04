import random
from tkinter import *
from tkinter import ttk

root = Tk()

# root window title and dimension
root.title("Sun Bear Trivia")
# Set geometry(widthxheight)
root.geometry('550x300')

var_1= StringVar()
lbl_1 = Label(root, relief="solid", textvariable=var_1)
lbl_1.grid(columnspan=4, row=1)

player_count=StringVar()
lbl_2 = Label(root)
lbl_2.pack()

m_display= StringVar()
lbl_3 = Label(root, relief="solid")
lbl_3.grid(columnspan=4, row=3)

a = [2,3,4]

# Combobox  
cb = ttk.Combobox(root, values=a)
cb.set("1")
cb.grid(row=2, column=3)

# set menu to display selected number and update player_count
def show():
    menu.config(text=cb.get())
    #player_count.set(cb)
    #make_player_roster()


# Button to display selection  
Button(root, text="Please select number of players", command=show).pack()

# Label to show selected value  
menu = Label(root, text=" ")
menu.pack()

player_roster = []
final_scores = []

def make_player(num):
    player = Player(num)
    display_txt = "Player:"+player.number
    m_display.set(display_txt)
   # player.name = input("enter your name: ")

    return [player.name, player.score]

def make_player_roster():
    for i in range(int(player_count)):
        player_roster.append(make_player(i + 1))




class Player:
    def __init__(self, number):
        self.number = number
        self.score = 0
        self.name = None



var_1.set("Welcome to the Greatest Sun Bear Trivia Game You've Ever Played!")
player_count = input("Please enter number of players: ")
while True:
    if int(player_count) > 4 or int(player_count) < 1:
        print("\nPlease choose between 1 and 4 players")
        continue

    player_roster = []
    final_scores = []

    def make_player(num):
        player = Player(num)
        print("Player", player.number)
        player.name = input("enter your name: ")

        return [player.name, player.score]

    def make_player_roster():
        for i in range(int(player_count)):
            player_roster.append(make_player(i + 1))

    def take_turn():
        for i in range(len(player_roster)):
            print("\nIt's " + player_roster[i][0] + "'s turn")
            print("\n"+player_roster[i][0] +
                  " has a score of:", player_roster[i][1])
            print(player_roster[i][0] + "'s question is:")
            q1 = random.choice(question_keys_list)
            q1_list = question_dictionary[q1]
            q1_list_copy = q1_list[:]
            random.shuffle(q1_list_copy)
            print("\n" + q1)
            for a in q1_list_copy:
                print(1 + q1_list_copy.index(a), a)
            answer_index = int(
                input("Select the number next to the correct answer: ")) - 1
            answer_item = q1_list_copy[answer_index]
            if q1_list.index(answer_item) == 0:
                print("\nWowza you know a lot about sun bears!")
                player_roster[i][1] += 1
            else:
                print("\nOofta better luck next time!")
            print(player_roster[i][0],
                  "has a score of:", player_roster[i][1])

    def end_game():

        for player in player_roster:
            final_scores.append(player[1])
        largest_num = max(final_scores)

        def has_duplicates(my_list, check_val):
            count = 0
            for item in my_list:
                if item == check_val:
                    count += 1
                    if count > 1:
                        return True
            return False

        if has_duplicates(final_scores, largest_num) == True:
            print("\nIt's a tie!")
            return

        windex = final_scores.index(largest_num)
        winner = player_roster[windex][0]
        if len(player_roster) > 1:
            print("\n"+winner, "is the winner!")


    make_player_roster()
    take_turn()
    take_turn()
    take_turn()
    end_game()
    print("Thanks for playing!")
    again = input("\nEnter 1 to play again, Enter 2 to quit: ")
    if again == "1":
        continue
    else:
        break
# Execute Tkinter
root.mainloop()