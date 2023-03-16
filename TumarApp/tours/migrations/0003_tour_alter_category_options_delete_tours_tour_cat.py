# Generated by Django 4.1.5 on 2023-03-09 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_category_alter_tour_options_tour_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('date', models.TimeField(max_length=250, verbose_name='Date')),
                ('equipment', models.TextField(verbose_name='Equipment')),
                ('country', models.TextField(verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.DeleteModel(
            name='Tours',
        ),
        migrations.AddField(
            model_name='tour',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tours.category'),
        ),
    ]
