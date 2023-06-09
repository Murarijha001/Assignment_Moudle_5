# Generated by Django 4.1.7 on 2023-05-16 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_model', models.CharField(max_length=10)),
                ('product_price', models.IntegerField()),
                ('product_ram', models.IntegerField()),
                ('product_image', models.FileField(upload_to='product_photo')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product_mst')),
            ],
        ),
        migrations.DeleteModel(
            name='Product_sub_category',
        ),
    ]
