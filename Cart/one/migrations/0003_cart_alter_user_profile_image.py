# Generated by Django 5.1.3 on 2024-12-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('product_count', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/profile.jpg', upload_to=''),
        ),
    ]
