# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, startingroom):
        self.currentroom = startingroom

    def move(self, direction):
        if getattr(self.currentroom, f'{direction}_to') is not None:
            self.currentroom = getattr(self.currentroom, f'{direction}_to')
            print(
                f'\n~ {self.currentroom.name} ~\n\t{self.currentroom.description}\n')
        else:
            print('\nThere is no room that way!\n')
