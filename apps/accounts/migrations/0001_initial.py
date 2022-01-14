# Generated by Django 3.2.10 on 2022-01-14 14:36

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='/uploads/default.jpg', null=True, upload_to='uploads/')),
                ('email_notif', models.BooleanField(default=True, verbose_name='Get Email Notifications')),
                ('verified', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('follows', models.ManyToManyField(related_name='followed_by', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
