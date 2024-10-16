
# appareils = {"capteur1": "température", "capteur2": "humidité", "capteur3": "pression"}

# capteur = {"id" : 12, "position" : "baie", "temprerature" : 17.5, "defaut":False}

# # print(appareils["capteur1"])

# print(appareils.get("capteur4"),"Inconnu")

# print(appareils.get("capteur2", "Inconnu"))  # Inconnu



# appareils = {"capteur1": "température", "capteur2": "humidité"}

# # Vérifier si "capteur4" est dans le dictionnaire
# etat_capteur4 = appareils.get("capteur4", "Inconnu")

# if etat_capteur4 == "Inconnu":
#     print("Le capteur4 n'est pas configuré dans le système.")
# else:
#     print(f"Le capteur4 mesure {etat_capteur4}.")



# appareils = {"capteur1": "température", "capteur2": "humidité"}

# # Obtenir l'état d'un capteur
# etat_capteur4 = appareils.get("capteur4")  # Renvoie None si capteur4 n'existe pas

# if etat_capteur4 is None:
#     print("Le capteur4 n'est pas dans le système.")
# else:
#     print(f"Le capteur4 mesure {etat_capteur4}.")

# capteurs = {"capteur1": "température", "capteur2": None}

# if capteurs.get("capteur2") is None:
#     print("Le capteur2 n'a pas encore de valeur.")


# capteurs = {"capteur1": "température", "capteur2": None}

# etat_capteur2 = capteurs.get("capteur2", "Inconnu")
# # etat_capteur2 = capteurs.get("capteur3", "Inconnu")

# if etat_capteur2 == "Inconnu":
#     print("Le capteur2 est inconnu.")
# elif etat_capteur2 is None:
#     print("Le capteur2 n'a pas encore de valeur.")


# appareils = {"capteur1": "température", "capteur2": "humidité", "capteur3": "pression"}

# appareils["capteur2"] = "humidité relative"  # Modifie
# print(appareils)

# appareils["capteur4"] = "luminosité"  # Ajoute
# print(appareils)


# appareils = {"capteur1": "température", 
#              "capteur2": "humidité", 
#              "capteur3": "pression"
#              }

# for cle in appareils.keys():
#     print(cle)  # dict_keys(['capteur1', 'capteur2'])


# for valeur in appareils.values():
    # print(valeur) 
   

# for cle, valeur in appareils.items():
#     print(f"{cle}: {valeur}")  


# print(appareils.items()) 
# #renvoie : dict_items([('capteur1', 'température'), ('capteur2', 'humidité relative')])


print(appareils)

# del appareils["capteur3"]  # Supprime capteur3

# print(appareils)

# app_removed = appareils.pop("capteur4", "Inexistant")  # Supprime et renvoie la valeur
# print(app_removed)
# print(appareils)




# for capteur, type in appareils.items():
#     print(f"{capteur} mesure {type}")





# etat_capteurs = {"capteur1": "actif", "capteur1": "actif", "capteur3": "inactif"}

# # print(len(etat_capteurs))



# for cle, valeur in etat_capteurs.items():
#     print(f"{cle} : {valeur}")


# etat_capteurs = {"capteur1": "actif", "capteur1": "actif", "capteur3": "inactif"}

# # Vérifie si tous les capteurs sont actifs
# tous_actifs = all(etat_capteur=="actif" for etat_capteur in etat_capteurs.values())
# print(tous_actifs)  # False, car capteur3 est inactif

# paquets = {"paquet1": 1200, "paquet2": 800, "paquet3": 1600}

# # Vérifie si au moins un paquet dépasse 1500 octets
# gros_paquet = any(taille > 1500 for taille in paquets.values())
# print(gros_paquet)  # True, car paquet3 dépasse 1500 octets


# etat_capteurs = {"capteur1": "actif", "capteur2": "actif", "capteur3": "inactif"}

# # Vider le dictionnaire
# etat_capteurs.clear()

# print(etat_capteurs)  # {}


# etat_capteurs = {"capteur1": "actif", "capteur2": "actif", "capteur3": "inactif"}

# # Compter le nombre de capteurs actifs
# nb_actifs = sum(1 for etat in etat_capteurs.values() if etat == "actif")
# print(nb_actifs)  # 2
