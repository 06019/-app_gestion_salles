import customtkinter as ctk
from tkinter import ttk
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()

        self.title("Application de gestion des salles")
        self.geometry("700x500")


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


        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10)

        self.btnAjouter = ctk.CTkButton(self.cadreAction, text="Ajouter", width=70)
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(self.cadreAction, text="Supprimer", width=70)
        self.btnModifier.grid(row=0, column=1, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(self.cadreAction, text="Modifier", width=70)
        self.btnSupprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(self.cadreAction, text="Rechercher",width=70)
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)






