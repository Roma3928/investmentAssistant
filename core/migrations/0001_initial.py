# Generated by Django 4.0.4 on 2022-05-29 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('symbol', models.CharField(blank=True, max_length=100, null=True)),
                ('exchange', models.CharField(blank=True, max_length=250, null=True)),
                ('rate', models.CharField(blank=True, max_length=50, null=True)),
                ('income', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_to', models.CharField(max_length=30)),
                ('register', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=100)),
                ('lot', models.CharField(max_length=100)),
                ('dividend', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='core.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='core.companycategory'),
        ),
    ]