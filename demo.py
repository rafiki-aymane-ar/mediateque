import datetime
from tabulate import tabulate

class Support:
    def __init__(self, id: str, Titre: str, Disponibilité: bool):
        self.__id_support = id
        self.__Titre = Titre
        self.__Disponibilité = Disponibilité

    @property
    def id_support(self):
        return self.__id_support

    @id_support.setter
    def id_support(self, value):
        if isinstance(value, str):
            self.__id_support = value
        else:
            raise ValueError("L'id du support doit être une chaîne de caractères")

    @property
    def Titre(self):
        return self.__Titre

    @Titre.setter
    def Titre(self, value):
        if isinstance(value, str):
            self.__Titre = value
        else:
            raise ValueError("Le titre du support doit être une chaîne de caractères")

    @property
    def Disponibilité(self):
        return self.__Disponibilité

    @Disponibilité.setter
    def Disponibilité(self, value):
        if isinstance(value, bool):
            self.__Disponibilité = value
        else:
            raise ValueError("La disponibilité du support doit être un booléen")

    def estDiponible(self):
        return self.__Disponibilité

    def rendreDisponible(self):
        self.__Disponibilité = True

    def rendreIndisponible(self):
        self.__Disponibilité = False


class Livre(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Auteur: str, NombrePages: int):
        super().__init__(id, Titre, Disponibilité)
        self.__Auteur = Auteur
        self.__NombrePages = NombrePages

    @property
    def Auteur(self):
        return self.__Auteur

    @Auteur.setter
    def Auteur(self, value):
        if isinstance(value, str):
            self.__Auteur = value
        else:
            raise ValueError("L'auteur du livre doit être une chaîne de caractères")

    @property
    def NombrePages(self):
        return self.__NombrePages

    @NombrePages.setter
    def NombrePages(self, value):
        if isinstance(value, int) and value > 0:
            self.__NombrePages = value
        else:
            raise ValueError("Le nombre de pages du livre doit être un entier")


class CD_ROM(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Editeur: str, Capacite: int):
        super().__init__(id, Titre, Disponibilité)
        self.__Editeur = Editeur
        self.__Capacite = Capacite

    @property
    def Capacite(self):
        return self.__Capacite

    @Capacite.setter
    def Capacite(self, value):
        if isinstance(value, int) and value > 0:
            self.__Capacite = value
        else:
            raise ValueError("La capacité du CD-ROM doit être un entier")

    @property
    def Editeur(self):
        return self.__Editeur

    @Editeur.setter
    def Editeur(self, value):
        if isinstance(value, str):
            self.__Editeur = value
        else:
            raise ValueError("L'éditeur du CD-ROM doit être une chaîne de caractères")


class Magazine(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Editeur: str, NumeroPublication: int,DatePublication: datetime.date):
        super().__init__(id, Titre, Disponibilité)
        self.__Editeur = Editeur
        self.__NumeroPublication = NumeroPublication
        self.__DatePublication = DatePublication

    @property
    def Editeur(self):
        return self.__Editeur

    @Editeur.setter
    def Editeur(self, value):
        if isinstance(value, str):
            self.__Editeur = value
        else:
            raise ValueError("L'éditeur du magazine doit être une chaîne de caractères")

    @property
    def NumeroPublication(self):
        return self.__NumeroPublication

    @NumeroPublication.setter
    def NumeroPublication(self, value):
        if isinstance(value, int) and value > 0:
            self.__NumeroPublication = value
        else:
            raise ValueError("Le numéro de publication du magazine doit être un entier")

    @property
    def DatePublication(self):
        return self.__DatePublication

    @DatePublication.setter
    def DatePublication(self, date: datetime.date):
        if isinstance(date, datetime.date):
            self.__DatePublication = date
        else:
            raise ValueError("La date de publication du magazine doit être une date")


class Adherent:
    def __init__(self, id: str, Nom: str, Prenom: str, Email: str, Telephone: str):
        self.__id = id
        self.__Nom = Nom
        self.__Prenom = Prenom
        self.__Email = Email
        self.__Telephone = Telephone

    @property
    def id(self):
        return self.__id

    @property
    def Nom(self):
        return self.__Nom

    @property
    def Prenom(self):
        return self.__Prenom

    @property
    def Email(self):
        return self.__Email

    @property
    def Telephone(self):
        return self.__Telephone


class Emprunt:
    def __init__(self, id: str, Support: Support, Adherent: Adherent, DateEmprunt: datetime.date, DateRetour: datetime.date):
        self.__id = id
        self.__Support = Support
        if Support.estDiponible():
            Support.rendreIndisponible()
            self.__Support = Support
            self.__Adherent = Adherent
            self.__DateEmprunt = DateEmprunt
            self.__DateRetour = DateRetour
            self.__DateRetourMaximale = None
        else:
            raise ValueError("Le support n'est pas disponible")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str):
            self.__id = value
        else:
            raise ValueError("L'id de l'emprunt doit être une chaîne de caractères")

    @property
    def Support(self):
        return self.__Support

    @Support.setter
    def Support(self, value):
        if isinstance(value, Support):
            self.__Support = value
        else:
            raise ValueError("Le support de l'emprunt doit être un objet Support")

    @property
    def Adherent(self):
        return self.__Adherent

    @Adherent.setter
    def Adherent(self, value):
        if isinstance(value, Adherent):
            self.__Adherent = value
        else:
            raise ValueError("L'adhérent de l'emprunt doit être un objet Adherent")

    @property
    def DateEmprunt(self):
        return self.__DateEmprunt

    @DateEmprunt.setter
    def DateEmprunt(self, date: datetime.date):
        if isinstance(date, datetime.date):
            self.__DateEmprunt = date
        else:
            raise ValueError("La date d'emprunt doit être une date")

    @property
    def DateRetour(self):
        return self.__DateRetour

    @DateRetour.setter
    def DateRetour(self, date: datetime.date):
        if isinstance(date, datetime.date):
            self.__DateRetour = date
        else:
            raise ValueError("La date de retour doit être une date")

    @property
    def DateRetourMaximale(self):
        return self.__DateRetourMaximale

    @DateRetourMaximale.setter
    def DateRetourMaximale(self, value):
        if isinstance(value, datetime.date):
            self.__DateRetourMaximale = value
        else:
            raise ValueError("La date maximale de retour doit être une date valide")

    def estEmprunté(self):
        if self.__DateRetour is None:
            return True
        return self.__DateRetour > datetime.date.today()

    def estRendu(self):
        if self.__DateRetour is None:
            return False
        return self.__DateRetour <= datetime.date.today()

    def Afficher(self):
        print(
            f"Emprunt {self.__id} : {self.__Support.Titre} emprunté par {self.__Adherent.Nom} {self.__Adherent.Prenom}")

    def retourner(self, date_retour: datetime.date):
        self.__DateRetour = date_retour
        if date_retour <= datetime.date.today():
            self.__Support.rendreDisponible()
        else:
            self.__Support.rendreIndisponible()

    def duree_emprunt(self) -> int:
        """Retourne le nombre de jours depuis l'emprunt"""
        if self.__DateRetour is not None:
            return (self.__DateRetour - self.__DateEmprunt).days
        return (datetime.date.today() - self.__DateEmprunt).days


LARGEUR = 56  # Largeur totale du cadre


def afficher_menu():
    print("\n===========================================")
    print("    SYSTÈME DE GESTION DE MÉDIATHÈQUE    ")
    print("===========================================")
    print("              Menu Principal             ")
    print("-------------------------------------------")
    print("  1. ➕ Créer un emprunt")
    print("  2. ↩️ Retourner un emprunt")
    print("  3. 🔍 Afficher les détails d'un emprunt")
    print("  4. 📝 Afficher les emprunts en cours")
    print("  5. 👤 Afficher les emprunts d'un adhérent")
    print("  6. 📚 Afficher les emprunts d'un support")
    print("  7. 📊 Afficher les statistiques")
    print("  8. 📋 Afficher tous les emprunts")
    print("  9. ⚠️ Afficher les emprunts en retard")
    print('  10. 📚 Afficher tous les supports')
    print("  0. 🚪 Quitter")
    print("===========================================")


def afficher_supports(supports):
    table_data = []
    for support in supports:
        if isinstance(support, Livre):
            status = "Disponible" if support.estDiponible() else "Indisponible"
            table_data.append([
                support.id_support,
                "Livre",
                support.Titre,
                status,
                support.Auteur,
                f"{support.NombrePages} pages",
                "-",
                "-"
            ])
        elif isinstance(support, CD_ROM):
            status = "Disponible" if support.estDiponible() else "Indisponible"
            table_data.append([
                support.id_support,
                "CD-ROM",
                support.Titre,
                status,
                "-",
                "-",
                f"{support.Capacite} Mo",
                support.Editeur
            ])
        elif isinstance(support, Magazine):
            status = "Disponible" if support.estDiponible() else "Indisponible"
            table_data.append([
                support.id_support,
                "Magazine",
                support.Titre,
                status,
                "-",
                f"N°{support.NumeroPublication}",
                str(support.DatePublication),
                support.Editeur
            ])

    headers = ["ID", "Type", "Titre", "Statut", "Auteur", "Pages/N°", "Capacité/Date", "Editeur"]
    print("\n📚 Liste des supports:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def afficher_adherents(adherents):
    table_data = [[
        adh.id,
        adh.Nom,
        adh.Prenom,
        adh.Adresse,
        adh.Telephone,
        adh.Email
    ] for adh in adherents]

    headers = ["ID", "Nom", "Prénom", "Adresse", "Téléphone", "Email"]
    print("\n👥 Liste des adhérents:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def afficher_emprunts(emprunts):
    table_data = [[
        emp.id,
        emp.Support.Titre,
        f"{emp.Adherent.Nom} {emp.Adherent.Prenom}",
        emp.DateEmprunt,
        emp.DateRetour if emp.DateRetour else "Non retourné"
    ] for emp in emprunts]

    headers = ["ID", "Support", "Adhérent", "Date Emprunt", "Date Retour"]
    print("\n📝 Liste des emprunts:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def afficher_tous_details(supports, adherents, emprunts):
    print("\n=== 📊 ÉTAT GÉNÉRAL DE LA MÉDIATHÈQUE ===")

    print("\n=== 📚 SUPPORTS ===")
    afficher_supports(supports)

    print("\n=== 👥 ADHÉRENTS ===")
    afficher_adherents(adherents)

    print("\n=== 📝 EMPRUNTS ===")
    afficher_emprunts(emprunts)


def ajouter_support():
    print("\n=== Quel type de support voulez-vous ajouter? ===")
    print("1. 📖 Livre")
    print("2. 💿 CD-ROM")
    print("3. 📰 Magazine")

    choix = input("\nVotre choix : ")

    id = input("ID du support : ")
    titre = input("Titre : ")

    if choix == "1":
        auteur = input("Auteur : ")
        nb_pages = int(input("Nombre de pages : "))
        return Livre(id, titre, True, auteur, nb_pages)
    elif choix == "2":
        editeur = input("Éditeur : ")
        capacite = int(input("Capacité (Mo) : "))
        return CD_ROM(id, titre, True, editeur, capacite)
    elif choix == "3":
        editeur = input("Éditeur : ")
        numero = int(input("Numéro de publication : "))
        date_pub = input("Date de publication (YYYY-MM-DD) : ")
        date = datetime.datetime.strptime(date_pub, "%Y-%m-%d").date()
        return Magazine(id, titre, True, editeur, numero, date)
    else:
        print("❌ Choix invalide!")
        return None


def ajouter_adherent():
    print("\n=== Nouvel adhérent ===")
    id = input("ID de l'adhérent : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    adresse = input("Adresse : ")
    telephone = input("Téléphone : ")
    email = input("Email : ")
    return Adherent(id, nom, prenom, adresse, telephone, email)


def afficher_statistiques(emprunts):
    total_emprunts = len(emprunts)
    emprunts_en_cours = len([emp for emp in emprunts if not emp.estRendu()])
    emprunts_retournes = len([emp for emp in emprunts if emp.estRendu()])

    print("\n===========================================")
    print("         STATISTIQUES DES EMPRUNTS        ")
    print("-------------------------------------------")
    print(f"  Total des emprunts: {total_emprunts}")
    print(f"  Emprunts en cours: {emprunts_en_cours}")
    print(f"  Emprunts retournés: {emprunts_retournes}")
    if total_emprunts > 0:
        taux = (emprunts_retournes / total_emprunts) * 100
        print(f"  Taux de retour: {taux:.1f}%")
    print("===========================================")


def afficher_details_emprunt(emprunts):
    if not emprunts:
        print("\n===========================================")
        print("        Aucun emprunt enregistré!        ")
        print("===========================================")
        return

    print("\n===========================================")
    print("            DÉTAILS DES EMPRUNTS       ")
    print("-------------------------------------------")

    for i, emprunt in enumerate(emprunts):
        status = "Retourné" if emprunt.estRendu() else "En cours"
        print(f"  #{i + 1:<3} {emprunt.Support.Titre:<45}")

    try:
        choix = int(input("\nChoisir le numéro de l'emprunt (0 pour retour): "))
        if choix == 0:
            return
        if 1 <= choix <= len(emprunts):
            emprunt = emprunts[choix - 1]
            print("\n===========================================")
            print("                   DÉTAILS DE L'EMPRUNT      ")
            print("-------------------------------------------")
            print(f"  Support: {emprunt.Support.Titre:<43}")
            print(f"  Adhérent: {emprunt.Adherent.Nom} {emprunt.Adherent.Prenom:<35}")
            print(f"  Date d'emprunt: {emprunt.DateEmprunt}")
            if emprunt.estRendu():
                print(f"  Date de retour: {emprunt.DateRetour}")
            print(f"  Statut: {status:<45}")
            print("===========================================")
        else:
            print("              Numéro d'emprunt invalide!                  ")
    except ValueError:
        print("                 Entrée invalide!                         ")


def retourner_emprunt(emprunts):
    if not emprunts:
        print("\n===========================================")
        print("        Aucun emprunt enregistré!        ")
        print("===========================================")
        return

    print("\n===========================================")
    print("                   Gestion des retours        ")
    print("-------------------------------------------")
    print("  1. 🔄 Retourner un emprunt")
    print("  2. 📅 Modifier une date de retour")
    print("  3. 📋 Voir tous les emprunts")
    print("  0. 🚪 Quitter")
    print("===========================================")

    choix = input("\nVotre choix : ")

    if choix == "1":
        # Afficher tous les emprunts avec leur statut
        print("\n===========================================")
        print("                   Tous les emprunts        ")
        print("-------------------------------------------")
        for emprunt in emprunts:
            status = "Retour prévu: " + str(emprunt.DateRetour) if emprunt.DateRetour else "🔄 En cours"
            dispo = "✅ Disponible" if emprunt.Support.estDiponible() else "❌ Indisponible"
            print(f"  {emprunt.id} {emprunt.Support.Titre:<45}")
            print(f"       Adhérent: {emprunt.Adherent.Nom} {emprunt.Adherent.Prenom:<35}")
            print(f"       Statut: {status:<45}")
            print("-------------------------------------------")
        print("===========================================")

        try:
            emprunt_id = input("\nEntrez l'ID de l'emprunt (ex: E001) : ")
            # Rechercher l'emprunt par son ID
            emprunt = next((e for e in emprunts if e.id == emprunt_id), None)
            
            if emprunt:
                print("\nDate de retour :")
                print("1. Aujourd'hui")
                print("2. Autre date")
                choix_date = input("Votre choix (1-2) : ")

                if choix_date == "1":
                    date_retour = datetime.date.today()
                elif choix_date == "2":
                    while True:
                        try:
                            date_str = input("Entrez la date de retour (YYYY-MM-DD) : ")
                            date_retour = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                            if date_retour < emprunt.DateEmprunt:
                                print("❌ La date de retour ne peut pas être antérieure à la date d'emprunt!")
                                continue
                            break
                        except ValueError:
                            print("❌ Format de date invalide! Utilisez le format YYYY-MM-DD")
                else:
                    print("❌ Choix invalide!")
                    return

                emprunt.retourner(date_retour)
                status = "disponible" if emprunt.Support.estDiponible() else "indisponible"
                print(f"✅ Date de retour mise à jour avec succès! Le support est maintenant {status}.")
            else:
                print("❌ ID d'emprunt invalide!")
        except ValueError:
            print("❌ Entrée invalide!")

    elif choix == "2":
        # Afficher tous les emprunts avec leur date de retour
        print("\n===========================================")
        print("              Tous les emprunts        ")
        print("-------------------------------------------")
        for i, emprunt in enumerate(emprunts):
            status = "📅 Retour prévu: " + str(emprunt.DateRetour) if emprunt.DateRetour else "🔄 En cours"
            dispo = "��� Disponible" if emprunt.Support.estDiponible() else "❌ Indisponible"
            print(f"  #{i + 1:<3} {emprunt.Support.Titre:<45}")
            print(f"       Adhérent: {emprunt.Adherent.Nom} {emprunt.Adherent.Prenom:<35}")
            print(f"       Statut: {status:<45}")
            if i < len(emprunts):
                print("-------------------------------------------")
        print("===========================================")

        try:
            emprunt_idx = int(input("\nChoisir le numéro de l'emprunt à modifier : "))
            if 0 <= emprunt_idx < len(emprunts):
                emprunt = emprunts[emprunt_idx]

                while True:
                    try:
                        date_str = input("Nouvelle date de retour (YYYY-MM-DD) : ")
                        nouvelle_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                        if nouvelle_date < emprunt.DateEmprunt:
                            print("❌ La date de retour ne peut pas être antérieure à la date d'emprunt!")
                            continue
                        emprunt.retourner(nouvelle_date)
                        status = "disponible" if emprunt.Support.estDiponible() else "indisponible"
                        print(f"✅ Date de retour modifiée avec succès! Le support est maintenant {status}.")
                        break
                    except ValueError:
                        print("❌ Format de date invalide! Utilisez le format YYYY-MM-DD")
            else:
                print("              Numéro d'emprunt invalide!                  ")
        except ValueError:
            print("                 Entrée invalide!                         ")

    elif choix == "3":
        # Voir tous les emprunts
        print("\n===========================================")
        print("             Tous les emprunts        ")
        print("-------------------------------------------")
        for i, emprunt in enumerate(emprunts):
            status = "📅 Retour prévu: " + str(emprunt.DateRetour) if emprunt.DateRetour else "🔄 En cours"
            dispo = "✅ Disponible" if emprunt.Support.estDiponible() else "❌ Indisponible"
            print(f"  #{i + 1:<3} {emprunt.Support.Titre:<45}")
            print(f"       Adhérent: {emprunt.Adherent.Nom} {emprunt.Adherent.Prenom:<35}")
            print(f"       Statut: {status:<45}")
            if i < len(emprunts):
                print("-------------------------------------------")
        print("===========================================")

    else:
        print("                 Entrée invalide!                         ")


def afficher_tableau(headers, data):
    formatted_data = [[str(cell) for cell in row] for row in data]
    print(tabulate(formatted_data, 
                  headers=headers, 
                  tablefmt="grid", 
                  stralign="left",
                  numalign="left"))


def afficher_emprunts_en_cours(emprunts):
    print("\n===========================================")
    print("          EMPRUNTS EN COURS              ")
    print("===========================================")

    emprunts_en_cours = [e for e in emprunts if not e.estRendu()]
    if emprunts_en_cours:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max", "Jours écoulés"]
        data = [
            [
                e.id,
                e.Support.Titre,
                f"{e.Adherent.Nom} {e.Adherent.Prenom}",
                e.DateEmprunt,
                e.DateRetourMaximale,
                f"{e.duree_emprunt()} jours"
            ]
            for e in emprunts_en_cours
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Aucun emprunt en cours")


def afficher_emprunts_retard(emprunts):
    print("\n===========================================")
    print("          EMPRUNTS EN RETARD              ")
    print("===========================================")

    aujourd_hui = datetime.date.today()

    emprunts_retard = [
        e for e in emprunts
        if not e.estRendu() and aujourd_hui > e.DateRetourMaximale
    ]

    if emprunts_retard:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max", "Jours retard", "Jours écoulés"]
        data = [
            [
                e.id,
                e.Support.Titre,
                f"{e.Adherent.Nom} {e.Adherent.Prenom}",
                e.DateEmprunt,
                e.DateRetourMaximale,
                (aujourd_hui - e.DateRetourMaximale).days,
                f"{e.duree_emprunt()} jours"
            ]
            for e in emprunts_retard
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Aucun emprunt en retard")


def afficher_tous_emprunts(emprunts):
    print("\n===========================================")
    print("        LISTE COMPLÈTE DES EMPRUNTS       ")
    print("===========================================")

    if emprunts:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max", "Statut", "Jours écoulés"]
        data = [
            [
                e.id,
                e.Support.Titre,
                f"{e.Adherent.Nom} {e.Adherent.Prenom}",
                e.DateEmprunt,
                e.DateRetourMaximale,
                "En retard" if (not e.DateRetour and datetime.date.today() > e.DateRetourMaximale)
                else "En cours" if not e.DateRetour
                else "Retourné le " + str(e.DateRetour),
                f"{e.duree_emprunt()} jours"
            ]
            for e in emprunts
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Aucun emprunt enregistré")


def afficher_emprunts_adherent(emprunts, id_adherent):
    print("\n===========================================")
    print(f"     EMPRUNTS DE L'ADHÉRENT {id_adherent}    ")
    print("===========================================")

    emprunts_adherent = [e for e in emprunts if e.Adherent.id == id_adherent]
    if emprunts_adherent:
        headers = ["Support", "Date emprunt", "Date retour max", "Statut"]
        data = [
            [
                e.Support.Titre,
                e.DateEmprunt,
                e.DateRetourMaximale,
                "Retourné" if e.DateRetour else "En cours"
            ]
            for e in emprunts_adherent
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt trouvé pour cet adhérent")


def afficher_emprunts_support(emprunts, id_support):
    print("\n===========================================")
    print(f"      EMPRUNTS DU SUPPORT {id_support}     ")
    print("===========================================")

    emprunts_support = [e for e in emprunts if e.Support.id_support == id_support]
    if emprunts_support:
        headers = ["Adhérent", "Date emprunt", "Date retour max", "Statut"]
        data = [
            [
                f"{e.Adherent.Nom} {e.Adherent.Prenom}",
                e.DateEmprunt,
                e.DateRetourMaximale,
                "Retourné" if e.DateRetour else "En cours"
            ]
            for e in emprunts_support
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt trouvé pour ce support")


def creer_emprunt(emprunts, supports):
    print("\n===========================================")
    print("          CRÉATION D'UN EMPRUNT          ")
    print("-------------------------------------------")

    try:
        # Saisie des informations de l'adhérent
        print("\nInformations de l'adhérent:")
        id_adherent = input("ID Adhérent: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        email = input("Email: ")
        telephone = input("Téléphone: ")

        adherent = Adherent(
            id=id_adherent,
            Nom=nom,
            Prenom=prenom,
            Email=email,
            Telephone=telephone
        )

        # Utilisation de la fonction ajouter_support
        print("\nInformations du support:")
        support = ajouter_support()
        if support is None:
            raise ValueError("Échec de la création du support")
        supports.append(support)

        # Saisie de la date d'emprunt
        print("\n===========================================")
        print("        DATE D'EMPRUNT")
        print("-------------------------------------------")
        print("1. Utiliser la date d'aujourd'hui")
        print("2. Spécifier une autre date")
        print("-------------------------------------------")

        choix_date_emprunt = input("\nVotre choix (1 ou 2): ")

        if choix_date_emprunt == "2":
            try:
                date_str = input("Date d'emprunt (YYYY-MM-DD): ")
                date_emprunt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date_emprunt > datetime.date.today():
                    raise ValueError("La date d'emprunt ne peut pas être dans le futur")
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation de la date d'aujourd'hui")
                date_emprunt = datetime.date.today()
        else:
            date_emprunt = datetime.date.today()

        # Définition de la date maximale de retour
        print("\n===========================================")
        print("     DATE MAXIMALE DE RETOUR     ")
        print("-------------------------------------------")
        print("1. Entrer le nombre de jours maximum")
        print("2. Entrer directement la date maximale")
        print("3. Utiliser le délai par défaut (14 jours)")
        print("-------------------------------------------")

        choix_date = input("\nVotre choix (1, 2 ou 3): ")

        # Création de l'emprunt
        id_emprunt = f"E{len(emprunts) + 1:03d}"
        date_retour_max = None

        if choix_date == "1":
            try:
                nb_jours = int(input("Nombre de jours maximum avant retour: "))
                if nb_jours <= 0:
                    raise ValueError("Le nombre de jours doit être positif")
                date_retour_max = date_emprunt + datetime.timedelta(days=nb_jours)
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation du délai par défaut (14 jours)")
                date_retour_max = date_emprunt + datetime.timedelta(days=14)

        elif choix_date == "2":
            try:
                date_str = input("Date maximale de retour (YYYY-MM-DD): ")
                date_retour_max = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date_retour_max <= date_emprunt:
                    raise ValueError("La date de retour doit être postérieure à la date d'emprunt")
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation du délai par défaut (14 jours)")
                date_retour_max = date_emprunt + datetime.timedelta(days=14)

        else:  # choix_date == "3" ou autre
            print("Utilisation du délai par défaut (14 jours)")
            date_retour_max = date_emprunt + datetime.timedelta(days=14)

        nouvel_emprunt = Emprunt(id_emprunt, support, adherent, date_emprunt, None)
        nouvel_emprunt.DateRetourMaximale = date_retour_max
        emprunts.append(nouvel_emprunt)

        print("\n===========================================")
        print("✅ Emprunt créé avec succès!")
        print(f"ID Emprunt: {id_emprunt}")
        print(f"Date d'emprunt: {date_emprunt}")
        print(f"Date maximale de retour: {date_retour_max}")
        print("===========================================")

    except ValueError as e:
        print(f"\n❌ Erreur: {e}")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")


def main():
    emprunts = []
    supports = []

    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            # Modifier cette ligne pour passer la liste des supports
            creer_emprunt(emprunts, supports)

        elif choix == "2":
            # Retourner un emprunt
            retourner_emprunt(emprunts)

        elif choix == "3":
            # Afficher les détails d'un emprunt
            afficher_details_emprunt(emprunts)

        elif choix == "4":
            # Afficher les emprunts en cours
            afficher_emprunts_en_cours(emprunts)

        elif choix == "5":
            # Afficher les emprunts d'un adhérent
            id_adherent = input("Entrez l'ID de l'adhérent : ")
            afficher_emprunts_adherent(emprunts, id_adherent)

        elif choix == "6":
            # Afficher les emprunts d'un support
            id_support = input("Entrez l'ID du support : ")
            afficher_emprunts_support(emprunts, id_support)

        elif choix == "7":
            # Afficher les statistiques
            afficher_statistiques(emprunts)

        elif choix == "8":
            # Afficher tous les emprunts
            afficher_tous_emprunts(emprunts)

        elif choix == "9":
            # Afficher les emprunts en retard
            afficher_emprunts_retard(emprunts)

        elif choix == "10":
            # Afficher tous les supports
            afficher_supports(supports)

        elif choix == "0":
            print("\n===========================================")
            print("               Au revoir!                 ")
            print("===========================================")
            break

        else:
            print("\nChoix invalide! Veuillez réessayer.")


if __name__ == "__main__":
    main()












