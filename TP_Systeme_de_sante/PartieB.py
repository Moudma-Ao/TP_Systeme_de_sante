class Client:
    def __init__(self, nom: str, prenom: str, email: str):
        self.__nom = nom    # private  
        self.__prenom = prenom  # private  
        self.__email = email    # private  
        self._comptes = []  # protected
    
    def ajouter_compte(self, compte):
        self._comptes.append(compte)
    
    def afficher_comptes(self):
        for compte in self._comptes: 
            print(f"Compte n°{compte.get_numero()} - Solde: {compte.get_solde()}€")

#=====================================
# COMPTE
#==================================    

class Compte:
    def __init__(self, numero: str, solde: float, proprietaire: Client):
        self.__numero = numero      # private
        self.__solde = solde        # private  
        self.__proprietaire = proprietaire  # private
        proprietaire.ajouter_compte(self)
    
    def deposer(self, montant: float):
        self.__solde += montant
    
    def retirer(self, montant: float):
        if montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Solde insuffisant")
        
    def afficher_solde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde}€")
        
    def get_numero(self) -> str:
        return self.__numero 
    
    def get_solde(self) -> float:
        return self.__solde

    def get_proprietaire(self) -> Client:
        return self.__proprietaire
    
    
    
    ############################################################
    # Test 
    ###################################################
# test_bank.py
class Client:
    def __init__(self, nom: str, prenom: str, email: str):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self._comptes = []
    
    def ajouter_compte(self, compte):
        self._comptes.append(compte)
    
    def afficher_comptes(self):
        print(f"\n--- Comptes de {self.__prenom} {self.__nom} ---")
        for compte in self._comptes:
            print(f"Compte n°{compte.get_numero()} - Solde: {compte.get_solde()}€")

class Compte:
    def __init__(self, numero: str, solde: float, proprietaire: Client):
        self.__numero = numero
        self.__solde = solde
        self.__proprietaire = proprietaire
        proprietaire.ajouter_compte(self)
    
    def deposer(self, montant: float):
        self.__solde += montant
        print(f"Dépôt de {montant}€ sur le compte {self.__numero}")
    
    def retirer(self, montant: float):
        if montant <= self.__solde:
            self.__solde -= montant
            print(f"Retrait de {montant}€ du compte {self.__numero}")
        else:
            print(f"Erreur: Solde insuffisant pour retirer {montant}€")
        
    def afficher_solde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde}€")
        
    def get_numero(self) -> str:
        return self.__numero 
    
    def get_solde(self) -> float:
        return self.__solde

#######################################################
# TEST
#########################################################
if __name__ == "__main__":
    # Création des clients
    client1 = Client("Systeme", "Sante", "syssan@email.com")
    client2 = Client("Diallo", "Mamoudou", "mdiallo@email.com")

    # Création des comptes
    compte1 = Compte("12345", 1000.0, client1)
    compte2 = Compte("67890", 500.0, client1)
    compte3 = Compte("11111", 2000.0, client2)

    # Test des opérations
    compte1.deposer(200)
    compte1.retirer(50)
    compte2.retirer(600)  # Test solde insuffisant

    # Affichage des comptes
    client1.afficher_comptes()
    client2.afficher_comptes()

    # Test affichage solde
    compte1.afficher_solde()