from configparser import MAX_INTERPOLATION_DEPTH
from datetime import datetime
from pydoc import describe
from pyexpat import model
from turtle import update
from unicodedata import category
from django.db import models
from account.models import Account

import uuid


class Sondage(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count


class Sondageglob(models.Model):
    name = models.CharField(max_length=50)
    mark = models.IntegerField(default=0)
    sondage = models.ForeignKey(Sondage,related_name='sondage',on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Comment(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.name


class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

#####################################################################################################################

class Course(models.Model):
   course_name = models.CharField(max_length=50)
 
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField(null=True)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    

class Result(models.Model):
    student = models.ForeignKey(Account,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.marks