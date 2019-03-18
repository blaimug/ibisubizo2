# Generated by Django 2.1.3 on 2019-02-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attachements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.FilePathField()),
                ('attachementDate', models.DateTimeField(auto_now_add=True)),
                ('attachementType', models.CharField(max_length=50)),
                ('attachementSize', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersArray', models.CharField(max_length=200)),
                ('problemId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificationType', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField()),
                ('recipient', models.CharField(max_length=200)),
                ('recipientName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='problemReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('reactionType', models.CharField(max_length=50)),
                ('reactionReason', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('attachementsArray', models.CharField(max_length=200)),
                ('public', models.BooleanField()),
                ('userId', models.IntegerField()),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
                ('canBeJoined', models.BooleanField()),
                ('groupId', models.IntegerField()),
                ('views', models.IntegerField()),
                ('resolved', models.BooleanField()),
                ('resolvedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('attachementsArray', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='replyReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('reactionType', models.CharField(max_length=50)),
                ('reactionReason', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('dataFrom', models.CharField(max_length=50)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('reason', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('initiated', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.DateTimeField()),
            ],
        ),
    ]