
from itertools import product
from urllib.request import Request
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateSondageForm , CommentForm ,ProductForm,CourseForm,QuestionForm
from .models import Course, Question, Result, Sondage , Comment , Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum



###############################

from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from pages import models as QMODEL


###############################


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def shop(request):
    return render(request,'pages/shop.html')


def show_comment(request):
    comment = Comment.objects.all()
    context = {
        'comment' : comment
    }

    return render(request,'pages/show_comment.html',context)


def contact(request):

	form = CommentForm()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
            
	context = {'form':form}
	return render(request, 'pages/contact.html', context)


def sondageglob(request):
    return render(request,'pages/sondageglob.html')

def home_sondage(request):
    sondage = Sondage.objects.all()
    context = {
        'sondage' : sondage
    }
    return render(request, 'pages/home_sondage.html', context)

def survey(request):
    if request.method == 'POST':
        form = CreateSondageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_sondage')
    else:
        form = CreateSondageForm()
    context = {
        'form' : form
    }
    return render(request, 'pages/survey.html', context)

def vote(request, sondage_id):
    sondage = Sondage.objects.get(pk=sondage_id)

    if request.method == 'POST':

        selected_option = request.POST['radio']
        if selected_option == 'option1':
            sondage.option_one_count += 1
        elif selected_option == 'option2':
            sondage.option_two_count += 1
        elif selected_option == 'option3':
            sondage.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        sondage.save()

        return redirect('home_sondage')
    
    context = {
        'sondage' : sondage
    }
    
    return render(request, 'pages/vote.html', context)

def result(request, sondage_id):
    sondage = Sondage.objects.get(pk=sondage_id)
    context = {
        'sondage' : sondage
    }
    return render(request, 'pages/result.html', context)




def create_result(request):
    return render(request, 'pages/create_result.html')



def productDetail(request):
    produit = Product.objects.all()
    

    context = {
        'produit': produit,
    }

    return render(request, 'pages/product.html', context)



def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addProduct')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'pages/addProduct.html', context)


    #####################################################################

def admin_add_course_view(request):
    courseForm=CourseForm()
    if request.method == 'POST':
        courseForm=CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
            return redirect('admin-add-course')
    else:
        courseForm = CourseForm()

        context = {
            'courseForm':courseForm
        }
        
    return render(request,'quiz/admin_add_course.html',context)


def admin_add_question_view(request):
    questionForm=QuestionForm()
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=models.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            questionForm=QuestionForm()
       
    return render(request,'quiz/admin_add_question.html',{'questionForm':questionForm})


def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response


def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_exam.html',{'courses':courses})



def admin_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'quiz/admin_view.html',{'courses':courses})


def delete_survey(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return redirect('admin-view')



def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'quiz/see_question.html',{'questions':questions})


def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return redirect('admin-view')

def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    if request.method=='POST':
        
        if request.COOKIES.get('course_id') is not None:
           course = request.COOKIES.get('course_id')
           course=QMODEL.Course.objects.get(id=course)
           total_marks=0
           questions=QMODEL.Question.objects.all().filter(course=course)
           for i in range(len(questions)):
            
            
                total_marks = total_marks + questions[i].marks
           student = models.Account.objects.get(username=request.user.username)
           result = QMODEL.Result()
           result.marks=total_marks
           result.exam=course
           result.student=student
           result.save()
          
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response
    


def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Account.objects.get(username=request.user.username)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'student/check_marks.html',{'results':results})


def view_result_view(request):
    results= models.Result.objects.all()
    return render(request,'student/view_result.html',{'results':results})


def test(request):
    student = models.Account.objects.get(username=request.user.username)
    data= QMODEL.Result.objects.all().filter(student=student).aggregate(thedata=Sum('marks'))
   
    return render(request,'pages/profil.html',{'data':data})


#####



# def test2(request):
#     student = models.Account.objects.get(username=request.user.username)
#     data= QMODEL.Result.objects.all().filter(student=student).aggregate(thedata=Sum('marks'))
#     product=models.Product.price
#     if request.POST.get('add'):
#         data=data-product
    

#     return render(request,'student/test2.html',{'data':data})


# def productDetail(request):
#     produit = Product.objects.all()
#     student = models.Account.objects.get(username=request.user.username)
#     data= QMODEL.Result.objects.all().filter(student=student).aggregate(thedata=Sum('marks'))
       
    
#     context = {
#         'produit': produit,
#         'data':data,
      
#     }

#     return render(request, 'pages/product.html', context)