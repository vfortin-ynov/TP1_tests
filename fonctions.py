class ErreurValidation(Exception):
    """Classe de base pour les erreurs de validation"""
    pass

class ErreurEmailInvalide(ErreurValidation):
    """Erreur levée quand un email est invalide"""
    pass

class ErreurNoteInvalide(ErreurValidation):
    """Erreur levée quand une note est invalide"""
    pass

class ErreurMotDePasse(ErreurValidation):
    """Erreur levée quand le mot de passe ne respecte pas les critères"""
    pass

def additionner(a, b):
    """Additionne deux nombres"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les deux paramètres doivent être des nombres")
    return a + b

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    if not isinstance(nombre, int):
        raise TypeError("Le paramètre doit être un entier")
    return nombre % 2 == 0

def valider_email(email):
    """Valide un email simple (doit contenir @ et .)"""
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne de caractères")
        
    if "@" not in email or "." not in email:
        raise ErreurEmailInvalide("Format d'email invalide. Doit contenir @ et .")
    
    # Vérification basique de la structure
    local_part, domain = email.split("@", 1)
    if not local_part or not domain or "." not in domain:
        raise ErreurEmailInvalide("Format d'email invalide")
    
    return True

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes numériques"""
    if not isinstance(notes, (list, tuple)):
        raise TypeError("Le paramètre doit être une liste ou un tuple")
        
    if not notes:
        raise ValueError("La liste des notes ne peut pas être vide")
        
    for note in notes:
        if not isinstance(note, (int, float)):
            raise TypeError("Toutes les notes doivent être des nombres")
            
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    if not isinstance(celsius, (int, float)):
        raise TypeError("La température doit être un nombre")
    if celsius < -273.15:  # Zéro absolu
        raise ValueError("La température ne peut pas être en dessous du zéro absolu (-273.15°C)")
    return (celsius * 9/5) + 32

def diviser(a, b):
    """Divise deux nombres"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les deux paramètres doivent être des nombres")
    if b == 0:
        raise ZeroDivisionError("Le diviseur ne peut pas être zéro")
    return a / b

def valider_mot_de_passe(mot_de_passe):
    """
    Valide un mot de passe selon plusieurs critères:
    - Minimum 8 caractères
    - Au moins une lettre majuscule
    - Au moins une lettre minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial parmi !@#$%^&*()_+-=[]{}|;:,.<>?
    """
    if not isinstance(mot_de_passe, str):
        raise TypeError("Le mot de passe doit être une chaîne de caractères")
        
    erreurs = []
    
    if len(mot_de_passe) < 8:
        erreurs.append("Le mot de passe doit contenir au moins 8 caractères")
    
    # Vérification des critères
    if not any(c.isupper() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins une majuscule")
    if not any(c.islower() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins une minuscule")
    if not any(c.isdigit() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins un chiffre")
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins un caractère spécial")
    
    if erreurs:
        raise ErreurMotDePasse("\n".join(erreurs))
    
    return True
