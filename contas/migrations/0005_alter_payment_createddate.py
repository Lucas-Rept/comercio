# Generated by Django 4.2.5 on 2023-10-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_payment_name_payment_quantity_payment_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
