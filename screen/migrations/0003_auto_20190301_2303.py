# Generated by Django 2.1 on 2019-03-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_movie_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='image_cluster')),
                ('image_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='movie_post',
            name='video',
            field=models.FileField(upload_to='video_cluster'),
        ),
    ]
