from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Service(models.Model):
    name = models.CharField('Название', max_length=128)
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    is_active = models.BooleanField('Активность', help_text='', default=True)

    class Meta:
        verbose_name = _("Сервис")
        verbose_name_plural = _("Сервисы")

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    phone = models.CharField('Телефон', max_length=16)

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name

    def format_phone(self):
        area = self.phone[1:4]
        rest = self.phone[4:7] + '-' + self.phone[7:9] + '-' + self.phone[9:]
        return self.phone[0] + ' (' + area + ') ' + rest


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, verbose_name='Услуга')
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name='Клиент')
    reserved_at = models.DateTimeField('Дата')

    class Meta:
        verbose_name = _("Запись")
        verbose_name_plural = _("Записи")
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unqiue_user_per_date',
                fields=['user', 'reserved_at']
            )
        ]

    def __str__(self):
        return str(self.service)