# Generated by Django 4.1.7 on 2023-05-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vocabulary", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lookup",
            name="additon",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="备注"
            ),
        ),
        migrations.AlterField(
            model_name="wordsinfo",
            name="additon",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="备注"
            ),
        ),
    ]
