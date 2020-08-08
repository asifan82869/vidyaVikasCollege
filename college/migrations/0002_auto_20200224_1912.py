# Generated by Django 3.0.1 on 2020-02-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='college/form_image')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mother_frist_name', models.CharField(max_length=50)),
                ('mother_middle_name', models.CharField(max_length=50)),
                ('mother_last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('date_of_brith', models.DateField()),
                ('current_address', models.CharField(max_length=50)),
                ('current_city', models.CharField(max_length=50)),
                ('current_state', models.CharField(max_length=50)),
                ('current_zip', models.CharField(max_length=20)),
                ('permanent_address', models.CharField(max_length=50)),
                ('permanent_city', models.CharField(max_length=50)),
                ('permanent_state', models.CharField(max_length=50)),
                ('permanent_zip', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('stream', models.CharField(max_length=20)),
                ('ssc_school_name', models.CharField(max_length=50)),
                ('ssc_borad_state', models.CharField(max_length=50)),
                ('ssc_parcentage', models.CharField(max_length=50)),
                ('hsc_school_name', models.CharField(max_length=50)),
                ('hsc_borad_state', models.CharField(max_length=50)),
                ('hsc_parcentage', models.CharField(max_length=50)),
                ('sem1_college_name', models.CharField(max_length=50)),
                ('sem1_university_name', models.CharField(max_length=50)),
                ('sem1_pointer', models.CharField(max_length=50)),
                ('sem2_college_name', models.CharField(max_length=50)),
                ('sem2_university_name', models.CharField(max_length=50)),
                ('sem2_pointer', models.CharField(max_length=50)),
                ('sem3_college_name', models.CharField(max_length=50)),
                ('sem3_university_name', models.CharField(max_length=50)),
                ('sem3_pointer', models.CharField(max_length=50)),
                ('sem4_college_name', models.CharField(max_length=50)),
                ('sem4_university_name', models.CharField(max_length=50)),
                ('sem4_pointer', models.CharField(max_length=50)),
                ('phone1', models.IntegerField(max_length=10)),
                ('phone2', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]