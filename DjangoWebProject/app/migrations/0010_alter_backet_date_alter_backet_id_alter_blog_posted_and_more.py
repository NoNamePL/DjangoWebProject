# Generated by Django 4.2.5 on 2023-11-28 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_backet_quantity_alter_backet_date_alter_blog_posted_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backet",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 5, 45, 15, 791937),
                verbose_name="Дата добавления в корзину",
            ),
        ),
        migrations.AlterField(
            model_name="backet",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 5, 45, 15, 790293),
                verbose_name="Опубликована",
            ),
        ),
        migrations.AlterField(
            model_name="catalogitem",
            name="Catalogdate",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 5, 45, 15, 791428),
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2023, 11, 28, 5, 45, 15, 790863),
                verbose_name="Дата комментария",
            ),
        ),
    ]
