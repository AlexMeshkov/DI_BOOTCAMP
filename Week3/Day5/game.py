import random


class Game:
    lst_choice = ["rock", "papper", "scissors"]

    def __init__(self):
        self.result = {"draw": 0, "win": 0, "loss": 0}

    @staticmethod
    def get_user_item():
        item = (
            input("Please select an item ((r)rock, (p)paper, (s)scissors)")
            .strip()
            .lower[0]
        )
        print
        return item

    @staticmethod
    def get_computer_item():
        comp_item = random.choice(["r", "p", "s"])
        return comp_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.result["draw"] += 1
        elif (
            (user_item == "r" and computer_item == "s")
            or (user_item == "s" and computer_item == "p")
            or (user_item == "p" and computer_item == "r")
        ):
            self.result["win"] += 1
        else:
            self.result["lost"] += 1
        return self.result

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        results = self.get_game_result(user, computer)

        # - print the output sentence
        # - return the results


new_game = Game()
new_game.play()
