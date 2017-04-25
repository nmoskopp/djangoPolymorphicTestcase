from django.db import models
from polymorphic.models import PolymorphicModel

class Base(PolymorphicModel):
    id = models.CharField(max_length=128, primary_key=True, verbose_name='ID')

class VariantA(Base):
    pass

class VariantB(Base):
    pass
