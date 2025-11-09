from datetime import datetime
#########################################################
# Utilisateur
############################################################
class Utilisateur:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role
    
    def verifier_password(self, password: str) -> bool:
        return self.password == password
    
    def est_admin(self) -> bool:
        return self.role == 'admin'
    
#########################################################
# Paiement
############################################################

class Paiement:
    def __init__(self, id_paiement: int, client: Utilisateur, montant: float, service: str):
        self.id_paiement = id_paiement
        self.client = client
        self.montant = montant
        self.service = service
        self.date = datetime.now()
        self.statut = "effectue"
    
    def annuler(self):
        self.statut = "annule"
    
    def __str__(self):
        return f"Paiement #{self.id_paiement} - {self.service} - {self.montant}€ - {self.statut}"

###################################################
# SPL
###################################################
class SPL:
    def __init__(self):
        self.utilisateurs = []
        self.paiements = []
        self.session_actuelle = None
        self._initialiser_donnees()
    
    def _initialiser_donnees(self):
        admin = Utilisateur("admin", "admin123", "admin")
        client1 = Utilisateur("client1", "pass123", "client")
        client2 = Utilisateur("client2", "pass456", "client")
        
        self.utilisateurs.extend([admin, client1, client2])
    
    def s_authentifier(self, username: str, password: str) -> bool:
        for user in self.utilisateurs:
            if user.username == username and user.verifier_password(password):
                self.session_actuelle = user
                print(f"OK - Authentification reussie - {username} ({user.role})")
                return True
        print("ERREUR - Echec de l'authentification")
        return False
    
    def payer_service(self, montant: float, service: str) -> bool:
        if not self.session_actuelle or self.session_actuelle.est_admin():
            print("ERREUR - Seuls les clients connectes peuvent payer")
            return False
        
        id_paiement = len(self.paiements) + 1
        paiement = Paiement(id_paiement, self.session_actuelle, montant, service)
        self.paiements.append(paiement)
        
        print(f"OK - Paiement effectue - {service} : {montant}€")
        self.recevoir_recu(paiement)
        return True
    
    def recevoir_recu(self, paiement: Paiement):
        print("\n" + "="*40)
        print("           RECU DE PAIEMENT")
        print("="*40)
        print(f"Client: {paiement.client.username}")
        print(f"Service: {paiement.service}")
        print(f"Montant: {paiement.montant}€")
        print(f"Date: {paiement.date.strftime('%d/%m/%Y %H:%M')}")
        print(f"ID: #{paiement.id_paiement}")
        print("="*40 + "\n")
    
    def consulter_paiements(self):
        if not self.session_actuelle:
            print("ERREUR - Veuillez vous authentifier")
            return
        
        if self.session_actuelle.est_admin():
            paiements_a_afficher = self.paiements
            print("=== TOUS LES PAIEMENTS (Admin) ===")
        else:
            paiements_a_afficher = [p for p in self.paiements if p.client == self.session_actuelle]
            print(f"=== MES PAIEMENTS ({self.session_actuelle.username}) ===")
        
        if not paiements_a_afficher:
            print("Aucun paiement trouve")
            return
            
        for paiement in paiements_a_afficher:
            print(paiement)
    
    def annuler_paiement(self, id_paiement: int) -> bool:
        if not self.session_actuelle or not self.session_actuelle.est_admin():
            print("ERREUR - Seuls les administrateurs peuvent annuler des paiements")
            return False
        
        for paiement in self.paiements:
            if paiement.id_paiement == id_paiement:
                paiement.annuler()
                print(f"OK - Paiement #{id_paiement} annule")
                return True
        
        print(f"ERREUR - Paiement #{id_paiement} non trouve")
        return False
#############################################################################
# TEST
################################################################
if __name__ == "__main__":
    systeme = SPL()
    
    print("=== TEST SYSTEME SPL ===")
    
    # Test client
    print("\n1. Authentification client:")
    systeme.s_authentifier("client1", "pass123")
    
    print("\n2. Paiement:")
    systeme.payer_service(50.0, "Abonnement Internet")
    
    print("\n3. Mes paiements:")
    systeme.consulter_paiements()
    
    # Test admin
    print("\n4. Authentification admin:")
    systeme.s_authentifier("admin", "admin123")
    
    print("\n5. Tous les paiements:")
    systeme.consulter_paiements()
    
    print("\n6. Annulation paiement:")
    systeme.annuler_paiement(1)
    
    print("\n7. Verification:")
    systeme.consulter_paiements()