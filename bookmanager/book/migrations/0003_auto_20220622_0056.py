# Generated by Django 2.2.5 on 2022-06-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220622_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peopleinfo',
            options={'verbose_name': '人物信息'},
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]
