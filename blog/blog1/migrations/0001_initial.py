# Generated by Django 5.0.1 on 2024-01-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Body', models.TextField()),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comm_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reg_num', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2)),
                ('phone_num', models.CharField(max_length=10, unique=True)),
                ('blog_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
