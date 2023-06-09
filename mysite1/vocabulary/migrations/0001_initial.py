# Generated by Django 4.1.7 on 2023-05-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lookup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="标题")),
                ("words", models.CharField(max_length=32, verbose_name="原单词")),
                ("translation", models.CharField(max_length=64, verbose_name="译文")),
                ("additon", models.CharField(max_length=64, verbose_name="备注")),
                ("add_time", models.DateTimeField(verbose_name="添加时间")),
            ],
        ),
        migrations.CreateModel(
            name="WordsInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("words", models.CharField(max_length=32, verbose_name="原单词")),
                ("translation", models.CharField(max_length=64, verbose_name="译文")),
                ("additon", models.CharField(max_length=64, verbose_name="备注")),
            ],
        ),
    ]
