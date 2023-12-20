# Generated by Django 4.2.6 on 2023-12-20 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='inscritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.IntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('observacion', models.TextField()),
                ('estado', models.CharField(max_length=25)),
                ('idinstitucion', models.ForeignKey(db_column='idInstitucion', on_delete=django.db.models.deletion.CASCADE, to='final_app.instituciones')),
            ],
        ),
    ]