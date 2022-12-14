# Generated by Django 4.1.3 on 2022-11-01 23:35

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_video_text_image_file_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='modul',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modul',
            name='order',
            field=courses.fields.OrderField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
