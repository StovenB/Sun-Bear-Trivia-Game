import random
from tkinter import *
from tkinter import ttk
from sys import exit

root = Tk()

# root window title and dimension
root.title("Sun Bear Trivia")
# Set geometry(widthxheight)
root.geometry('600x300')


main_display= StringVar()
main_display.set("Welcome to the Greatest Sun Bear Trivia Game You've Ever Played! \n\n")
lbl_main = Label(root, relief="solid", textvariable=main_display)
lbl_main.place(x=50, y=50, width=500, height=100)

while True:
#---------------drop down menu------------------------------------
    player_count = 1
    a = [1,2,3,4]

# Combobox  
    cb = ttk.Combobox(root, values=a)
    cb.set("select number of players")
    cb.place(x=50,y=160, width=155)



# update player_count
    def select():
        global player_count
        player_count = cb.get()
        make_player_roster(player_count)
        replace_dropdown()


# Button to display selection  
    b_num = Button(root, text="Select", command=select)
    b_num.place(x=215, y=160)

#-----------------------------------------------------------------

#-------------------name entry------------------------------------

    clear_entry= StringVar()
    namer_entry=Entry(root, textvariable=clear_entry)

    name_counter = 0


# replace buttons/fields
    def replace_dropdown():
        display_txt = "Player 1, enter your name"
        main_display.set(display_txt)
        cb.place_forget()
        b_num.place_forget()
        namer_entry.place(x=50,y=160, width=155)
        b_name.place(x=215, y=160)


    def namer(player_count):
        global name_counter
        global player_roster
        name = namer_entry.get()
        clear_entry.set("")
        player_roster[name_counter][0] = name
        name_counter+=1
        if name_counter == player_count:
            main_display.set("")
            replace_namer()
            return
        display_text = "Player "+str(name_counter +1)+ " , enter your name"
        main_display.set(display_text)
    
    

    b_name=Button(text="Enter", command=lambda: namer(int(player_count)))
#-----------------------------------------------------------------

#-------------questions, answer radios, turns, game end-----------

    def replace_namer():
        namer_entry.place_forget()
        b_name.place_forget()
        play_game()

    var = IntVar()

    def take_turn():
            for i in range(len(player_roster)):
                q1 = random.choice(question_keys_list)
                q1_list = question_dictionary[q1]
                q1_list_copy = q1_list[:]
                random.shuffle(q1_list_copy)
                display_text = "It's " + player_roster[i][0] + "'s turn""\n"+player_roster[i][0] +" has a score of: "+ str(player_roster[i][1])+"\n"+player_roster[i][0] + "'s question is:"+"\n" + q1
                main_display.set(display_text)

                v = IntVar(root, 0) 

                one = Radiobutton(root, text=q1_list_copy[0], variable=v, value=0)
                one.place(x=50,y=160)
                two = Radiobutton(root, text=q1_list_copy[1], variable=v, value=1)
                two.place(x=50,y=180)
                three = Radiobutton(root, text=q1_list_copy[2], variable=v, value=2)
                three.place(x=50,y=200)

                b_select = Button(root, text="Select", command=lambda: var.set(1))
                b_next = Button(root, text="Next", command=lambda: var.set(0))
                b_select.place(x=50, y=235)
                b_next.place(x=100, y=235)
                b_select.wait_variable(var)

                answer_index = v.get()
                answer_item = q1_list_copy[answer_index]
                if q1_list.index(answer_item) == 0:
                    main_display.set("Wowza you know a lot about Sun bears!")
                    player_roster[i][1] += 1
                else:
                    main_display.set("Oofta better luck next time!")
            

                b_next.wait_variable(var) 
                one.place_forget() 
                two.place_forget()
                three.place_forget()
                b_next.place_forget()
                b_select.place_forget()



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
        
            windex = final_scores.index(largest_num)
            winner = player_roster[windex][0]

            if has_duplicates(final_scores, largest_num) == True:
                main_display.set("It's a tie!")
            
            elif len(player_roster) > 1:
                display_txt = winner + " is the winner!"
                main_display.set(display_txt)
        
            else:
                main_display.set("I hope you enjoyed learning about Sun Bears!")
            
            b_next = Button(root, text="Next", command=lambda: var.set(0))
            b_next.place(x=100, y=235)
            b_next.wait_variable(var) 
            b_next.place_forget()
            main_display.set("Thanks for playing!\nWould you like to play again?")
        
            
            b_again.place(x=50, y=235)
            b_exit.place(x=170, y=235)
            #b_again.wait_variable(var)

    def again():
        b_again.place_forget()
        b_exit.place_forget()
        for i in range(int(player_count)):
            player_roster[i][1] = 0
        final_scores.clear()
        play_game()

    b_again = Button(root, text="Play Again", command=again)
    b_exit = Button(root, text="Exit", command=root.quit)     
    
    


    def play_game():
        take_turn()
        take_turn()
        take_turn()
        end_game()
   
    
    
#-----------------------------------------------------------------

### Pythonic activity ###
    player_roster = []
    final_scores = []

    def make_player(num):
        player = Player(num)
        return [player.name, player.score]

    def make_player_roster(num):
        for i in range(int(num)):
            player_roster.append(make_player(i + 1))
    



    class Player:
        def __init__(self, number):
            self.number = number
            self.score = 0
            self.name = None

    question_dictionary = {"Sun bears are native to what part of the world?": ["South-east Asia", "The Amazon rain forest", "Australia"], "Sun bears have a distinct coloration known as a 'sun patch' located on their": ["Throats/torso", "Back and shoulders", "Ears"], "Sun bears are the smallest species of bear, weighing ______ on average": [
        "60-150 lbs", "200-300 lbs", "20-70 lbs"], "Which statement is false?": ["Sun bears are mainly active at night", "Sun bears spend more time in trees than all other species of bears", "Sun bears are solitary animals"], "Sun bears are most closely related to what kind of bear?": ["Black bears", "Pandas", "Grizzly bears"]}
    question_keys_list = list(question_dictionary.keys())


    root.mainloop()
    exit(0)