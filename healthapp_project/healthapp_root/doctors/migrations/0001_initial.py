# Generated by Django 2.1.7 on 2019-03-01 16:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorLogin',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_no', models.IntegerField()),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=20)),
                ('doc_logins', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctors.DoctorLogin')),
            ],
        ),
        migrations.CreateModel(
            name='LoginCredentials',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name='doctorlogin',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctors'),
        ),
    ]