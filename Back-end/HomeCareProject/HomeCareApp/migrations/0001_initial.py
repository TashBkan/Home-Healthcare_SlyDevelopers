# Generated by Django 4.1.1 on 2022-09-12 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=30, null=True)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('direccion', models.CharField(max_length=50, null=True)),
                ('longitud', models.CharField(max_length=50, null=True)),
                ('latitud', models.CharField(max_length=50, null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('ciudad', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('registroMedico', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='HomeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosticos', models.CharField(max_length=30)),
                ('signos', models.CharField(max_length=30)),
                ('oximetria', models.CharField(max_length=30)),
                ('FrecRespiratoria', models.CharField(max_length=30)),
                ('FrecCardiaca', models.CharField(max_length=30)),
                ('Temperatura', models.CharField(max_length=30)),
                ('presionArterial', models.CharField(max_length=30)),
                ('glicemias', models.CharField(max_length=30)),
                ('sugerencias_cuidado', models.CharField(max_length=300)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_clinica', to='HomeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enfermero', to='HomeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auxiliar', to='HomeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Acompañante',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompañante', to='HomeCareApp.paciente')),
            ],
        ),
    ]