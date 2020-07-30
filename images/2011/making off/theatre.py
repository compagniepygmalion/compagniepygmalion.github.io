import os
i = 0
arr = os.listdir()
for v in arr:
    nom = ""
    if "à" in v or "é" in v or " " in v:
        for n in v:
            if n == "à" or n == "â":
                nom = nom + "a"
            elif n == "é":
                nom = nom + "e"
            elif n == " ":
                nom = nom + "_"
            else:
                nom = nom + n
        os.rename(v, nom)
        print(nom)
        
