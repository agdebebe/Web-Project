# Generated by Django 2.2 on 2019-12-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('primaryCategory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, upload_to='products/')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('preview_text', models.TextField(max_length=200, verbose_name='Preview Text')),
                ('detail_text', models.TextField(max_length=1000, verbose_name='Detail Text')),
                ('price', models.FloatField()),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]
