# Generated by Django 3.0.6 on 2020-06-17 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=20, verbose_name='お名前')),
                ('age', models.SmallIntegerField(null=True, verbose_name='年齢')),
                ('species', models.CharField(blank=True, max_length=5, null=True, verbose_name='種族')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('age', models.SmallIntegerField(null=True, verbose_name='年齢')),
                ('age2', models.SmallIntegerField(null=True, verbose_name='年齢2')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('id3', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='年齢')),
                ('link_pro_names', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_test_app.Profile', verbose_name='外部キーテスト')),
            ],
        ),
    ]
