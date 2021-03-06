# Generated by Django 3.0.7 on 2020-06-09 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WalkEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('distance', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('weight', models.CharField(max_length=4)),
                ('image_url', models.CharField(max_length=600, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
