# Import du random
from random import choices
from typing import List, Optional

"""
Définition des classes et des fonctions
Pour ajouter des citations, voir plus bas dans le fichier
"""

# Structure des citations


class Quote:
    """
    L'objet Quote est utilisé pour représenter une citation d'un professeur, ou autre.\n
    Il est composé de plusieurs attributs :
     - text : Cela représente le texte de la citation, qui sera affiché à l'écran, cela doit être un string
     - author : Cela représente l'auteur de la citation, ce sera affiché en dessous du texte de la citation
     - weight : Cela représente la pondération de la citation, ses chances d'être choisie. Valeur si non fourni : 100
    """

    # Initialisation d'une variable de classe, pour définir des poids cumulatifs

    def __init__(self, text: str, author: str, weight: int = 100) -> None:
        # Initialisation de attributs
        self.text = text
        self.author = author
        self.weight = weight

        # Ajout dans les listes, pour pouvoir être choisi par la fonction choices
        quotes.append(self)
        quotesWeight.append(weight)

    def __contains__(self, other: str):
        # On définit le in pour permettre de vérifier l'auteur simplement
        if not isinstance(other, str):
            raise TypeError

        if other.lower() in self.author.lower():
            return True
        return False


global quotesToPull
quotesToPull = []

# Tirage d'une citation
def random_quote(author: Optional[str] = None) -> Quote:
    """ Tire une citation au hasard dans la liste pondéré des citations """
    # Si un auteur particulier est demandé
    if author != None:
        # On se met dans un try pour éviter les erreurs de l'entrée utilisateur
        try:
            # On créer deux nouvelles listes, contenant les quotes et leurs poids correspondant à l'auteur demandé
            newQuotesToPull = [i for i in quotes if author in i]
            newQuotesWeight = [i.weight for i in newQuotesToPull]

            # On donne une citation aléatoire de la nouvelle liste
            return choices(newQuotesToPull, weights=newQuotesWeight, k=1)[0]

        except:
            # Si il y a un problème, on ignore et fait comme si aucun argument n'avait été passé
            pass

    # Cas général
    # On définit la liste comme global, ainsi elle sera maintenue entre plusieurs appels de la fonction
    global quotesToPull

    # On regarde si la liste contient des quotes
    if quotesToPull == []:
        # Si la liste est vide, on prend 20 éléments de la liste, avec répétition, car on peut pas faire autrement
        quotesToPull = choices(quotes, weights=quotesWeight, k=20)

        # On transforme en set, puis en liste, pour enlever les répétitions
        quotesToPull = list(set(quotesToPull))

    # Puis on return une citation au hasard et l'enlève de la liste
    return quotesToPull.pop()

# Comptage du nombre de citations


def quotes_count():
    return len(quotes)


# Création des listes des citations
quotes: List[Quote] = []
quotesWeight: List[int] = []


"""
Definition des citations
"""

# Guide pour pondérer les citations :
# Vide si c'est une citation commune/emblématique d'un prof
# 70 si elle vient d'un philosophe/auteur ...
# 50 si elle vient d'un élève
# 30 si c'est plus une blague qu'autre chose


# Citations de Vincent
Quote("C'est moins simple.", "Vincent V.K.")
Quote("C'est moins marrant.", "Vincent V.K.")
Quote("On va pas être copain.", "Vincent V.K.")
Quote("C'est presque évident.", "Vincent V.K.")
Quote("Je ressemble plus à une vache que vous à des scientifiques.", "Vincent V.K.")
Quote("C'est **tragique !**", "Vincent V.K.")
Quote("Ça, c'est tout à fait remarquable.", "Vincent V.K.")
Quote("Pas de regrets, vous avez pas le niveau !", "Vincent V.K.")
Quote("Oui, bien sûr!", "Vincent V.K.")
Quote("N'utilisez pas de blanco, n'utilisez pas de gomme. Encadrez vos erreurs !", "Vincent V.K.")
Quote("Bon les enfants, c'est l'heure !", "Vincent V.K.")
Quote("Tout le reste, c'est une question d'échelle.", "Vincent V.K.")
Quote("Ce qui est un signe de maladie mentale.", "Vincent V.K.")
Quote("Pôle Emploi va vous recevoir... vous aurez pas de travail, mais il va vous recevoir !", "Vincent V.K.")
Quote("Vous tapez sur des clous, vous vous tapez une fois sur le doigt.\nÇa vous a plu, du coup vous allez le refaire !", "Vincent V.K.")
Quote("Ça va de pas beaucoup, à pas mal", "Vincent V.K.")
Quote("C'est ça que ça veut dire !", "Vincent V.K.")
Quote("Si vous aimez pas la formule du binôme, et bah on vous emmerde !", "Vincent V.K.")
Quote("Ça te servira jusqu'à la fin de tes jours en prépa... qui ne seront peut-être pas longs.", "Vincent V.K.")
Quote("L'honnêteté intellectuelle, bah c'est l'inverse de la malhonnêteté intellectuelle.", "Vincent V.K.")
Quote("On est ce qu'on appelle un truand.", "Vincent V.K.")
Quote("Relis ton cours !", "Vincent V.K.")
Quote("Si j'entends dire que quelqu'un roule en vélo a contre sens sur l'autoroute je penserais à vous", "Vincent V.K.")
Quote("Comme disait Oliver Véran à l'assemblée hier soir, vous pouvez sortir", "Vincent V.K.")
Quote("Je préfère la trigo que les courges", "Vincent V.K.")
Quote("Si tu penses que tu es en vacances, penses aussi à ce que tu feras plus tard", "Vincent V.K.")
Quote("Si vous confondez des nombres avec des fonctions, vous confondez tous", "Vincent V.K.")
Quote("Si vous confondez les nombres et les fonctions, c'est comme si vous confondiez une voiture avec de l'argent", "Vincent V.K.")
Quote("En maths, il n'y a rien qui existe. C'est virtuel", "Vincent V.K.")
Quote("En maths tout se dessine", "Vincent V.K.")
Quote("Quand on est feignant, on est puni", "Vincent V.K.")
Quote("A mon age je suis encore un con", "Vincent V.K.")
Quote("Faites comme moi, soyez un jeune con, puis un moins jeune con, puis... un vieux con", "Vincent V.K.")
Quote("Autant dire que vous faites n'importe quoi", "Vincent V.K.")
Quote("Menteur !", "Vincent V.K.")
Quote("On va être de grands amis dans l'avenir... Une très longue amitié !", "Vincent V.K.")
Quote("J'ai besoin d'un rendez-vous chez l'ophtalmo", "Vincent V.K.")
Quote("Si vous savez calculer une dérivée, vous savez calculer une primitive.", "Vincent V.K.")
Quote("Une primite", "Vincent V.K.")
Quote("C'est presque du terrorisme de mettre de la colle", "Vincent V.K.")
Quote("T'arrêtes de parler !", "Vincent V.K.")
Quote("C'est moi qui vait me faire engueuler à crier comme ça", "Vincent V.K.")
Quote("Ouf !", "Vincent V.K.")
Quote("C'est une perte de temps et d'énergie... Non c'est bien !", "Vincent V.K.")
Quote("C'est toujours des filles qui gloussent", "Vincent V.K.")
Quote("Vous me trouvez sexiste mais c'est la vérité", "Vincent V.K.")
Quote("Ah ça y est j'ai attrapé le Covid !", "Vincent V.K.")
Quote("Il fait chier lui ! Il arrive en retard et il regarde son téléphone", "Vincent V.K.")
Quote("Ça se fait en... assez vite", "Vincent V.K.")
Quote("Ça c'est connu depuis belle lurette", "Vincent V.K.")
Quote("Que vous soyez pas sérieux, j'en doute pas une seconde, j'avais remarqué", "Vincent V.K.")
Quote("Y'avait ça dans votre interro... y'en a qui connaissaient pas vraiment", "Vincent V.K.")
Quote("Vous allez mourir du Covid si je ferme la fenêtre. C'est à partir de -20°C qu'on meurt de froid", "Vincent V.K.")
Quote("Demandez un rendez-vous à la proviseur, dites lui que je suis un sadique", "Vincent V.K.")
Quote("OH ! J'ai déjà vu cette énormité", "Vincent V.K.")
Quote("Vous croyez qu'il y a des fantômes dans ce lycée ?", "Vincent V.K.")
Quote("On ne peut plus rien pour vous", "Vincent V.K.")
Quote("On réfléchit pas quand c'est pas nécessaire", "Vincent V.K.")
Quote("C'est l'auto confinement : on reste confiné dans sa voiture", "Vincent V.K.")
Quote("1 + 1 = 0", "Vincent V.K.")
Quote("Je vous souhaite bien du courage ! _tape du pied_", "Vincent V.K.")


# Citations de Stefano
Quote("Le cahier de prépa est à jour.", "Stefano S.")
Quote("Reviens dans une heure.", "Stefano S.")
Quote("Ne seront lues que les réponses dont les __résultats ou mots importants sont ENCADRÉS__, et dont on a vérifié l'__HOMOGÉNÉITÉ__.", "Stefano S.")
Quote("On connait une tension, on cherche une tension.", "Stefano S.")
Quote("On passe au plat de résistance ?", "Stefano S.")
Quote("Les notes, on s'en fout ! Si tu veux, je te mets un 20.", "Stefano S.")
Quote("Il y a ampère à gauche et il y a ampère à droite.", "Stefano S.")
Quote("Là la tension elle fluctue donc c'est pas facile.", "Stefano S.")
Quote("Quelle horreur !", "Stefano S.")
Quote("On ne peut pas faire de physique sans schéma.", "Stefano S.")
Quote("Non, ça sonne à 13h05.", "Stefano S.")
Quote("Une loi d'Ohm sans schéma est forcément fausse, même si elle est juste.", "Stefano S.")
Quote("En physique, on a tous les droits !", "Stefano S.")
Quote("Là, j'ai attendu mille minutes !", "Stefano S.")
Quote("C'est parce que là, je parle du futur...", "Stefano S.")
Quote("C'est parfait, c'est formidable !", "Stefano S.")
Quote("Bon...", "Stefano S.")
Quote("Ça devrait être intuitif", "Stefano S.")
Quote("On va se comporter comme une vraie classe de prépa", "Stefano S.")
Quote("Ça, ça sera l'objet du cours suivant", "Stefano S.")
Quote("Au revoir, bon travail !", "Stefano S.")
Quote("C'est presque plus simple !", "Stefano S.")
Quote("Allez tiens ça fera passer le temps !", "Stefano S.")
Quote("Bon bref ! Tous ces efforts pour arriver à une équation", "Stefano S.")
Quote("C'est pas terrible comme équation !", "Stefano S.")
Quote("On se mouille pas trop quand on écrit ça...", "Stefano S.")
Quote("Je m'en rappelle plus !", "Stefano S.")
Quote("Je viendrai vous fusiller sur le champ !", "Stefano S.")
Quote("Vous récitez ça tous les matins pendant 10 jours et puis c'est bon !", "Stefano S.")
Quote("Revenons à nos moutons", "Stefano S.")
Quote("Vous n'avez pas honte !", "Stefano S.")
Quote("Je vous souhaite bien du plaisir", "Stefano S.")
Quote("Bon bah, écoutez, débrouillez vous !", "Stefano S.")
Quote("L'air est plus visqueux que le vide", "Stefano S.")
Quote("C'est une représentation qu'on utilisera JAMAIS, mais c'est important de la comprendre", "Stefano S.")
Quote("Je fais copier, contrôle-c, puis contrôle-v", "Stefano S.")
Quote("Oh bah non :|", "Stefano S.")
Quote("Si vous dites ça vaut 1, vous allez faire sauter au plafond celui qui vous écoute", "Stefano S.")
Quote("Et le tour est joué !", "Stefano S.")
Quote("Les équa diff on en a marre !", "Stefano S.")
Quote("C'est du calcul mathématique, c'est pas intéressant", "Stefano S.")


# Citations de Baptiste
Quote("Tout seul on va plus vite, ensemble on va plus loin.", "Baptiste H. (proverbe africain)")
Quote("Oh, c'est pas très sympatique ça.", "Baptiste H.")
Quote("Il y a des normes.", "Baptiste H.")
Quote("On s'en fou si on arrive pas à lire, du moment qu'on comprend ce qu'il faut faire !", "Baptiste H.")


# Citations de René
Quote("M. RINGOT, **DEVANT !**", "René L.")
Quote("Il n'y a que des vielles version à la noix de coco !", "René L.")
Quote("Je veux pas d'élèves comme ça, il sait tout faire, je peux pas lui crier dessus !", "René L.")
Quote("Toi, cours jusqu'à la salle des profs et fait moi 15 photocopies du sujet !", "René L.")
Quote("Toi, t'as envie d'aller au tableau ? Bien sûr que tu as envie !", "René L.")
Quote("L'infini n'existe pas.", "René L.")
Quote("À dans plus tard !", "René L.")
Quote("On fait des maths, pas de la choucroute", "René L.")
Quote("bONJOUR cHARLES ON FAIT LE TD DE CE mARDI", "René L.")
Quote("Cordialement", "René L.")
Quote("C'est des vieux shnocks comme moi !", "René L.")
Quote("bboonnjjoouurr lleess aammiiss", "René L.")
Quote("LE CRIBLE D'ERASTOTHENE !", "René L.")
Quote("Entrecôte", "René L.")
Quote("C'est moi qui décide, eh !", "René L.")


# Citations de Claire
Quote("Ok guys!", "Claire T.B.")
Quote("Guys?!", "Claire T.B.")
Quote("Salut, ça va ? Il va comment ton chat ?\nAh bah, c'est un chat effrayé par les concombres !", "Claire T.B.")
Quote("Un panda, c'est pas un raton-laveur.", "Claire T.B.")
Quote("C'est vraiment cette heure là.", "Claire T.B.")
Quote("Le truc, c'est que si il marche sur ses petits *paws*. Sur ses petits pots. Sur ses coussinets.", "Claire T.B.")
Quote("A washing raton.", "Claire T.B.")
Quote("Ça commence mal, ça commence mal !", "Claire T.B.")
Quote("Oh non, ça y est, je vous retrouve !", "Claire T.B.")


# Citations de Benjamin
Quote("ln(2) = 0.69, ça se retient !", "Benjamin D.")


# Citations des khôleurs
Quote("Léo, tu es encore vivant ou tu es en PLS ?", "Christophe B.")


# Citations de Marc (Prof d'Allemand)
Quote("Là on est en 2015, et on va faire le grand saut en 2020 !", "Marc V.T.")


# Citations de philosophes/auteurs
Quote("Quiconque lutte contre des monstres devrait prendre garde, dans le combat, à ne pas devenir monstre lui-même.\n" +
      "Et quant à celui qui scrute le fond de l'abysse, l'abysse le scrute à son tour.", "Friedrich Nietzsche", 70)
Quote("Dieu est mort ! Dieu reste mort ! Et c'est nous qui l'avons tué !\nComment nous consoler, nous les meurtriers des meurtriers ?", "Friedrich Nietzsche", 70)
Quote("Seule deux choses sont infinies, l'univers et la bêtise humaine.\nMais pour l'univers, je n'en ai pas encore la certitude absolue.", "Albert Einstein", 70)
Quote("Maintenant j'ai devenu la Mort, le destructeur de monde.",
      "J. Robert Oppenheimer", 70)  # La faute est authentique à la citation originelle


# Citations des élèves - Note, pas fait pour les insultes, juste pour quand quelqu'un sort quelque chose de mémorable
# De plus, ne rajouter pas vos propres citation, ça ne se fait pas. Si c'était assez mémorable, quelqu'un d'autre le rajoutera à votre place
Quote("Le masque il faut le brancher à un avion.", "Nathan F.", 50)
Quote("Quelle technique ? Mais QUELLE Technique !!?", "Léo I.", 50)
Quote("En plus y a pas de meuf en prepa", "Léo I.", 50)
Quote("J'ai oublié un moins, je suis stupide !", "Emilien G.", 50)
Quote("Heuuuuu", "Valentine C.", 50)
Quote("C'est intéressant quand on sait faire", "Guillaume F.", 50)
Quote("Mollo l'asticot !", "Guillaume F.", 50)
Quote("Cherche pas je suis con", "Guillaume F.", 50)
Quote("Qu'est ce que c'est bien de réfléchir", "Guillaume F.", 50)
Quote("- Vous avez fait la fête ?\n- Oui", "Vincent V.K et Sammy S.A.", 50)
Quote("Je pensais ne pas y arriver, et... je n'y suis pas arrivé", "Emilien G.", 50)


# Citations anonymes
Quote("Tout est relatif, sauf la vodka, qui est absolute !", "Anonyme", 30)


# Citiations diverses
Quote("We can be do, to do. What we want to do!", "François Hollande", 30)
Quote("Yes, **WE CAN!**", "Barrack Obama", 30)
Quote("Ich bin ein Berliner!", "John F. Kennedy", 30)
Quote("Il ne faut jamais croire les citations trouvées sur Internet.", "Albert Einstein", 30)
Quote("01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001", "Bot", 30)
Quote("Les deux machines fonctionnent", "Surveillant", 30)


# Citation du rap français
Quote("Se faire sucer c'est pas tromper", "Damso", 30)
Quote("Je lance des tomates sur les vegans", "Lorenzo", 30)
Quote("Lunettes sur le nez s'essaye de passer incognito", "Bosh", 30)
Quote("Basique Simple, Simple basique, Vous n'avez pas les bases", "Orelsan", 30)
Quote("Tout va bien... Petit tout va bien", "Orelsan", 30)
Quote("Faut pas se prendre pour ce que l'on est pas. Nous même on ne se connait pas", "Nekfeu", 30)
Quote("En voilà une drôle de question ?", "Roméo Elvis", 30)
Quote("Un pied dans les flammes, un autre dans la glace... Seduit pas les extrêmes... J'ai trouvé ma place", "Lomepal", 30)