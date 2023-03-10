# Generated by Django 4.1.3 on 2022-12-15 12:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated'),
        ('pedidos', '0002_remove_lineapedido_pedido_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineapedido',
            name='pedido',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido' , null= True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lineapedido',
            name='producto',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='tienda.producto', null= True),
            preserve_default=False,
        ),
    ]
