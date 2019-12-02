# Generated by Django 2.2.7 on 2019-12-02 03:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название приложения')),
                ('access_token', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Ключ API')),
            ],
        ),
    ]
