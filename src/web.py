""" Import des librairies & ressources """

# Import de l'API
from quart import Quart
from bot import bot
from os import system



""" Initialisation du serveur web """

# On init l'app
app = Quart(__name__)



""" Définition des endpoints """

# Racine
@app.route('/')
async def home() -> str:
    return 'Coucou la MPSI1'

# Pull
@app.route('/pull', methods=['POST'])
async def pull() -> None:
    # On pull et on reboot le bot
    system('git pull && sh start.sh')
    await bot.logout()
    quit()
    return 'OK'