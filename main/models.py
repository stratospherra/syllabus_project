from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS_CHOICES = (
    ("Ru", "Ru"),
    ("En", "En"),
    ("Kz", "Kz"),
)

# Create your models here.

class Language(models.Model):
    status_choices = models.CharField(max_length=50, verbose_name="Выбор языка",
        choices=STATUS_CHOICES, default="Ru")

    def __str__(self):
        return f"{self.status_choices}"
    
class School(models.Model):
    title = models.CharField(verbose_name='Название школы', max_length=255)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Название школы"
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CustomUser(AbstractUser):
    email = models.EmailField('Эл. Почта', max_length=255)
    prof = models.CharField('Должность', max_length=255)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}."

    def __str__(self):
        return self.get_full_name()

    def get_created_syllabuses(self):
        return Instructor.objects.filter(instructor=self)

    class Meta:
        verbose_name = 'Преподаватель'

class Director(models.Model):
    full_name = models.CharField('ФИ', max_length=255)
    prof = models.CharField('Должность', max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name


class Code_and_Name_discipline(models.Model):
    name = models.CharField(verbose_name="Название дисциплины", max_length=255)
    code = models.CharField(verbose_name="Код", max_length=255)

    def __str__(self):
        return f"{self.code} {self.name}"
    class Meta:
        verbose_name = "Название дисциплины"
        verbose_name_plural = "Название дисциплины"
    
class ECTS_and_hours(models.Model):
    ects = models.PositiveIntegerField(verbose_name="Кредиты")
    allhours = models.PositiveIntegerField(verbose_name="Всего часов")
    auditorhours = models.PositiveIntegerField(verbose_name="Аудиторные часы")
    Independent_work = models.PositiveIntegerField(verbose_name="Самостоятельная работа(СРОП, СРО)")

    def __str__(self):
        return f"{self.ects} | {self.allhours} | {self.auditorhours} | {self.Independent_work}"
    
    class Meta:
        verbose_name = "ECTS"
        
    
class Prerequisites(models.Model):
    prerequisites = models.TextField(verbose_name='Пререквизиты', blank=False)
    
    def __str__(self):
        return f"{self.prerequisites}"
    
    class Meta:
        verbose_name = "Пререквизиты"
    
class TrainingLevel(models.Model):
    training_level = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Уровень обучения')

    def __str__(self):
        return f"{self.training_level}"
    
    class Meta:
        verbose_name = "Уровень обучения"
        verbose_name_plural = "Уровень обучении"

class Semester(models.Model):
    semester = models.PositiveIntegerField(verbose_name="Cеместр", null=True, blank=True)

    def __str__(self):
        return f"{self.semester}"
    
    class Meta:
        verbose_name = "Cеместр"
        verbose_name_plural = "Cеместры"

    
class EduPrograms(models.Model):
    edu_programms = models.TextField(verbose_name='Образовательная программа', blank=False)

    def __str__(self):
        return f"{self.edu_programms}"
    
    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"

class Language_of_education(models.Model):
    language_of_education = models.CharField(max_length=120, null=True, blank=True, verbose_name="Язык обучения")

    def __str__(self):
        return f"{self.language_of_education}"
    
    class Meta:
        verbose_name = "Язык обучения"
        verbose_name_plural = "Язык обучение"


class Proficiency_level(models.Model):
    proficiency_level = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Уровень владения языком')

    def __str__(self):
        return f"{self.proficiency_level}"
    
    class Meta:
        verbose_name = "Уровень владения языком"

class Format_of_training(models.Model):
    format_of_training = models.CharField(max_length=255, null=True, blank=True, verbose_name="Формат обучения")

    def __str__(self):
        return f"{self.format_of_training}"
    
    class Meta:
        verbose_name = "Формат обучения"

class Instructor(models.Model):
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, verbose_name='Инструктор/Преподаватель')

    def __str__(self):
        return f"{self.instructor}"
    
    class Meta:
        verbose_name = "Инструктор/Преподаватель"

class Contact(models.Model):
    email = models.CharField(verbose_name="Email", max_length=120)
    phone = models.CharField(verbose_name="телефон", max_length=12)

    def __str__(self):
        return f"{self.email} | {self.phone} "
    
    class Meta:
        verbose_name = "Контакты"

class Time_Place(models.Model):
    time_place = models.TextField(verbose_name='Время и место проведения',blank=False)

    def __str__(self):
        return f"{self.time_place}"
    
    class Meta:
        verbose_name = "Время и место проведения"


class Course_Objective(models.Model):
    course_objective = models.TextField(verbose_name="Цель курса")

    def __str__(self):
        return f"{self.course_objective}"
    
    class Meta:
        verbose_name = "Цель курса"



