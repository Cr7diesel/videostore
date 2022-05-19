# Generated by Django 3.2.12 on 2022-02-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профайл', 'verbose_name_plural': 'Профайлы'},
        ),
        migrations.AddField(
            model_name='profile',
            name='accept',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='male', max_length=50, verbose_name=(('male', 'Мужской'), ('female', 'Женский'))),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='pictures/user_icon.png', upload_to='user_images', verbose_name='Фото пользователя'),
        ),
    ]
