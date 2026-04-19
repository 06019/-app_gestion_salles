from data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if salle.code == "" or salle.libelle == "" or salle.type == "" or str(salle.capacite) == "":
            return False, "Tous les champs sont obligatoires"
        elif int(salle.capacite) < 1:
            return False, "La capacité doit être supérieure ou égale à 1"
        else:
            self.dao_salle.insert_salle(salle)
            return True, "Salle ajoutée avec succès"

    def modifier_salle(self, salle):
        if salle.code == "" or salle.libelle == "" or salle.type == "" or str(salle.capacite) == "":
            return False, "Tous les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacité doit être supérieure ou égale à 1"

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès"