# Generated by Django 3.2.4 on 2023-10-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rp1_rp10_rp11_rp12_rp2_rp3_rp4_rp5_rp6_rp7_rp8_rp9'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='RP1',
        ),
        migrations.DeleteModel(
            name='RP10',
        ),
        migrations.DeleteModel(
            name='RP11',
        ),
        migrations.DeleteModel(
            name='RP12',
        ),
        migrations.DeleteModel(
            name='RP2',
        ),
        migrations.DeleteModel(
            name='RP3',
        ),
        migrations.DeleteModel(
            name='RP4',
        ),
        migrations.DeleteModel(
            name='RP5',
        ),
        migrations.DeleteModel(
            name='RP6',
        ),
        migrations.DeleteModel(
            name='RP7',
        ),
        migrations.DeleteModel(
            name='RP8',
        ),
        migrations.DeleteModel(
            name='RP9',
        ),
    ]