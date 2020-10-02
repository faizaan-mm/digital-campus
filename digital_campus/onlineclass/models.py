from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class Campus(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):

	user_type = models.IntegerField(blank=True, null=True)
	name = models.CharField(null=True, blank=True, max_length=50)
	campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.username


class Department(models.Model):

    name = models.CharField(max_length=50)
    hod = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name

class Section(models.Model):

	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	name = models.CharField(max_length=2)
	sem = models.IntegerField(blank=False, null=False)

	def __str__(self):
		return self.name

class Student(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	section = models.ForeignKey(Section, on_delete=models.PROTECT,)
	birth_date = models.DateField(null=False, verbose_name="Birth Date")

	def __str__(self):
		return self.user


class Faculty(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	designation = models.CharField(max_length=50)
	qualifications = models.CharField(max_length=50)
	birth_date = models.DateField(null=False, verbose_name="Birth Date")

	def __str__(self):
		return self.user


class Course(models.Model):

	dept = models.ForeignKey(Department, on_delete=models.CASCADE)
	credits = models.IntegerField(blank=False, null=False, unique=False)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.name


class Enrolled(models.Model):

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)


class Teaches(models.Model):

	instructor = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Class(models.Model):

	teacher = models.ForeignKey(Teaches, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	start_time = models.TimeField(blank=False, null=False)
	end_time = models.TimeField(blank=False, null=False)
	start_date = models.DateField(blank=False, null=False)
	end_date = models.DateField(blank=False, null=False)
	day = models.CharField(max_length=10)
	class_type = models.IntegerField(blank=False, null=False)


class Resources(models.Model):

	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	link = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


class Test(models.Model):

	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	start = models.DateTimeField(blank=False, null=False)
	end = models.DateTimeField(blank=False, null=False)
	max_marks = models.IntegerField()
	test_type = models.IntegerField(blank=False, null=False)
	link = models.CharField(max_length=255)


class Submission(models.Model):

	test = models.ForeignKey(Test, on_delete=models.PROTECT)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	marks = models.IntegerField()
	remarks = models.CharField(max_length=255)


class Performance(models.Model):

	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	enrolled = models.ForeignKey(Enrolled, on_delete=models.CASCADE)
	internals = models.IntegerField()
	endsems = models.IntegerField()
	grade = models.CharField(max_length=2)
	attendance = models.DecimalField(max_digits=2,decimal_places=2)


class Attendance(models.Model):

	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	enrolled = models.ForeignKey(Enrolled, on_delete=models.CASCADE)
	counter = models.IntegerField()

