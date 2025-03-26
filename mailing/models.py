from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Client(models.Model):
    """Получатель рассылки"""
    email =models.EmailField(unique=True, verbose_name="e-male", help_text="Введите e-mail")
    name = models.CharField(max_length=100, verbose_name="ФИО", help_text="Введите как Вас зовут")
    comment = models.TextField(blank=True, null=True, verbose_name="комментарий", help_text="Добавьте комментарий")
    is_active = models.BooleanField(default=True, verbose_name="активность")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Получатель", help_text="Укажите получателя", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.email}"


    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
        ordering = [
            "name",
        ]

class Mailing(models.Model):
    """Рассылка"""
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    clients = models.ManyToManyField(Client)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Рассылка #{self.id} ({self.get_status_display()})"

class MessageLog(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    error = models.TextField(blank=True)


