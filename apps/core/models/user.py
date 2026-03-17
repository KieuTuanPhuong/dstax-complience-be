from django.db import models

from libs.models import BaseModel


class Role(models.TextChoices):
    DSTAX_ADMIN = "DSTAX_ADMIN", "DSTax_Admin"
    DSTAX_PREPARER = "DSTAX_PREPARER", "DSTax_Preparer"
    CLIENT_ADMIN = "CLIENT_ADMIN", "Client_Admin"
    CLIENT_STAFF = "CLIENT_STAFF", "Client_Staff"


class User(BaseModel):
    role = models.CharField(max_length=20, choices=Role.choices)
    managed_client = models.ForeignKey(
        "Client", blank=True, null=True, on_delete=models.SET_NULL, related_name="users"
    )
    assigned_legal_entities = models.ManyToManyField("LegalEntity", blank=True, related_name="users")

    @property
    def is_dstax_admin(self):
        return self.role == Role.DSTAX_ADMIN

    @property
    def is_dstax_preparer(self):
        return self.role == Role.DSTAX_PREPARER

    @property
    def is_client_admin(self):
        return self.role == Role.CLIENT_ADMIN

    @property
    def is_client_staff(self):
        return self.role == Role.CLIENT_STAFF
