# Generated by Django 4.2.4 on 2023-08-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('comision', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('fecha_de_entrega', models.DateField(auto_now_add=True)),
                ('esta_aprobado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('profesion', models.CharField(max_length=128)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
