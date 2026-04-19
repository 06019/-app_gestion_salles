import customtkinter as ctk
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()

        self.title("Application de gestion des salles")
        self.geometry("700x500")

        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10)

        self.lblCode = ctk.CTkLabel(self.cadreInfo, text="Code salle :")
        self.lblCode.grid(row=0, column=0, padx=10, pady=10)
        self.txtCode = ctk.CTkEntry(self.cadreInfo)
        self.txtCode.grid(row=0, column=1, padx=10, pady=10)

        self.lblLibelle = ctk.CTkLabel(self.cadreInfo, text="Libellé :")
        self.lblLibelle.grid(row=1, column=0, padx=10, pady=10)
        self.txtLibelle = ctk.CTkEntry(self.cadreInfo)
        self.txtLibelle.grid(row=1, column=1, padx=10, pady=10)

        self.lblType = ctk.CTkLabel(self.cadreInfo, text="Type :")
        self.lblType.grid(row=2, column=0, padx=10, pady=10)
        self.txtType = ctk.CTkEntry(self.cadreInfo)
        self.txtType.grid(row=2, column=1, padx=10, pady=10)

        self.lblCapacite = ctk.CTkLabel(self.cadreInfo, text="Capacité :")
        self.lblCapacite.grid(row=3, column=0, padx=10, pady=10)
        self.txtCapacite = ctk.CTkEntry(self.cadreInfo)
        self.txtCapacite.grid(row=3, column=1, padx=10, pady=10)

        # Cadre Actions
        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10)

        self.btnAjouter = ctk.CTkButton(self.cadreAction, text="Ajouter", width=70, command=self.ajouter_salle)
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", width=70, command=self.supprimer_salle)
        self.btnSupprimer.grid(row=0, column=1, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(self.cadreAction, text="Modifier", width=70, command=self.modifier_salle)
        self.btnModifier.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(self.cadreAction, text="Rechercher", width=70, command=self.rechercher_salle)
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)

    def ajouter_salle(self):
        salle = Salle(
            self.txtCode.get(),
            self.txtLibelle.get(),
            self.txtType.get(),
            self.txtCapacite.get()
        )

        self.service_salle.ajouter_salle(salle)

    def supprimer_salle(self):
        code = self.txtCode.get()
        self.service_salle.supprimer_salle(code)


    def modifier_salle(self):
        salle = Salle(
            self.txtCode.get(),
            self.txtLibelle.get(),
            self.txtType.get(),
            self.txtCapacite.get()
        )

        self.service_salle.modifier_salle(salle)

