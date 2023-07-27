class Game:
    # lst_choice = ["self", "rock", "papper", "scissors"]
    @staticmethod
    def get_user_item():
        item = (
            input("Please select an item ((r)rock, (p)paper, (s)scissors)")
            .strip()
            .lower[0]
        )

    return item
