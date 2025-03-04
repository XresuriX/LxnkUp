# Generated by Django 5.0.12 on 2025-03-04 02:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('allow_reposts', models.BooleanField(default=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('link', models.URLField(blank=True, max_length=500)),
                ('media', models.FileField(blank=True, null=True, upload_to='post-media')),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLIC', 'Public'), ('ARCHIVED', 'Archived')], default='PUBLIC', max_length=10)),
                ('reposts_allowed', models.BooleanField(default=True)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='comments.comments')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table_comment': 'Lxnkup post model',
            },
        ),
    ]
