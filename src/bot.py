""" Import des librairies & ressources """

# Import des APIs system
from os import system
from typing import Optional

# Importation de l'API Discord
from discord.ext import commands
from discord import Embed, Game

# On importe nos ressources
from helper import isAlmostEqual
from quotes import random_quote, quiz_quote, quotes_count
from item_chest import generateItem
from clear import clearChannel, emptyChannel
from morpion import MorpionGame, MorpionHuman, MorpionComputer

# Import du random
from random import randint


""" Initialisation du bot """

# On init le bot
bot = commands.Bot(command_prefix='.')


# Quand le bot est pret
@bot.listen()
async def on_ready() -> None:
    # On log la connexion
    print('Logged on as {0}!'.format(bot.user))

    # On update le status
    await bot.change_presence(activity=Game('https://github.com/MPSI1Thuillier/Bot'))


""" Définition des commandes """

#
# Commandes de controles
#

# Commande de ping


@bot.command()
async def ping(ctx) -> None:
    # On répond pong
    await ctx.send('Pong')
    await ctx.message.delete()

# Commande de reboot


@bot.command()
@commands.is_owner()
async def reboot(ctx) -> None:
    # On reboot le bot
    system('sh start.sh')
    await ctx.bot.logout()
    await ctx.message.delete()
    quit()

# Commande de stop


@bot.command()
@commands.is_owner()
async def stop(ctx) -> None:
    # On stop le bot
    await ctx.bot.logout()
    await ctx.message.delete()
    quit()


#
# Commandes de gestion des channels
#

# Commande de clear
@bot.command()
@commands.is_owner()
async def clear(ctx) -> None:
    # On supprime tous les messages de commande et du bot du channel
    await clearChannel(ctx)
    await ctx.message.delete()

# Commande de empty


@bot.command()
async def empty(ctx) -> None:
    # On supprime tous les messages
    await emptyChannel(ctx)
    await ctx.message.delete()


#
# Commandes d'info
#

# Guide de la contribution
@bot.command()
async def contribution(ctx) -> None:
    # On explique comment fonctionne la contribution
    await ctx.send("Pour contribuer au fonctionnement du bot et l'améliorer, rendez vous sur https://github.com/MPSI1Thuillier/Bot")
    await ctx.message.delete()


#
# Commandes de citation
#

# Commande de citation
@bot.command()
async def citation(ctx, arg: Optional[str] = None) -> None:
    # On choisi une citation
    quote = random_quote(arg)

    # On créé un embed
    embed = Embed(title=quote.text)
    embed.set_footer(text=quote.author)

    # On envoit
    await ctx.send(embed=embed)
    await ctx.message.delete()

# Commande pour compter les citations


@bot.command()
async def count(ctx) -> None:
    # On compte les citations
    n = quotes_count()

    # On créé les paramètres de l'équation
    a = randint(1, 20)
    n2 = randint(-10, -1)

    # On créé un embed
    embed = Embed(
        title="J'ai n citations, tel que :",
        description="```" + str(a) + "n² - " + str(a*(n + n2)) +
        "n - " + str(-a*n*n2) + " = 0``````n > 0```"
    )

    # On envoit
    await ctx.send(embed=embed)
    await ctx.message.delete()


#
# Commandes funs
#

# Commande d'item
@bot.command()
async def item(ctx) -> None:
    # On gènere un item et l'envoi
    text = generateItem()
    embed = Embed(title=text[0])
    embed.set_footer(text=text[1])

    await ctx.send(embed=embed)
    await ctx.message.delete()

# Commande de pile ou face


@bot.command()
async def pileface(ctx) -> None:
    # On décide et envoie le résultat
    await ctx.send("Le résulat est : {}".format(["Pile", "Face"][randint(0, 1)]))
    await ctx.message.delete()

# Commande de token


@bot.command()
async def token(ctx) -> None:
    # On envoi le token
    await ctx.send("Le token est : Tm9uLCBsZSB0b2tlbiBuJ2VzdCBwYXMgYWNjZXNzaWJsZSBjb21tZSDDp2E")
    await ctx.message.delete()


#
# Commande de morpion et listen des reactions
#

morpion_games = []

# Commande de morpion


@bot.command()
async def morpion(ctx) -> None:
    # On démarre une partie de morpion
    game = MorpionGame(3, MorpionHuman("O", "Joueur 1"), MorpionHuman("X", "Joueur 2"), ctx)
    morpion_games.append(game)
    await ctx.message.delete()
    await game.nextMove()

# Commande de morpion


@bot.command()
async def morpionbot(ctx) -> None:
    # On démarre une partie de morpion
    game = MorpionGame(3, MorpionHuman("O", "Joueur 1"), MorpionComputer("X", "Ordinateur"), ctx)
    morpion_games.append(game)
    await ctx.message.delete()
    await game.nextMove()


@bot.listen()
async def on_reaction_add(reaction, user) -> None:
    # On check que c'est pas le bot
    if user.bot:
        return

    # On récupère la game liée au message et on joue
    for game in morpion_games:
        if game.message != None and reaction.message.id == game.message.id:
            # On joue avec la réaction
            await game.playFromReaction(reaction.emoji, user)

            # On clear la game si c'est fini
            if game.current == "*":
                morpion_games.remove(game)
                return

#
# Question pour un préparationiste
# Le but : compléter la citation donnée par le bot
#

quiz_games = []

# Commande pour lancer le jeu

@bot.command()
async def questionprepa(ctx):
    # On récupère une citation qui contient une virgule (qui se complète)
    quote = quiz_quote()

    # On coupe à la virgule
    parts = quote.text.split(", ")

    # On créé un embed
    embed = Embed(
        title="Trouver la fin de la citation :",
        description=parts[0] + ", ..."
    )
    embed.set_footer(text=quote.author)

    # On envoit
    await ctx.send(embed=embed)
    await ctx.message.delete()

    # On save la question
    question = (ctx.author.id, quote)
    quiz_games.append(question)

@bot.listen()
async def on_message(message):
    # On regarde si ya une question associée avec l'auteur
    for question in quiz_games:
        if question[0] == message.author.id:
            # On est sur la réponse à notre question
            if isAlmostEqual(message.content, question[1].text.split(", ")[1]):
                # Bonne réponse
                embed = Embed(
                    title="Bonne réponse !!! 👍",
                    description=question[1].text
                )
                embed.set_footer(text=question[1].author)
                await message.channel.send(embed=embed)
            else:
                # Mauvaise réponse
                embed = Embed(
                    title="Mauvaise réponse !!! 👎",
                    description="La citation complète était :\n" + question[1].text
                )
                embed.set_footer(text=question[1].author)
                await message.channel.send(embed=embed)
            
            # On le retire de la liste
            quiz_games.remove(question)

            # On s'arrete
            break
