def additionner(a, b):
    """Additionne deux nombres"""
    return a * b # ERREUR VOLONTAIRE : * au lieu de +

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def valider_email(email):
    """Valide un email simple (doit contenir @ et .)"""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    return (celsius * 9/5) + 32

def diviser(a, b):
    """Divise deux nombres et retourne une erreur si le diviseur est zéro"""
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro")
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
    if len(mot_de_passe) < 8:
        return False
    
    # Vérification des critères
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in mot_de_passe:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    # Retourne True seulement si tous les critères sont respectés
    return has_uppercase and has_lowercase and has_digit and has_special
