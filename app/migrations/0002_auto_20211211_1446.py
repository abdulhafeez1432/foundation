# Generated by Django 3.2.9 on 2021-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetails',
            name='name',
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='passport',
            field=models.ImageField(null=True, upload_to='applicant', verbose_name='Passport Photography'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='place_of_birth',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
