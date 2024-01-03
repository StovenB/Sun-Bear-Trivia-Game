import random


class Player:
    def __init__(self, number):
        self.number = number
        self.score = 0
        self.name = None


while True:
    print("Welcome to the Greatest Sun Bear Trivia Game You've Ever Played!")
    player_count = input("Please enter number of players: ")
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
                print("\nWowza you know a lot about Sun bears!")
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

    question_dictionary = {"Sun bears are native to what part of the world?": ["South-east Asia", "The Amazon rain forest", "Australia"], "Sun bears have a distinct coloration known as a 'sun patch' located on their": ["Throats/torso", "Back and shoulders", "Ears"], "Sun bears are the smallest species of bear, weighing ______ on average": [
        "60-150 lbs", "200-300 lbs", "20-70 lbs"], "Which statement is false?": ["Sun bears are mainly active at night", "Sun bears spend more time in trees than all other species of bears", "Sun bears are solitary animals"], "Sun bears are most closely related to what kind of bear?": ["Black bears", "Pandas", "Grizzly bears"]}
    question_keys_list = list(question_dictionary.keys())
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
