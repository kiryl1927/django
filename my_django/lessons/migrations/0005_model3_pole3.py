# Generated by Django 4.2.2 on 2023-06-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_model3'),
    ]

    operations = [
        migrations.AddField(
            model_name='model3',
            name='pole3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lessons.model2'),
            preserve_default=False,
        ),
    ]
