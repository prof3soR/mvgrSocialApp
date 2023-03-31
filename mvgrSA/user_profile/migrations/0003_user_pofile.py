# Generated by Django 4.1.7 on 2023-03-31 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0002_remove_user_post_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_pofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('dp', models.ImageField(upload_to='')),
                ('mobile', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]