# Generated by Django 4.1.1 on 2022-09-20 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rol', models.TextField(default='paciente', max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=30, null=True)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('direccion', models.CharField(max_length=50, null=True)),
                ('longitud', models.CharField(max_length=50, null=True)),
                ('latitud', models.CharField(max_length=50, null=True)),
                ('telefono', models.BigIntegerField()),
                ('ciudad', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rol', models.TextField(default='medico', max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField()),
                ('registroMedico', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='homeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('diagnosticos', models.CharField(max_length=30)),
                ('signos', models.CharField(max_length=30)),
                ('oximetria', models.CharField(max_length=30)),
                ('frecRespiratoria', models.CharField(max_length=30)),
                ('frecCardiaca', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=30)),
                ('presionArterial', models.CharField(max_length=30)),
                ('glicemias', models.CharField(max_length=30)),
                ('sugerencias_cuidado', models.CharField(max_length=300)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiaClinica', to='homeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rol', models.TextField(default='enfermero', max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField()),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enfermero', to='homeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rol', models.TextField(default='paciente', max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField()),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auxiliar', to='homeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Acompañante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rol', models.TextField(default='paciente', max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('telefono', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompañante', to='homeCareApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rol', models.TextField(max_length=20, verbose_name='Rol')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=50, verbose_name='Name')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Lastname')),
                ('telefono', models.BigIntegerField(null=True, verbose_name='Phone')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
