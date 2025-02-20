# Generated by Django 3.2.6 on 2021-11-09 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookMng', '0004_auto_20211107_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookMng.bookrating'),
        ),
        migrations.AddField(
            model_name='bookrating',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
