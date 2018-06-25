# Generated by Django 2.0.6 on 2018-06-25 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180625_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('web.user',),
        ),
    ]