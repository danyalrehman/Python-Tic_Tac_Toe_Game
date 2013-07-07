class TicTacToe:
    """This class stores the internal state of the
    Tic Tac Toe game, along with the operations that
    are needed to play the game.
    """

    def __init__(self):
        """Initialize the contents of a new Tic Tac Toe game grid.
        """
        self.clear()
        
    def make_move(self, x, y):
        """Make a move in the position specified by the given X and Y
        coordinates. Switch the player after completing this move.
        """
        if x not in range(0, 3) or y not in range(0, 3):
            raise self.InvalidMoveException(x, y)
        if (x, y) in self.grid:
            raise self.InvalidMoveException(x, y)

        self.grid[(x, y)] = self.current_player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def clear(self):
        """Clear the grid for a new game.
        """
        self.grid = {}
        self.current_player = 'X'

    def winner(self):
        """Return the symbol of the player who has won the game
        (either 'X' or 'O'), or None if there's no winner yet.
        A winner is defined as a player with three of their symbols
        in a straight line in the grid.
        """
        result = None
        listofindices = [0, 1, 2]
        # this function takes care of winning if the user completes a row
        for x in listofindices:
            if self.grid.get((x, 0)) == self.grid.get((x, 1))\
            == self.grid.get((x, 2)):
                result = self.grid.get((x, 0)) or result
        # this function takes care of winning if the user completes a column.
        for y in listofindices:
            if self.grid.get((0, y)) == self.grid.get((1, y))\
            == self.grid.get((2, y)):
                result = self.grid.get((0, y)) or result
        # this part of the function will take care of winning by one diagonal.
        if self.grid.get((0, 0)) == self.grid.get((1, 1))\
        == self.grid.get((2, 2)):
            result = self.grid.get((0, 0)) or result
        # this part of the function takes care of winning by the other diagonal
        if self.grid.get((2, 0)) == self.grid.get((1, 1))\
        == self.grid.get((0, 2)):
            result = self.grid.get((2, 0)) or result
        return result

    def play(self):
        """Start a game with the user, printing out the game grid after
        each turn, until the grid is full or one player has three in a row.
        The game automatically alternates player moves between "X" and "O".
        """
        self.clear()
        print 'Welcome to the Tic Tac Toe game!'

        while (len(self.grid) < 9) and self.winner() == None:
            print "It's " + str(self.current_player) + "'s turn."
            y = raw_input('What row would you like to use? ')
            x = raw_input('What column would you like to use? ')
            try:
                self.make_move(int(x), int(y))
            except:
                print self.InvalidMoveException(x, y)
            print self
            winner = self.winner()
        if winner:
            print str(winner) + " is the winner!"
        print 'Thanks for playing!'

    def __str__(self):
        """Return a sting representation of this Tic Tac Toe grid.
        This will be a 3x3 grid of characters, either "X", "O" or " "
        (a space character if the grid position is empty). Each row
        is separated by a newline character in the string that is
        returned to the calling program.
        """
        result = ""
        listofindices = [0, 1, 2]
        for y in listofindices:
            for x in listofindices:
                # look up the tuple that contains the current X and Y
                # coordinates, and if a symbol exists at that location,
                # add that symbol to the final output string.
                if self.grid.get((x, y)):
                    result += self.grid.get((x, y))
                else:
                    result += ' '
            # add a new line at the end of every row.
            result += '\n'
        return result

class InvalidMoveException(Exception):
        """ the function of this class is that if the user
        inputs a number in a space that has already been used
        it raises an error.
        """

        def __init___(self, x, y):
            """ Initializes x and y values.
            """

            self.x = x
            self.y = y

        def __str__(self):
            """Chooses the string to return if the specific
            error comes up.
            """

            return "This position + (" + str(self.x) \
                   + "," + str(self.y) + ") + has already been taken"

# If this module is the main one being executed, then create
# a TicTacToe object and start the game.
if __name__ == "__main__":
    g = TicTacToe()
    g.play()