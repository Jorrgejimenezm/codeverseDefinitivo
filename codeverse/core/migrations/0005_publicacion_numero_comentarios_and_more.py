# Generated by Django 5.0.6 on 2024-06-16 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_publicacion_usuario_alter_grupo_administrador_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='numero_comentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=models.TextField(max_length=250, verbose_name='Contenido'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=500)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacion')),
            ],
        ),
    ]
