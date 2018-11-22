import pytest
from MVP2.tout_MVP2 import *

class test_Tout_MVP2(pytest.TestCase):
    def test_listes_de_variables(self):
        self.assertEqual(listes_de_variables("EventCandidatA.rb"), ["self.table_name", "KIND", "availabilities",
        "openings", "appointments", "slots"])

    def test_remove_specials(self):
        self.assertEqual(remove_specials("self.availabilities(start_date,"), "self.availabilities")
        self.assertEqual(remove_specials("appointment?\n"),"appointment?" )

    def test_controle_nom_variable(self):
        self.assertEqual(controle_nom_variable("EventCandidatA.rb"), 0 )

    def test_calcul_pourcentage_fonctions_mal_nommees(self):
        self.assertEqual(calcul_pourcentage_fonctions_mal_nommees("EventCandidatA.rb"),0)
        self.assertEquals(calcul_pourcentage_fonctions_mal_nommees("EventCandidateB.rb"), 0)

    def test_majuscule_fonction(self):
        self.assertEqual(majuscule_fonction("EventCandidatA.rb"), 0)

    def test_transformation_fichier(self):
        self.assertEqual(type(transformation_fichier("EventCandidatA.rb")),list)
        self.assertEqual(transformation_fichier("EventCandidatA.rb")[0], "class EventCandidatA < ApplicationRecord\n")

    def test_list_functions(self):
        self.assertEqual(list_functions("EventCandidatA.rb"), ["opening?", "appointment?", "self.availabilities",
            "starts_at_cannot_be_greater_than_ends_at", "ends_at_cannot_be_a_different_day_than_starts_at",
            "hours_must_be_a_multiple_of_thirty_minutes", "same_kind_of_event_cannot_be_in_a_same_time_slot",
            "ppointment_cannot_be_outside_of_opening_hours", "self.slots_available", "self.split_into_slots"])

    def test_suppr_space(self):
        self.assertEqual(suppr_space("Le nouveau document"), "Lenouveaudocument")
        self.assertEqual(suppr_space("Le nouveau document\n est ici"), "Lenouveaudocumentestici")

    def test_suppr_blank_and_end(self):
        self.assertEqual(suppr_blank_and_end(" "),"" )
        self.assertEqual(suppr_blank_and_end("Le document\n end"), "Le document")

    def test_egalitelist(self):
        self.assertEqual(egalitelist("abc", "abcd"), (("abc ", "abcd")) )
        self.assertNotEqual(egalitelist("abcd", "abc"), ("abcd ", "abc"))

    def test_coeff_dice(self):
        self.assertEqual(type(coeff_dice(["abc", "def"], .02)), float)

    def test_run_script_MVP2(self):
        self.assertEqual(type(run_script_MVP2("EventCandidatA.rb")), dict)
        self.assertEqual(run_script_MVP2("EventCandidatA.rb")["liste_de_variables"], ["self.table_name", "KIND",
        "availabilities","openings", "appointments", "slots"])
        self.assertEqual(type(run_script_MVP2("EventCandidatA.rb")["pourcentage_fonctions_mal_nommées"]), float)
        self.assertEqual(type(run_script_MVP2("EventCandidatA.rb")["liste_des_fonctions"]), list)
