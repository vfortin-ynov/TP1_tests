import unittest
from fonctions import (
    additionner, est_pair, valider_email, calculer_moyenne, 
    convertir_temperature, diviser, valider_mot_de_passe,
    ErreurValidation, ErreurEmailInvalide, ErreurNoteInvalide, ErreurMotDePasse
)

class TestFonctions(unittest.TestCase):

    #region Tests pour additionner
    def test_additionner_cas_positif(self):
        """Test addition avec nombres positifs"""
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_additionner_cas_negatif(self):
        """Test addition avec nombres négatifs"""
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)
        
    def test_additionner_type_incorrect(self):
        """Test addition avec des types incorrects"""
        with self.assertRaises(TypeError):
            additionner("2", 3)
        with self.assertRaises(TypeError):
            additionner(2, "3")
    #endregion

    #region Tests pour est_pair
    def test_est_pair_vrai(self):
        """Test si un nombre pair retourne True"""
        self.assertTrue(est_pair(2))
        self.assertTrue(est_pair(0))
        self.assertTrue(est_pair(-4))

    def test_est_pair_faux(self):
        """Test si un nombre impair retourne False"""
        self.assertFalse(est_pair(1))
        self.assertFalse(est_pair(-3))
        self.assertFalse(est_pair(99))
        
    def test_est_pair_type_incorrect(self):
        """Test avec un type incorrect"""
        with self.assertRaises(TypeError):
            est_pair(2.5)
        with self.assertRaises(TypeError):
            est_pair("deux")
    #endregion

    #region Tests pour valider_email
    def test_valider_email_valide(self):
        """Test avec des emails valides"""
        self.assertTrue(valider_email("test@example.com"))
        self.assertTrue(valider_email("user.name@domain.fr"))
        self.assertTrue(valider_email("a@b.c"))

    def test_valider_email_invalide(self):
        """Test avec des emails invalides"""
        with self.assertRaises(ErreurEmailInvalide):
            valider_email("test.example.com")  # Sans arobase
            
        with self.assertRaises(ErreurEmailInvalide):
            valider_email("test@examplecom")  # Sans point
            
        with self.assertRaises(ErreurEmailInvalide):
            valider_email("")  # Vide
            
        with self.assertRaises(ErreurEmailInvalide):
            valider_email("test@")  # Arobase sans domaine
            
        with self.assertRaises(ErreurEmailInvalide):
            valider_email("test.")  # Point sans domaine complet
            
    def test_valider_email_type_incorrect(self):
        """Test avec un type incorrect"""
        with self.assertRaises(TypeError):
            valider_email(123)  # Nombre au lieu de chaîne
    #endregion

    #region Tests pour calculer_moyenne
    def test_calculer_moyenne_normal(self):
        """Test de calcul de moyenne avec des valeurs normales"""
        self.assertEqual(calculer_moyenne([10, 20, 30]), 20)
        self.assertEqual(calculer_moyenne([1, 2, 3, 4]), 2.5)
        self.assertEqual(calculer_moyenne([-5, 0, 5]), 0)
        self.assertEqual(calculer_moyenne([100, 200, 300]), 200)

    def test_calculer_moyenne_liste_vide(self):
        """Test de calcul de moyenne avec une liste vide"""
        with self.assertRaises(ValueError):
            calculer_moyenne([])

    def test_calculer_moyenne_valeur_unique(self):
        """Test de calcul de moyenne avec une seule valeur"""
        self.assertEqual(calculer_moyenne([5]), 5)
        
    def test_calculer_moyenne_notes_invalides(self):
        """Test avec des notes invalides"""
        with self.assertRaises(TypeError):
            calculer_moyenne([10, "15", 20])  # Chaîne au lieu de nombre
            
        with self.assertRaises(TypeError):
            calculer_moyenne("pas une liste")  # Mauvais type
    #endregion

    #region Tests pour convertir_temperature
    def test_convertir_temperature_zero(self):
        """Test de conversion de 0°C en Fahrenheit"""
        self.assertEqual(convertir_temperature(0), 32)

    def test_convertir_temperature_eau_bouillante(self):
        """Test de conversion de 100°C (eau bouillante) en Fahrenheit"""
        self.assertEqual(convertir_temperature(100), 212)
        
    def test_convertir_temperature_negatif(self):
        """Test de conversion de température négative"""
        self.assertEqual(convertir_temperature(-40), -40)
        
    def test_convertir_temperature_invalide(self):
        """Test avec une température invalide"""
        with self.assertRaises(ValueError):
            convertir_temperature(-300)  # En dessous du zéro absolu
            
        with self.assertRaises(TypeError):
            convertir_temperature("cent")  # Type incorrect
    #endregion

    #region Tests pour diviser
    def test_diviser_normal(self):
        """Test de division avec des valeurs normales"""
        self.assertEqual(diviser(10, 2), 5)
        self.assertEqual(diviser(7, 2), 3.5)
        self.assertEqual(diviser(-6, 3), -2)

    def test_diviser_par_zero(self):
        """Test que la division par zéro lève une exception ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            diviser(10, 0)
            
    def test_diviser_type_incorrect(self):
        """Test avec des types incorrects"""
        with self.assertRaises(TypeError):
            diviser("dix", 2)
            
        with self.assertRaises(TypeError):
            diviser(10, "deux")
    #endregion

    #region Tests mot de passe
    def test_valider_mot_de_passe_valide(self):
        """Test avec un mot de passe valide"""
        self.assertTrue(valider_mot_de_passe("Test123!"))
        self.assertTrue(valider_mot_de_passe("Autre.Mot2Passe"))

    def test_valider_mot_de_passe_invalide(self):
        """Test avec des mots de passe invalides"""
        with self.assertRaises(ErreurMotDePasse):
            valider_mot_de_passe("Test!")  # Trop court
            
        with self.assertRaises(ErreurMotDePasse):
            valider_mot_de_passe("test123!")  # Pas de majuscule
            
        with self.assertRaises(ErreurMotDePasse):
            valider_mot_de_passe("TEST123!")  # Pas de minuscule
            
        with self.assertRaises(ErreurMotDePasse):
            valider_mot_de_passe("TestTest!")  # Pas de chiffre
            
        with self.assertRaises(ErreurMotDePasse):
            valider_mot_de_passe("Test1234")  # Pas de caractère spécial
            
    def test_valider_mot_de_passe_type_incorrect(self):
        """Test avec un type incorrect"""
        with self.assertRaises(TypeError):
            valider_mot_de_passe(12345678)  # Nombre au lieu de chaîne
    #endregion

# Permet d'exécuter les tests
if __name__ == '__main__':
    unittest.main()
