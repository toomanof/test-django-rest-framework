import uuid

from django.db import models


class Application(models.Model):
    ''' Модель 'Приложения'
        Обязательные поля модели:
        id,
        title - Название приложения,
        access_token - Ключ API.
    '''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='Название приложения')
    access_token = models.UUIDField(
        unique=True,
        blank=False,
        null=False,
        default=uuid.uuid4,
        verbose_name='Ключ API')

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

    def create_token(self):
        ''' Метод создания Ключ API '''
        return uuid.uuid4()

    def set_access_Token(self):
        ''' Метод создания и записи в объект ключа API '''
        try:
            self.access_token = self.create_token()
            self.save()
        except Exception as e:
            return 500, (False, e)
        else:
            return 201, True
