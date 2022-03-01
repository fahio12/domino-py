import random

def main():
    # create pieces
    pieces = createPieces()

    # shuffle them
    random.shuffle(pieces)

    # Get input to get num of players (2 or 4)
    playerNum = int(input("Please enter the number of players (2 or 4): "))

    # Create players
    players = []
    for player in range(playerNum):
        name = input(f"Enter player {player+1}'s name: ")
        players.append(Player(name, pieces[:10]))
        del pieces[:10]

    # ACTUAL GAME
    table = []
    end = False
    while(end == False):
        tableStatus = len(table)
        for player in range(playerNum):
            choice = "pass"
            # THIS IF STATEMENT CHECKS IF THE TABLE IS EMPTY SO THAT THE FIRST
            # PLAYER CAN START THE GAME
            # Not ideal to check if table is empty every turn performance-wise
            # but this way offers more concise code.
            if not table:
                print(f"{players[0].name} - pieces: ")
                print(players[0].pieces)
                choice = input(f"{players[0].name} - Choose a starting piece: ")
                print (choice)
                table.append(choice)
                print(table)
                print('-------------------------------------------------------')

                continue

            # Normal turn
            print(table)
            print(f"{players[player].name} - pieces: ")
            print(players[player].pieces)
            print('-------------------------------------------------------')

        if tableStatus == len(table):
            end = True

#Creates a list with all the pieces in the game
def createPieces():
    pieces = []
    for i in range(10):
        for j in range(10):
            pieces.append([i,j])
            for piece in pieces:
                if piece == [j,i] and j != i:
                    pieces.remove(piece)
    return pieces


class Player:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
    def getPieces(self):
        print(self.pieces)



if __name__ == '__main__':
    main()
