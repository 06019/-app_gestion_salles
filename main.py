from data.dao_salle import DataSalle
from models.salle import Salle

data_salle = DataSalle()


con = data_salle.get_connection()
print("Connexion réussie :", con)
con.close()


s1 = Salle("S100", "Salle Test", "Classe", 20)
data_salle.insert_salle(s1)
print("Salle ajoutée")


salle = data_salle.get_salle("S100")
if salle is not None:
    print("Salle trouvée :")
    salle.afficher_infos()
else:
    print("Salle introuvable")


s2 = Salle("S100", "Salle Test Modifiée", "Laboratoire", 35)
data_salle.update_salle(s2)
print("Salle modifiée")


salle = data_salle.get_salle("S100")
if salle is not None:
    print("Après modification :")
    salle.afficher_infos()

print("Liste de toutes les salles :")
liste = data_salle.get_salles()
for s in liste:
    i=1
    print(f"salle:{i}")
    s.afficher_infos()
    i = i+1

data_salle.delete_salle("S100")
print("Salle supprimée")


salle = data_salle.get_salle("S100")
if salle is None:
    print("La salle S100 a bien été supprimée")