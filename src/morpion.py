# Import des bibliotheques necessaires au programme
from copy import deepcopy
from random import shuffle
from discord import Embed

"""
Class MorpionPlayer - Gestion du joueur
"""


class MorpionPlayer:

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name
        self.id = -1

    async def play(self, game, completion):
        completion((0, 0))


"""
Class MorpionComputer - Implementation de MorpionPlayer pour l'ordinateur
"""


class MorpionComputer(MorpionPlayer):

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name
        self.id = -2

    async def play(self, game, completion):
        (x, y) = self.bestMove(game, game.table, game.size, self.sign)[0]
        await completion(x, y)

    # Selectionner la meilleure possibilitee de jeu
    def bestMove(self, game, table, size, sign):
        # On recupere le sign de l'adverse pour nos calculs
        other = ("X" if sign == "O" else "O")
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()

        # On parcours le tableau pour classer chaque possibilitee
        for x in range(size):
            for y in range(size):
                # Si la case est disponible
                if table[x][y] == "*":
                    # On fait une copie du tableau dans laquelle on joue
                    copy = deepcopy(table)
                    copy[x][y] = sign
                    # Et on recupere le resultat
                    win = game.win(copy)

                    # Si le tableau est plein et que personne ne gagne, on le grade 0
                    if win == "*" and game.full(copy):
                        score = 0
                    # Si il permet de gagner, on le grade 1
                    elif win == sign:
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - self.bestMove(game, copy, size, other)[1]
                    result = ((x, y), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajout dans la liste avec les autres et on continue
                    moves.append(result)

        # Une fois tous les coups dans la liste, on les trie par score
        shuffle(moves)
        moves.sort(key=lambda move: move[1], reverse=True)
        # Et on joue le meilleur
        return moves[0]


"""
Class MorpionHuman - Implementation de MorpionPlayer pour le joueur
"""


class MorpionHuman(MorpionPlayer):

    async def play(self, game, completion):
        self.completion = completion


"""
Class MorpionGame - Gestion du tableau de jeu
"""


class MorpionGame:

    # Initialisation du tableau de jeu
    def __init__(self, size, player1, player2, ctx):
        self.size = size
        self.table = [["*" for x in range(size)] for y in range(size)]
        self.player1 = player1
        self.player2 = player2
        self.ctx = ctx
        self.current = player1.sign
        self.message = None

    # Deroulement de la partie
    async def nextMove(self):
        # Send first message if needed
        if self.message == None:
            await self.show()

        # Check who wins
        win = self.win(self.table)

        # Check that it's not the end of the game
        if win == "*" and not self.full(self.table):
            # Iterate the players
            for player in [self.player1, self.player2]:
                if player.sign == self.current:
                    # Here the player plays
                    await player.play(self, self.handleNextMove)
                    return

        # The game ended
        self.current = "*"
        await self.show()

    # Traitement du next move
    async def handleNextMove(self, x, y):
        # Set the move
        if self.play(x, y, self.current):
            self.current = self.player2.sign if self.current == self.player1.sign else self.player1.sign

        # Update message
        await self.show()

        # And go to next move
        await self.nextMove()

    # Affichage du tableau
    async def show(self):
        # Generate output
        output = ""

        # Players
        output += self.convertChar(self.player1.sign, -1, -1) + " : **" + self.player1.name + \
            "**\n" + self.convertChar(self.player2.sign, -1, -1) + \
            " : **" + self.player2.name + "**\n\n"

        # Lines
        for y in range(self.size):
            line = ""
            for x in range(self.size):
                line += self.convertChar(self.table[x][y], x, y)
            output += line + "\n"

        # Check for game status
        output += "\n"
        if self.current == "*":
            win = self.win(self.table)
            for player in [self.player1, self.player2]:
                if player.sign == win:
                    output += "Victoire de " + player.name + " !"
                    break
            else:
                output += "Match nul ! (donc Nathan a gagné xD)"
        else:
            output += "Cliquez sur un chiffre pour jouer"

        # Construct embed
        embed = Embed(title="Jeu du Morpion", description=output)

        # Send message
        if self.message == None:
            self.message = await self.ctx.send(embed=embed)
            await self.message.add_reaction("1️⃣")
            await self.message.add_reaction("2️⃣")
            await self.message.add_reaction("3️⃣")
            await self.message.add_reaction("4️⃣")
            await self.message.add_reaction("5️⃣")
            await self.message.add_reaction("6️⃣")
            await self.message.add_reaction("7️⃣")
            await self.message.add_reaction("8️⃣")
            await self.message.add_reaction("9️⃣")
        else:
            await self.message.edit(embed=embed)

        # Clear reaction if game ended
        if self.current == "*" and self.message != None:
            await self.message.clear_reactions()

    # Convertir le caractère en emoji discord
    def convertChar(self, sign, x, y):
        if sign == "X":
            return ":x:"
        elif sign == "O":
            return ":o:"
        elif x == 0 and y == 0:
            return ":one:"
        elif x == 1 and y == 0:
            return ":two:"
        elif x == 2 and y == 0:
            return ":three:"
        elif x == 0 and y == 1:
            return ":four:"
        elif x == 1 and y == 1:
            return ":five:"
        elif x == 2 and y == 1:
            return ":six:"
        elif x == 0 and y == 2:
            return ":seven:"
        elif x == 1 and y == 2:
            return ":eight:"
        elif x == 2 and y == 2:
            return ":nine:"

    # Joue sur le joueur en cours selon l'emoji choisi
    async def playFromReaction(self, emoji, user):
        # On init les coordonnées
        (x, y) = (0, 0)

        # On check l'emoji
        if emoji == "1️⃣":
            (x, y) = (0, 0)
        elif emoji == "2️⃣":
            (x, y) = (1, 0)
        elif emoji == "3️⃣":
            (x, y) = (2, 0)
        elif emoji == "4️⃣":
            (x, y) = (0, 1)
        elif emoji == "5️⃣":
            (x, y) = (1, 1)
        elif emoji == "6️⃣":
            (x, y) = (2, 1)
        elif emoji == "7️⃣":
            (x, y) = (0, 2)
        elif emoji == "8️⃣":
            (x, y) = (1, 2)
        elif emoji == "9️⃣":
            (x, y) = (2, 2)
        else:
            return

        # On iterate les joueurs pour jouer
        for player in [self.player1, self.player2]:
            if player.sign == self.current and (player.id == -1 or player.id == user.id):
                player.id = user.id
                player.name = user.display_name
                await player.completion(x, y)
                return

    # Change la valeur d'une case si libre
    def play(self, x, y, player):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and self.table[x][y] == "*":
            self.table[x][y] = player
            return True
        return False

    # Regarde si un joueur a gagne
    def win(self, table):
        for i in range(self.size):
            # Check if a line has a winner
            line = self.line(table, i)
            if line != "*":
                return line

            # Check if a row has a winner
            col = self.col(table, i)
            if col != "*":
                return col

        for i in range(2):
            # Check is a dia has a winner
            dia = self.dia(table, i)
            if dia != "*":
                return dia

        return "*"

    # Verifie une ligne
    def line(self, table, y):
        player = table[0][y]
        changed = False

        for x in range(self.size):
            if table[x][y] != player:
                changed = True

        if changed:
            return "*"

        return player

    # Verifie une colonne
    def col(self, table, x):
        player = table[x][0]
        changed = False

        for y in range(self.size):
            if table[x][y] != player:
                changed = True

        if changed:
            return "*"

        return player

    # Verifie une diagonale
    def dia(self, table, d):
        i = (0 if d == 0 else self.size-1)
        player = table[i][0]
        changed = False

        for x in range(self.size):
            i = (x if d == 0 else self.size-1-x)
            if table[i][x] != player:
                changed = True

        if changed:
            return "*"

        return player

    def full(self, table):
        for x in range(self.size):
            for y in range(self.size):
                if table[x][y] == "*":
                    return False
        return True
