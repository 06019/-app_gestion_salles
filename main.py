from services.service_salle import ServiceSalle
from models.salle import Salle

service_salle = ServiceSalle()

print("Liste des salles :")
liste = service_salle.recuperer_salles()
i = 1
for s in liste:
    print(f"Salle {i} :")
    s.afficher_infos()
    i = i + 1

s1 = Salle("S100", "Salle Test", "Classe", 20)
resultat, message = service_salle.ajouter_salle(s1)
print(message)

salle = service_salle.rechercher_salle("S100")
if salle is not None:
    print("Salle trouvée :")
    salle.afficher_infos()
else:
    print("Salle introuvable")

s2 = Salle("S100", "Salle Test Modifiée", "Laboratoire", 35)
resultat, message = service_salle.modifier_salle(s2)
print(message)

salle = service_salle.rechercher_salle("S100")
if salle is not None:
    print("Après modification :")
    salle.afficher_infos()

service_salle.supprimer_salle("S100")
print("Salle supprimée")

salle = service_salle.rechercher_salle("S100")
if salle is None:
    print("La salle S100 a bien été supprimée")
else:
    print("La salle existe encore")