# On importe les librairies
from random import choice, randint
from typing import List, Tuple, Union

# On définit les différents objets
class Stat:
    """
    L'objet Stat est utilisé pour représenter une stat pour un objet.\n
    Il possède plusieurs attributs :
     - name : Définit le nom de la stat
     - type : Définit si la stat est relative (%), flat ou autre
     - modifier: Définit le multiplicateur à appliquer à la stat
     - special : Définit si la stat apparait aléatoirement ou est spécifique à un attibut/matériau
    """
    def __init__(self, name: str, type: str, modifier: float, special: bool = False):
        self.name = name
        self.type = type
        self.modifier = modifier

        if not special:
            stats.append(self)
    
    def __str__(self):
        return self.name
class Type:
    """
    L'objet Type est utilisé pour représenter un type d'objet.\n
    Il possède plusieurs attributs :
     - name : Définit le nom du type
     - stat : Définit quelle stat est attaché au type
     - statModifier: Définit le multiplicateur à appliquer à la stat
     - gender : Définit si l'objet est masculin ou féminin ou pluriel (0 et 2: masculin; 1 et 3: féminin; 2 et 3: pluriel)
    """
    def __init__(self, name: str, stat: Stat, statMod: float, gender: int):
        self.name = name
        self.stat = stat
        self.statMod = statMod
        self.gender = gender

        types.append(self)
    
    def __str__(self):
        return self.name
class Material:
    """
    L'objet Material est utilisé pour représenter un matériau pour un objet.\n
    Il possède plusieurs attributs :
     - name : Définit le nom du matériau
     - stat : Définit quelle stat est attaché au matériau
     - statModifier: Définit le multiplicateur à appliquer à la stat
     - feminine : Définit quel féminin appliquer à l'objet (0: aucun; 1: +e; 2: eux/euse; 3: eur/rice; 4: +le)
     - plural : Définit si l'on doit appliquer le pluriel à l'objet
    """
    def __init__(self, name: str, stat: Stat, quality: int, statMod: float, feminine: int, plural: bool = True):
        self.name = name
        self.stat = stat
        self.quality = quality
        self.statMod = statMod
        self.feminine = feminine
        self.plural = plural

        materials.append(self)
    
    def __str__(self):
        return self.name
class Attribute:
    """
    L'objet Attribute est utilisé pour représenter un attribut pour un objet.\n
    Il possède plusieurs attributs :
     - name : Définit le nom de l'attribut
     - stat : Définit quelle stat est attaché à l'attribut
     - statModifier: Définit le multiplicateur à appliquer à la stat
     - feminine : Définit quel féminin appliquer à l'objet (0: aucun; 1: +e; 2: eux/euse; 3: eur/rice; 4: +le)
     - plural : Définit si l'on doit appliquer le pluriel à l'objet
    """
    def __init__(self, name: str, stat: Stat, qualMod: int, statMod: float, feminine: int, plural: bool = False):
        self.name = name
        self.stat = stat
        self.qualMod = qualMod
        self.statMod = statMod
        self.feminine = feminine
        self.plural = plural

        attributes.append(self)
    
    def __str__(self):
        return self.name
class Quality:
    """
    L'objet Quality est utilisé pour représenter une qualité d'objet, determinant combien de stats il aura.\n
    Il possède plusieurs attributs :
     - name : Définit le nom de la qualité
     - multiplier: Définit le multiplicateur à appliquer aux stats de l'objet
     - totalStats : Définit combien de stats rajoute cette qualité
    """
    def __init__(self, name: str, multiplier: float, totalStats: int):
        self.name = name
        self.multiplier = multiplier
        self.totalStats = totalStats
    
    def __str__(self):
        return self.name

# Listes pour l'indexation
stats: List[Stat] = []
materials: List[Material] = []
types: List[Type] = []
attributes: List[Attribute] = []


# Stats classiques
Attaque = Stat("Attaque", "Dual", 1)
Résistance = Stat("Résistance", "Dual", 1)
Intelligence = Stat("Intelligence", "Dual", 1)
Sagesse = Stat("Sagesse", "Dual", 1)
Concentration = Stat("Concentration", "Dual", 1)
Dextérité = Stat("Dextérité", "Dual", 1.2)
Vitesse = Stat("Vitesse", "Dual", 0.7)
Puissance = Stat("Puissance", "Flat", 0.8)
Durabilité = Stat("Durabilité", "Flat", 1)
Chance = Stat("Chance", "Dual", 1.2)
Agilité = Stat("Agilité", "Dual", 0.4)
Régénération = Stat("Régénération", "Relative", 0.3)
RenvoiDégâts = Stat("Renvoi de dêgats", "Relative", 0.3)
Empoisonement = Stat("Empoisonement", "Relative", 0.4)
Vitalité = Stat("Vitalité", "Dual", 0.6)
Vamprisme = Stat("Vamprisme", "Relative", 0.3)
AptFeu = Stat("Aptitude Feu", "Relative", 1)
AptEau = Stat("Aptitude Eau", "Relative", 1)
AptGlace = Stat("Aptitude Glace", "Relative", 1)
AptAir = Stat("Aptitude Air", "Relative", 1)
AptTerre = Stat("Aptitude Terre", "Relative", 1)
AptLumière = Stat("Aptitude Lumière", "Relative", 1)
AptTénébres = Stat("Aptitude Ténébres", "Relative", 1)
AptFoudre = Stat("Aptitude Foudre", "Relative", 1)
AptTemporelle = Stat("Aptitude Temporelle", "Relative", 1)
AptÉlémentaire = Stat("Aptitude Élémentaire", "Relative", 0.5)
AptDimensionelle = Stat("Aptitude Dimensionelle", "Relative", 0.5)
ArgentRécolté = Stat("Argent Récolté", "Relative", 1.5)
DégâtsCritique = Stat("Dégâts Critiques", "Relative", 1.5)
ChanceCritique = Stat("Chance Critique", "Relative", 0.2)
PénétrationPhysique = Stat("Pénétration Physique", "Relative", 0.3)
PénétrationMagique = Stat("Pénétration Magique", "Relative", 0.3)
Charme = Stat("Charme", "Flat", 0.6)
Précision = Stat("Précision", "Relative", 1.2)
Brulure = Stat("Brûlure", "Relative", 0.3)
Electrocution = Stat("Électrocution", "Relative", 0.4)
Efficacité = Stat("Efficacité", "Relative", 0.6)

# Stats spéciales
DégâtsMortsVivants = Stat("Dêgats contre les morts-vivants", "Relative", 1, True)
PatriotismeAveugle = Stat("Patriotisme Aveugle", "Relative", 1, True)
CrimesGuerre = Stat("Crimes de Guerre", "Flat", 8.8, True)
ContenuPayant = Stat("Contenu Payant", "Relative", 0.6, True)
Triche = Stat("Triche", "Relative", 2, True)
PacteDiable = Stat("Pactes avec le diable", "FixedFlat", 666, True)
Dinousaures = Stat("Dinousaures", "Flat", 7, True)

# Stats systèmes
Null = Stat("Null", "Dual", 0, True) # Utilisé quand aucune stat additionelle est ajoutée
Random = Stat("Random", "Dual", 0, True) # Utilisé pour obtenir une stat aléatoire
Copy = Stat("Copy", "Dual", 0, True) # Utilisé pour copier la stat du Type


# Types
Anneau = Type("Anneau", Sagesse, 0.8, 0)
Armure = Type("Armure", Résistance, 2, 1)
Épée = Type("Épée", Attaque, 1.4, 1)
Heaume = Type("Heaume", Résistance, 1, 0)
Lance = Type("Lance", Dextérité, 0.8, 1)
Bouclier = Type("Bouclier", Résistance, 1.4, 0)
Hache = Type("Hache", Puissance, 1.8, 1)
Torche = Type("Torche", Null, 0, 1)
Grimoire = Type("Grimoire", Intelligence, 2, 0)
Crystal = Type("Crystal", Sagesse, 1.6, 0)
Écu = Type("Écu", Résistance, 1.2, 0)
Orbe = Type("Orbe", Intelligence, 1.3, 1)
Hallebarde = Type("Hallebarde", Attaque, 1.7, 1)
Rapière = Type("Rapière", Dextérité, 0.7, 1)
Orange = Type("Orange", Null, 0, 1)
Dague = Type("Dague", DégâtsCritique, 2, 1)
Fouet = Type("Fouet", Dextérité, 0.6, 0)
Arc = Type("Arc", Dextérité, 1.6, 0)
Masse = Type("Masse", Puissance, 2, 1)
Arbalète = Type("Arbalète", Dextérité, 1.3, 1)
Fusil = Type("Fusil", Précision, 0.8, 0)
Pistolet = Type("Pistolet", Précision, 1.1, 0)
Sabre = Type("Sabre", Attaque, 1.1, 0)
Marteau = Type("Marteau", Puissance, 1.8, 0)
Bâton = Type("Bâton", Intelligence, 0.7, 0)
Imprimante = Type("Imprimante", Null, 0, 1)
Sceptre = Type("Sceptre", Intelligence, 1.8, 0)
Potion = Type("Potion", Random, 3, 1)
Parchemin = Type("Parchemin", Intelligence, 3, 0)
Tromblon = Type("Tromblon", Puissance, 3, 0)
Pelle = Type("Pelle", Attaque, 0.7, 1)
Trident = Type("Trident", Attaque, 1, 0)
Chakram = Type("Chakram", Dextérité, 1.2, 0)
Casque = Type("Casque", Résistance, 1, 0)
Katana = Type("Katana", Attaque, 1.9, 0)
Faux = Type("Faux", Attaque, 0.9, 1)
Naginata = Type("Naginata", Dextérité, 1, 0)
Batte = Type("Batte", Attaque, 1.3, 1)
Gilet = Type("Gilet", Résistance, 0.8, 0)
Gant = Type("Gants", Attaque, 0.3, 2)
Raquette = Type("Raquette", Attaque, 0.2, 1)
BombeA = Type("Bombe atomique", CrimesGuerre, 1, 1)
Monado = Type("Monado", Concentration, 2, 0)
LanceRoquette = Type("Lance-roquette", Puissance, 3, 0)
CouteauLancer = Type("Couteaux de lancer", Précision, 1.5, 2)
FusilPompe = Type("Fusil à pompe", Puissance, 1.7, 0)
Botte = Type("Bottes", Vitesse, 0.8, 3)
Bolas = Type("Bolas", Dextérité, 0.5, 2)
Fléau = Type("Fléau", Attaque, 1, 0)
LanceFlamme = Type("Lance-Flamme", Brulure, 1, 0)
Faucille = Type("Faucille", Dextérité, 1.3, 1)
Shurikens = Type("Shurikens", Précision, 1.4, 2)
Sarbacane = Type("Sarbacane", Empoisonement, 0.8, 1)
Chaîne = Type("Chaîne", Vitesse, 0.4, 1)
Claymore = Type("Claymore", Attaque, 1.8, 1)
Fleuret = Type("Fleuret", Vitesse, 0.8, 0)
Falchion = Type("Falchion", Concentration, 1.5, 0)
Kukri = Type("Kukri", Attaque, 0.6, 0)
Kunai = Type("Kunai", PénétrationPhysique, 0.8, 0)
Taser = Type("Taser", Electrocution, 0.8, 0)
Sniper = Type("Sniper", Précision, 2, 0)


# Materials
doré = Material("doré", ArgentRécolté, 7, 1, True)
feu = Material("de feu", AptFeu, 5, 1, 0)
glace = Material("de glace", AptGlace, 5, 1, 0)
argent = Material("d'argent", DégâtsMortsVivants, 6, 2, 0)
verre = Material("de verre", DégâtsCritique, 4, 4, 0)
eau = Material("d'eau", AptEau, 5, 1, 0)
air = Material("d'air", AptAir, 5, 1, 0)
terre = Material("de terre", AptTerre, 5, 1, 0)
sang = Material("de sang", Vamprisme, 6, 1, 0)
obsidienne = Material("d'obsidienne", DégâtsCritique, 8, 1, 0)
titane = Material("de titane", Copy, 7, 2, 0)
foudre = Material("de foudre", AptFoudre, 5, 1, 0)
crystal = Material("de crystal", Résistance, 9, 1.5, 0)
quartz = Material("de quartz", DégâtsCritique, 8, 1.5, 0)
décoré = Material("décoré", Copy, 10, 2, 1, True)
émeraude = Material("d'émeraude", Empoisonement, 8, 0.5, 0)
rubis = Material("de rubis", Vamprisme, 8, 0.5, 0)
saphire = Material("de saphire", Agilité, 8, 0.5, 0)
diamant = Material("de diamant", DégâtsCritique, 10, 0.5, 0)
osseux = Material("osseux", DégâtsCritique, 6, 0.2, 2)
adamantium = Material("d'adamantium", Résistance, 12, 3, 0)
bronze = Material("de bronze", Résistance, 7, 0.8, 0)
fer = Material("de fer", Copy, 6, 1, 0)
étain = Material("d'étain", Attaque, 6, 1.5, 0)
draconium = Material("de draconium", Copy, 12, 4, 0)
cobalt = Material("de cobalt", Durabilité, 10, 2, 0)
ardite = Material("d'ardite", AptFeu, 10, 3, 0)
manyullyn = Material("de manyullyn", Null, 0, 11, 0)
cuivre = Material("de cuivre", Résistance, 6, 0.7, 0)
papier = Material("de papier", Null, 1, 0, 0)
acier = Material("d'acier", Durabilité, 7, 1.2, 0)
pierre = Material("de pierre", Attaque, 3, 0.6, 0)
mithril = Material("de mithril", Durabilité, 12, 4, 0)
orichalque = Material("d'orichalque", Attaque, 11, 2, 0)
vibranium = Material("de vibranium", RenvoiDégâts, 10, 1, 0)
osmium = Material("d'osmium", Copy, 9, 1.2, 0)
uru = Material("d'uru", AptFoudre, 10, 3, 0)
duracier = Material("de duracier", Résistance, 8, 2, 0)
cortosis = Material("de cortosis", AptLumière, 8, 3, 0)
latinum = Material("de latinum", Null, 9, 0, 0)
naquadah = Material("de naquadah", Copy, 9, 1.8, 0)
ébonite = Material("d'ébonite", Résistance, 8, 0.6, 0)
tiberium = Material("de tiberium", Attaque, 9, 0.6, 0)
volithe = Material("de volithe", Vitesse, 8, 1.5, 0)
erchyus = Material("d'erchyus", AptLumière, 8, 2, 0)
luminitite = Material("de luminite", AptLumière, 9, 4, 0)
démonite = Material("de démonite", AptTénébres, 9, 4, 0)
adamantine = Material("d'adamantine", Copy, 9, 5, 0)
australium = Material("d'australium", Attaque, 9, 3, 0)
unobtainium = Material("d'unobtainium", Durabilité, 12, 5, 0)
aiguemarine = Material("d'aiguemarine", Sagesse, 9, 1.5, 0)
opale = Material("d'opale", AptEau, 8, 2, 0)
jade = Material("de jade", ArgentRécolté, 8, 2, 0)
platine = Material("de platine", Puissance, 7, 1.5, 0)
lave = Material("de lave", AptFeu, 6, 2, 0)
chair = Material("de chair", Régénération, 5, 0.5, 0)



# Attributes
Témor = Attribute("de Témor", Attaque, 2, 3, 0)
Tamaire = Attribute("de Tamaire", Résistance, 2, 3, 0)
magique = Attribute("magique", Intelligence, 1, 1.5, 0, True)
pointu = Attribute("pointu", PénétrationPhysique, 0, 0.5, 1, True)
enflammé = Attribute("enflammé", AptFeu, 0, 1, 1, True)
cassé = Attribute("cassé", Null, -2, 0, 1, True)
mouillé = Attribute("mouillé", AptEau, 0, 1, 1, True)
KLitThé = Attribute("de K-Lit-Thé", Copy, 2, 2, 0)
inutile = Attribute("inutile", Null, -1, 0, 0, True)
froid = Attribute("froid", AptGlace, 0, 1, 1, True)
volant = Attribute("volant", AptAir, 0, 1, 1, True)
Patesriz = Attribute("de la Patesriz", Copy, 2, 0.5, 0)
force = Attribute("de force", Attaque, 0, 1.5, 0)
courage = Attribute("de courage", Résistance, 0, 1.5, 0)
sagesse = Attribute("de sagesse", Sagesse, 0, 1.5, 0)
vie = Attribute("de vie", Régénération, 0, 0.8, 0)
vivant = Attribute("vivant", Régénération, 0, 0.5, 1, True)
Paix = Attribute("de la Paix", Vitalité, 1, 1.5, 0)
gel = Attribute("du gel", AptGlace, 0, 1.5, 0)
sanguin = Attribute("sanguin", Vamprisme, 0, 0.5, 1, True)
tonnere = Attribute("du tonnere", AptFoudre, 0, 1.5, 0)
toner = Attribute("du toner", Null, 1, 0, 0)
sympa = Attribute("sympa", Copy, 1, 0.3, 0)
merde = Attribute("de merde", Null, -3, 0, 0)
usé = Attribute("usé", Null, -1, 0, 1, True)
lourd = Attribute("lourd", Copy, 0, 0.5, 1, True)
naturel = Attribute("naturel", Régénération, 0, 0.3, 4, True)
piquant = Attribute("piquant", RenvoiDégâts, 0, 0.5, 1, True)
épineux = Attribute("épineux", RenvoiDégâts, 0, 0.8, 2, True)
vitesse = Attribute("de vitesse", Vitesse, 0, 1, 0)
chance = Attribute("de chance", Chance, 0, 1, 0)
chanceux = Attribute("chanceux", Chance, 0, 1.5, 2, True)
Toncha = Attribute("d'Antoncha", Copy, 2, 1, 0)
légendaire = Attribute("légendaire", Copy, 3, 3, 0, True)
légende = Attribute("de légende", Copy, 3, 4, 0)
protecteur = Attribute("protecteur", Résistance, 0, 2, 3)
merdique = Attribute("merdique", Null, -3, 0, 0, True)
MédineShina = Attribute("de Médine-Shina", Null, -3, 0, 0)
Iochi = Attribute("de Iochi", Attaque, 1, 1.2, 0)
Ardiké = Attribute("d'Ardiké", Attaque, 1, 1.5, 0)
éléctrique = Attribute("éléctrique", AptFoudre, 0, 1, 0, True)
Idicong = Attribute("d'Idicong", Agilité, 1, 0.8, 0)
nul = Attribute("nul", Null, -2, 0, 4, True)
Sauron = Attribute("de Sauron", Attaque, 1, 2, 0)
Passito = Attribute("des Passito", Null, -3, 0, 0)
Tanosse = Attribute("de Tanosse", Copy, 2, 2, 0)
dimensionel = Attribute("dimensionel", Copy, 3, 3, 4, True)
transcendant = Attribute("transcendant", Copy, 5, 5, 1, True)
ultime = Attribute("ultime", Copy, 127, 6, 0, True)
loup = Attribute("du loup", Attaque, 0, 2, 0)
ours = Attribute("de l'ours", Puissance, 0, 2, 0)
serpent = Attribute("du serpent", Empoisonement, 0, 2, 0)
lievre = Attribute("du lièvre", Agilité, 0, 2, 0)
renard = Attribute("du renard", Dextérité, 0, 2, 0)
lunaire = Attribute("lunaire", AptTénébres, 2, 2, 0, True)
solaire = Attribute("solaire", AptLumière, 2, 2, 0, True)
EA = Attribute("d'Ihé", ContenuPayant, -3, 1, 0)
Aegis = Attribute("d'Aegis", AptLumière, 3, 3, 0)
alchimique = Attribute("alchimique", AptÉlémentaire, 2, 1, 0, True)
philosophal = Attribute("philosophal", AptTemporelle, 4, 1, 1, True)
Arbie = Attribute("d'Arbie", Triche, 3, 1, 0)
Onald = Attribute("d'Onald", PatriotismeAveugle, -3, 1, 0)
aléatoire = Attribute("aléatoire", Chance, 0, 1, 0, True)
Aispetrant = Attribute("des Aispet-Rant", Null, -127, 0, 0)
DDD = Attribute("des Dédais", Puissance, 1, 3, 0)
complexe = Attribute("complexe", Random, 1, 1, 0, True)
Édal = Attribute("d'Édal", Chance, 1, 2, 0)
Spidreun = Attribute("du Spid-Reun", Vitesse, 1, 5, 0)
soldat = Attribute("du soldat", Attaque, 0, 1.5, 0)
assassin = Attribute("de l'assassin", Vitesse, 0, 1.5, 0)
paladin = Attribute("du paladin", Résistance, 0, 1.5, 0)
mage = Attribute("du mage", Sagesse, 0, 1.5, 0)
prêtre = Attribute("du prêtre", Régénération, 0, 1.5, 0)
marchand = Attribute("du marchand", ArgentRécolté, 0, 1.5, 0)
chasseur = Attribute("du chasseur", Dextérité, 0, 1.5, 0)
médecin = Attribute("du médecin", Vitalité, 0, 1.5, 0)
Eros = Attribute("d'Eros", Charme, 0, 3, 0)
Émont = Attribute("d'Émont", PacteDiable, 0, 1, 0)
Io = Attribute("d'Io", AptTemporelle, 3, 1, 0)
Yego = Attribute("d'Yego", Dinousaures, 2, 1, 0)
D4C = Attribute("d'Iforci", AptDimensionelle, 3, 1, 0)



# Quality
Maudit = Quality("Maudit", -6, 6)
Merdique = Quality("Merdique", -3, 2)
Cassé = Quality("Cassé", -5, 0)
Mauvais = Quality("Mauvaise Qualité", -1, 1)
Poussiéreux = Quality("Poussiéreux", -2, 0)
Banal = Quality("Banal", 0.5, 0)
Basique = Quality("Basique", 0, 1)
Commun = Quality("Commun", 1, 0)
Curieux = Quality("Curieux", 0.5, 1)
PeuCommun = Quality("Peu Commun", 2, 0)
Étrange = Quality("Étrange", 1, 2)
Rare = Quality("Rare", 4, 1)
Antique = Quality("Antique", 6, 2)
Précieux = Quality("Précieux", 7, 0)
Enchanté = Quality("Enchanté", 4, 3)
Mythique = Quality("Mythique", 9, 1)
Mystique = Quality("Mystique", 6, 6)
Légendaire = Quality("Légendaire", 9, 4)
Relique = Quality("Relique", 12, 1)
Divin = Quality("Divin", 12, 4)
Démoniaque = Quality("Démoniaque", 16, 2)
Dimensionel = Quality("Dimensionel", 13, 5)
Galactique = Quality("Galactique", 16, 3)
Transcendant = Quality("Transcendant", 20, 5)
Ultime = Quality("Ultime", 16, 8)
Omniscient = Quality("Omniscient", 10, 12)

qualities = [[Maudit],
            [Merdique, Cassé],
            [Mauvais, Poussiéreux],
            [Banal, Basique],
            [Commun, Curieux],
            [PeuCommun, Étrange],
            [Rare, Antique],
            [Précieux, Enchanté],
            [Mythique, Mystique],
            [Légendaire, Relique],
            [Divin, Démoniaque],
            [Dimensionel, Galactique],
            [Transcendant, Ultime, Omniscient]]



# On définit la fonction principale
def generateItem() -> Tuple[str, str]:
    # On prend des paramètres aléatoires dans les listes
    iType, iAttr, iMat = choice(types), choice(attributes), choice(materials)
    title = iType.name + " " + iMat.name # On commence à former le nom de l'objet
    # On change le nom du matériau suivant masculin/féminin/pluriel
    if iType.gender in (1, 3) and iMat.feminine == 1: title += "e"
    elif iType.gender in (1, 3) and iMat.feminine == 2: title = title[:-1] + "se"
    elif iType.gender in (1, 3) and iMat.feminine == 3: title = title[:-3] + "rice"
    elif iType.gender in (1, 3) and iMat.feminine == 4: title += "le"
    if iType.gender >= 2 and iMat.plural: title += "s"
    title += " " + iAttr.name # On ajoute le nom de l'attribut
    # On change le nom de l'attribut suivant masculin/féminin/pluriel
    if iType.gender in (1, 3) and iAttr.feminine == 1: title += "e"
    elif iType.gender in (1, 3) and iAttr.feminine == 2: title = title[:-1] + "se"
    elif iType.gender in (1, 3) and iAttr.feminine == 3: title = title[:-3] + "rice"
    elif iType.gender in (1, 3) and iAttr.feminine == 4: title += "le"
    if iType.gender >= 2 and iAttr.plural: title += "s"
    if iAttr.name != "aléatoire": qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-1, 1), 0), 12) # On gère l'ajout de la qualité de l'objet
    else: qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-5, 5), 0), 12) # Cas special pour "aléatoire"
    quality = choice(qualities[qualNum]) # On prend une qualité aléatoire correspondant au rang de l'objet
    item = quality.name # On l'ajoute au nom

    # On calcule les 3 premières stats
    for i in range(3):
        obj: Union[Type, Material, Attribute] = [iType, iMat, iAttr][i] # On prend l'objet, et setup relative
        stat, relative = obj.stat, False
        # Gestion des cas "Copy", "Random" et "Null"
        if stat.name == "Copy": stat = iType.stat
        if stat.name == "Random": stat = stats[randint(0, 2)]
        elif stat.name == "Null": continue
        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * quality.multiplier *  stat.modifier * obj.statMod + randint(-4, 6))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type in ("Relative", "FixedRelative"): statMagn, relative = statMagn * 2, True
        if "Fixed" in stat.type: statMagn = stat.modifier # Et si sa valeur est fixe
        # On rajoute la stat au message
        if statMagn != 0: item += "\n " + ("+" if statMagn > 0 else "-") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name

    qualMul = -6 if quality.name == "Démoniaque" else quality.multiplier # On gère le cas spécial de la qualité "Démoniaque"
    for i in range(quality.totalStats): # On calcule toutes les autres stats
        stat, relative = choice(stats), False
        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * qualMul * stat.modifier + randint(-2, 3))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type == "Relative": statMagn, relative = statMagn * 2, True
        # On rajoute la stat au message
        if statMagn != 0: item += "\n " + ("+" if statMagn > 0 else "-") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name

    return title, item