# Generated by Django 4.0.3 on 2022-08-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=50)),
                ('stuemail', models.EmailField(max_length=50)),
                ('stupass', models.CharField(max_length=50)),
            ],
        ),
    ]
