from django.db.models import DateTimeField, Model


class BaseModels(Model):
    create_at = DateTimeField(auto_now_add=True, db_index=True)
    update_at = DateTimeField(auto_now=True, db_index = True)

    class Meta:
        abstract = True