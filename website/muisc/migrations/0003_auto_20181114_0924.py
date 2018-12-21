# Generated by Django 2.1.1 on 2018-11-14 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muisc', '0002_auto_20181110_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=240)),
                ('password', models.CharField(max_length=50)),
                ('confirm_Password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muisc.signUp'),
        ),
    ]