# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _


# class BaseAbstractUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField(_("email address"), unique=True, db_index=True)
#     phone = models.CharField(_("phone"), max_length=15, unique=True, default="")
#     created_at = models.DateTimeField(_("user creation date"), auto_now_add=True)
#     update_at = models.DateTimeField(_("user modify date"), auto_now=True)

#     REQUIRED_FIELDS = ["phone", "email"]

#     class Meta:
#         abstract = True
