from django_extensions.db.fields import UUIDField

class AutoUUIDField(UUIDField):
    def contribute_to_class(self, cls, name):
        assert not cls._meta.has_auto_field, "A model can't have more than one AutoField."
        super(UUIDField, self).contribute_to_class(cls, name)
        cls._meta.has_auto_field = True
        cls._meta.auto_field = self
