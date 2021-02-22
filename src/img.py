# Import des libs
from PIL import Image, ImageDraw, ImageFont
from quotes import random_quote
from random import choice

# Couleurs de background disponibles
colors = ["#34CCDB", "#2ECC71", "#9B98B6", "#34495E", "#E67E22", "#E74C3C"]

# Définition d'une création d'image
def generate_image():
    # On prend une citation
    quote = random_quote()

    # Création d'une image
    width = 2560
    height = 1600
    img = Image.new("RGB", (width, height), choice(colors))

    # On prépare le dessin
    d = ImageDraw.Draw(img)

    # On filtre le texte pour ajouter des retours à la ligne
    newText = ""
    sinceNL = 0
    for c in quote.text:
        newText += c
        sinceNL += 1
        if sinceNL >= 30 and c == ' ':
            newText += "\n"
            sinceNL = 0

    # Citation
    font1 = ImageFont.truetype("fonts/Arial.ttf", 120)
    tw, th = d.textsize(newText, font=font1)
    d.text(((width-tw)//2, height//2 - th), newText, font=font1)

    # Auteur
    font2 = ImageFont.truetype("fonts/Arial.ttf", 90)
    tw, th = d.textsize(quote.author, font=font2)
    d.text(((width-tw)//2, height-(height//4)), quote.author, font=font2)

    # On save l'image
    img.save("wallpaper.jpg")
