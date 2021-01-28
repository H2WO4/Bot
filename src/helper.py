# Fonction qui vérifie si deux strings sont "à peu près" égales
def isAlmostEqual(str1, str2):
    # Helper pour enlever ce qu'il faut enlever
    def convert(string):
        return list(filter(None, string.lower()
            .replace(".", "") # Les points
            .replace("'", " ") # Les apostrophes
            .replace("’", " ")
            .replace("*", " ") # Le gras
            .replace("_", " ") # Le souligné
            .replace("!", "") # Les points d'exclamation
        .split()))

    # On compare
    return convert(str1) == convert(str2)