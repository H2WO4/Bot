# Fonction qui vérifie si deux strings sont "à peu près" égales
def isAlmostEqual(str1, str2):
    # Helper pour enlever ce qu'il faut enlever
    def convert(string):
        return list(filter(None, string.lower()
            .replace(".", "") # Les points
            .replace("-", " ") # Les tirêts
            .replace("'", " ") # Les apostrophes
            .replace("’", " ")
            .replace("*", " ") # Le gras
            .replace("_", " ") # Le souligné
            .replace("!", "") # Les points d'exclamation
            .replace("é", "e") # Les accents
            .replace("è", "e")
            .replace("ê", "e")
            .replace("à", "a")
            .replace("â", "a")
            .replace("ô", "o")
            .replace("î", "i")
        .split()))

    # On compare
    return convert(str1) == convert(str2)