# Generated by Django 3.2.9 on 2021-11-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('L', '일상'), ('Y', '맛집탐방'), ('E', '기타')], default='L', max_length=100)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]