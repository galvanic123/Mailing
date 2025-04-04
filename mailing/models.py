from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """Получатель рассылки(модель клиента)"""
    email =models.EmailField(unique=True, verbose_name="e-male", help_text="Введите e-mail")
    full_name = models.CharField(max_length=100, verbose_name="ФИО", help_text="Введите как Вас зовут")
    comment = models.TextField(blank=True, null=True, verbose_name="комментарий", help_text="Добавьте комментарий")
    is_active = models.BooleanField(default=True, verbose_name="активность")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Получатель", help_text="Укажите получателя", blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"


    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = [
            'full_name',
        ]


class Message(models.Model):
    """Модель сообщения для рассылки"""
    subject = models.CharField(verbose_name='Тема письма', max_length=255)
    body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, related_name='messages')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    """Рассылка"""
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
        ]

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата первой отправки')
    end_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата окончания отправки')
    status = models.CharField(
        verbose_name='Статус',
        max_length=10,
        choices=STATUS_CHOICES,
        default='created',
    )
    is_active = models.BooleanField(
        default=True, verbose_name="активна", null=True, blank=True
    )
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE, null=True,
        blank=True,)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='Получатели')
    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return f"Рассылка #{self.id} ({self.get_status_display()})"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status']


class MailingAttempt(models.Model):
    """Модель попытки рассылки"""
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    date_time_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')
    sending_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='success', verbose_name='Статус попытки рассылки',)

    def __str__(self):
        return f"{self.date_time_attempt} '{self.sending_status}'"

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['date_time_attempt', 'sending_status']




