from MVP1.tout_MVP1 import *

def test_remove_special():
    assert remove_special('starts_at_cannot_be_greater_than_ends_at\n') == 'starts_at_cannot_be_greater_than_ends_at'
    assert remove_special('self.availabilities(start_date,') == 'self.availabilities'

def test_list_functions():
    assert list_functions("EventCandidatA.rb") == ['opening?', 'appointment?', 'self.availabilities',
                    'starts_at_cannot_be_greater_than_ends_at', 'ends_at_cannot_be_a_different_day_than_starts_at',
                    'hours_must_be_a_multiple_of_thirty_minutes', 'same_kind_of_event_cannot_be_in_a_same_time_slot',
                    'appointment_cannot_be_outside_of_opening_hours','self.slots_available','self.split_into_slots']
    assert len(list_functions("EventCandidatA.rb")) == 10
    assert list_functions("EventCandidateB.rb") == ["self.availabilities", "self.event_specific_query",
                                                    "self.event_recurring_query", "day_schedule_creator",
                                                    "self.schedule_availibilities", "date_order_validation",
                                                    "event_same_date"]

def test_compte_commentaires():
    assert compte_commentaires("EventCandidatA.rb") == 0
    # le nombre de # ne correspond pas au nombre de commentaires avec la convention adoptée
    assert compte_commentaires("EventCandidateB.rb") != 21
    assert compte_commentaires("EventCandidateB.rb") == 19
    assert compte_commentaires("EventCandidateC.rb") == 8

def test_list_tests():
    assert list_tests("EventCandidatATest.rb") != None
    assert len(list_tests("EventCandidatATest.rb")) == 13

def test_count_boucles():
    assert count_boucles("EventCandidatA.rb") == 3

def test_listes_de_variables():
    assert len(listes_de_variables("EventCandidatA.rb")) == 6
