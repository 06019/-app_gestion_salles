import json
import mysql.connector
from models.salle import Salle

class DataSalle:
     def get_connection(self):
         with open("config.json", "r",encoding="utf-8") as f:
             config = json.load(f)
         con = mysql.connector.connect(
             host=config["host"],
             user=config["user"],
             password=config["password"],
             database=config["database"]
         )
         return con

     def insert_salle(self, salle):
         con = self.get_connection()
         cursor = con.cursor()
         cursor.execute(

             "insert into salle values(%s,%s,%s,%s)",
             (salle.code, salle.libelle, salle.type, salle.capacite)

         )

         con.commit()
         cursor.close()
         con.close()
     def update_salle(self, salle):
         con = self.get_connection()
         cursor = con.cursor()
         cursor.execute( """

            UPDATE salle
            SET libelle=%s, type=%s, capacite=%s
            WHERE code=%s
            """,
            ( salle.libelle, salle.type, salle.capacite,salle.code)

        )

         con.commit()
         cursor.close()
         con.close()

     def delete_salle(self, code):
         con = self.get_connection()
         cursor = con.cursor()

         cursor.execute(
             "DELETE FROM salle WHERE code=%s",
             (code,)
         )

         con.commit()
         cursor.close()
         con.close()





