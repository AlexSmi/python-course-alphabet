# Generated by Django 2.2.2 on 2019-07-17 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('article', '0012_auto_20190717_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='parent',
        ),
        migrations.AddField(
            model_name='comments',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]