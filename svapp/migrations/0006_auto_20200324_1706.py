# Generated by Django 2.2.10 on 2020-03-24 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('svapp', '0005_auto_20200318_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=10)),
                ('text', models.CharField(max_length=255, verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='svapp.Answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_answers', to='svapp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(choices=[('#007bff', '#007bff'), ('#EC407A', '#EC407A'), ('#FF5733', '#FF5733'), ('#2ECC71', '#2ECC71'), ('#7D3C98', '#7D3C98'), ('#1B4F72', '#1B4F72'), ('#F7DC6', '#F7DC6')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='TakenQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='svapp.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='svapp.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='add',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(related_name='interested_students', to='svapp.Subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='quizzes',
            field=models.ManyToManyField(through='svapp.TakenQuiz', to='svapp.Quiz'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quiz',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='svapp.Subject'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='svapp.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='svapp.Question'),
        ),
    ]