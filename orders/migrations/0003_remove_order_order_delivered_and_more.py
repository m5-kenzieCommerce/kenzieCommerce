# Generated by Django 4.1.7 on 2023-03-08 13:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_user"),
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_delivered",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_in_progress",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_placed",
        ),
        migrations.AddField(
            model_name="order",
            name="buyed_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pedido_realizado", "Pedido Realizado"),
                    ("pedido_em_andamento", "Pedido em Andamento"),
                    ("entregue", "Entregue"),
                ],
                default="pedido_realizado",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="OrderedProduct",
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
                ("totalPrice", models.DecimalField(decimal_places=2, max_digits=8)),
                ("totalQuantity", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordered_products",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordered_products",
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="orders.OrderedProduct", to="products.product"
            ),
        ),
    ]
