# Generated by Django 4.0.1 on 2022-01-09 01:35
'''django just created this whole document for us(after using makemigrations command), 
so we don't need to manually execute all these commands. Note that we also need to go
ahead and execute this migration. So anytime we add or modify a model field we run makemigrations and
finally `python manage.py migrate`, so now the table is officially there. But we also need to do
an extra thing. When you check your admin panel, you get surprised that the table is not there yet.
Do you know what that is? check out <app>/admin.py, remember that we said admin panel is a totally
different thing from the database itself?'''
from django.db import migrations, models
import uuid



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
