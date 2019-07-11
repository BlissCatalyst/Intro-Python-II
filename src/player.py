# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, startingroom):
        self.currentroom = startingroom
        self.playeritems = []

    def move(self, direction):
        if getattr(self.currentroom, f'{direction}_to') is not None:
            self.currentroom = getattr(self.currentroom, f'{direction}_to')
            print(
                f'\n~ {self.currentroom.name} ~\n\t{self.currentroom.description}\n')
        else:
            print('\nThere is no room that way!\n')

    def getitem(self, item):
        self.playeritems.append(item)
        print(f'\n\tYou got the {item}!\n')

    def dropitem(self, item):
        self.playeritems.remove(item)
        print(f'\n\tYou dropped the {item}!\n')

    def checkinv(self):
        inv = ', '.join(self.playeritems)
        if inv:
            print(f'\n\t{inv}\n')
        else:
            print('\n\tYou have nothing in your inventory!\n')
