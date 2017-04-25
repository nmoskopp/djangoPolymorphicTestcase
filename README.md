This Django application demonstrates a bug in django-polymorphic.

The application `djangoPolymorphicTestcase` has three model classes:
* `Base`, a `polymorphic.models.PolymorphicModel`
* `VariantA`, which inherits from `Base`
* `VariantB`, which inherits from `Base`

The test creates a `VariantA` object with primary key of `DUPLICATE`.
It then creates a `VariantB` object with a primary key of `DUPLICATE`.
As a result we do not have two objects, but a single `VariantB` object.
Accessing it via `VariantA.objects()` is possible, but throws `TypeError`.

# How to test
`PYTHONPATH=/usr/lib/python3/dist-packages/ python3 ./manage.py test`