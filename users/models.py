from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="Введи номер телефона",
    )
    avatar = models.ImageField(upload_to="photo/avatar", blank=True, null=True, verbose_name="Аватар",
                               help_text="Загрузите аватар")
    country = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )
    is_blocked = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("can_block_user", "Может блокировать пользователя"),
        ]

    def __str__(self):
        return self.email