# Generated by Django 2.1.7 on 2019-04-01 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(max_length=65)),
            ],
        ),
    ]
