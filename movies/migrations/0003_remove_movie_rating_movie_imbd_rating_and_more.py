# Generated by Django 4.0.2 on 2022-02-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='movie',
            name='imbd_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.FileField(blank=True, null=True, upload_to='trailers'),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
