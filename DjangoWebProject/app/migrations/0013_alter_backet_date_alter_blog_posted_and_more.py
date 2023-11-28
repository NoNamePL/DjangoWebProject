# Generated by Django 4.2.5 on 2023-11-28 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0012_alter_backet_date_alter_backet_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backet",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 6, 2, 23, 204524),
                verbose_name="Дата добавления в корзину",
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 6, 2, 23, 203362),
                verbose_name="Опубликована",
            ),
        ),
        migrations.AlterField(
            model_name="catalogitem",
            name="Catalogdate",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 6, 2, 23, 204170),
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 6, 2, 23, 203783),
                verbose_name="Дата комментария",
            ),
        ),
    ]
