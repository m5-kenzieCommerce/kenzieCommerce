# Generated by Django 4.1.7 on 2023-03-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_orderedproduct_category_orderedproduct_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderedproduct",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]