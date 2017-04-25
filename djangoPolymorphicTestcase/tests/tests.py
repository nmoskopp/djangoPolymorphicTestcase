from django.test import TestCase
from model_mommy import mommy
from ..models import Base, VariantA, VariantB

class BaseTest(TestCase):
    def setUp(self):
        a = mommy.make(VariantA, id='DUPLICATE')
        a.save()
        b = mommy.make(VariantB, id='DUPLICATE')
        b.save()

    def test_duplicate_count(self):
        # If the following assertion fails, the polymorphic model has failed
        # as queries like “c=VariantA.objects.all()[0]” result in TypeErrors.
        self.assertEqual(VariantA.objects.count(), 0)  # Doesn't trigger bug.

    def test_duplicate_demonstration(self):
        # This demonstrates the actual bug:
        bug_here = VariantA.objects.first()
