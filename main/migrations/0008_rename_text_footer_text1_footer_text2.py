# Generated by Django 4.2 on 2023-05-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_footer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='text',
            new_name='text1',
        ),
        migrations.AddField(
            model_name='footer',
            name='text2',
            field=models.CharField(default=1, max_length=60, verbose_name='text'),
            preserve_default=False,
        ),
    ]
