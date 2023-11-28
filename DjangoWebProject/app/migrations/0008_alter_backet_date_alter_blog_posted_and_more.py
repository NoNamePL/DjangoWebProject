# Generated by Django 4.2.5 on 2023-11-22 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_remove_backet_text_backet_user_alter_backet_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backet",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 22, 6, 14, 32, 320200),
                verbose_name="Дата добавления в корзину",
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 22, 6, 14, 32, 318985),
                verbose_name="Опубликована",
            ),
        ),
        migrations.AlterField(
            model_name="catalogitem",
            name="Catalogdate",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 22, 6, 14, 32, 319825),
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 22, 6, 14, 32, 319417),
                verbose_name="Дата комментария",
            ),
        ),
    ]