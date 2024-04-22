from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    # str fields:
    mobile_phone = models.CharField(
        verbose_name="Мобильный тел.",
        max_length=12,
        null=True,
        blank=True,
    )

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # dunder methods:
    def __str__(self) -> str:
        return f"{self.id} --- {self.email}"

    class Meta:
        db_table = "users"
        ordering = ["-date_joined"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"