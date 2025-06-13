import unittest
from fonctions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser

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
    #endregion

    #region Tests pour valider_email
    def test_valider_email_valide(self):
        """Test avec des emails valides"""
        self.assertTrue(valider_email("test@example.com"))
        self.assertTrue(valider_email("user.name@domain.fr"))
        self.assertTrue(valider_email("a@b.c"))

    def test_valider_email_sans_arobase(self):
        """Test avec un email sans arobase"""
        self.assertFalse(valider_email("test.example.com"))

    def test_valider_email_sans_point(self):
        """Test avec un email sans point"""
        self.assertFalse(valider_email("test@examplecom"))

    def test_valider_email_vide(self):
        """Test avec un email vide"""
        self.assertFalse(valider_email(""))

    def test_valider_email_arobase_sans_domaine(self):
        """Test avec un email contenant un arobase mais sans domaine"""
        self.assertFalse(valider_email("test@"))

    def test_valider_email_point_sans_domaine(self):
        """Test avec un email contenant un point mais sans domaine complet"""
        self.assertFalse(valider_email("test."))
    #endregion

    #region Tests pour calculer_moyenne
    def test_calculer_moyenne_normal(self):
        """Test de calcul de moyenne avec des valeurs normales"""
        self.assertEqual(calculer_moyenne([10, 20, 30]), 20)
        self.assertEqual(calculer_moyenne([1, 2, 3, 4]), 2.5)

    def test_calculer_moyenne_liste_vide(self):
        """Test de calcul de moyenne avec une liste vide"""
        self.assertEqual(calculer_moyenne([]), 0)

    def test_calculer_moyenne_valeur_unique(self):
        """Test de calcul de moyenne avec une seule valeur"""
        self.assertEqual(calculer_moyenne([5]), 5)
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
    #endregion

    #region Tests pour diviser
    def test_diviser_normal(self):
        """Test de division avec des valeurs normales"""
        self.assertEqual(diviser(10, 2), 5)
        self.assertEqual(diviser(7, 2), 3.5)
        self.assertEqual(diviser(-6, 3), -2)

    def test_diviser_par_zero(self):
        """Test que la division par zéro lève une exception ValueError"""
        with self.assertRaises(ValueError):
            diviser(10, 0)
    #endregion

    #region Tests mot de passe
    def test_valider_mot_de_passe_valide(self):
        """Test avec un mot de passe valide"""
        self.assertTrue(valider_mot_de_passe("Test123!"))

    def test_valider_mot_de_passe_trop_court(self):
        """Test avec un mot de passe trop court"""
        self.assertFalse(valider_mot_de_passe("Test!"))

    def test_valider_mot_de_passe_sans_majuscule(self):
        """Test avec un mot de passe sans majuscule"""
        self.assertFalse(valider_mot_de_passe("test123!"))

    def test_valider_mot_de_passe_sans_minuscule(self):
        """Test avec un mot de passe sans minuscule"""
        self.assertFalse(valider_mot_de_passe("TEST123!"))

    def test_valider_mot_de_passe_sans_chiffre(self):
        """Test avec un mot de passe sans chiffre"""
        self.assertFalse(valider_mot_de_passe("Test!"))

    def test_valider_mot_de_passe_sans_special(self):
        """Test avec un mot de passe sans caractère spécial"""
        self.assertFalse(valider_mot_de_passe("Test123"))
    #endregion

# Permet d'exécuter les tests
if __name__ == '__main__':
    unittest.main()
