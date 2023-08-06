# Django
from django.test import TestCase

# Project
from fun_facts.models import FunFact


class FunFactTests(TestCase):
    fixtures = [
        'fixtures/fun_facts.json'
    ]

    def test__str__(self) -> None:
        fun_fact = FunFact.objects.first()
        self.assertIsNotNone(fun_fact.__str__())
        self.assertEqual(fun_fact.__str__(), f'{fun_fact.month}/{fun_fact.day}')

    def test_save(self) -> None:
        fun_fact = FunFact.objects.first()
        old_fact = fun_fact.fact
        new_fact = 'ChangedFact'
        fun_fact.fact = 'ChangedFact'
        fun_fact.save()
        self.assertNotEqual(new_fact, old_fact)
        self.assertNotEqual(fun_fact.fact, old_fact)
        self.assertEqual(fun_fact.fact, new_fact)
