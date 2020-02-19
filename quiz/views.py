from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from .forms import SignUpForm
from .models import Quiz,UserProfile,QuizId
from django.contrib.auth.models import User
# from django.contrib.sessions.models import Session
from django.contrib.auth.signals import user_logged_in
# import scipy
# from scipy import stats
# import numpy as np
from .utils import render_to_pdf
import datetime
from django.http import HttpResponse
import pandas as pd
import random
totalQuestions=[]



# print(totalQuestions.id)
print('totalquestions')
def index(request):
    totalQuestions = []
    print('1',request.session)
    request.session['key']='value'
    print(request.user)
    # global totalQuestions
    # totalQuestions = random.sample(list(Quiz.objects.all()), 60)

    return render(request,'quiz/home.html',{'myurl':'http://www.tvashtaa.com'})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            userid = form.cleaned_data.get('tvashId')
            uname=form.cleaned_data.get('username')
            print('uname',uname)
            lis1=QuizId.objects.all()
            u=User.objects.all()
            uprofile = UserProfile.objects.all()
            uprofileid=[]
            tid=[]
            for i in uprofile:
                uprofileid.append(i.TvashId)
            for i in lis1:
                tid.append(i.quizid)
            print('uid',uprofileid)
            if userid in tid:
                if userid in uprofileid:
                    return render(request, 'quiz/login.html',
                                  {'message': "You can not sign up with different name with same ID"})
                else:
                    print("came")
                    user = form.save()
                    user.refresh_from_db()
                    # username=form.cleaned_data.get('username')
                    # password = form.cleaned_data.get('password')
                    user.userprofile.mobileNumber = form.cleaned_data.get('mobileNumber')
                    user.userprofile.TvashId = form.cleaned_data.get('tvashId')

                    user.userprofile.save()
                    print(user.userprofile.mobileNumber)
                    print(user.userprofile.TvashId)
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=user.username, password=raw_password)
                    print('user', user)
                    login(request, user)
                    return redirect('index')


            else:
                return render(request, 'quiz/login.html', {'message': "You are not allowed to take exam"})
    else:
        form = SignUpForm()
    return render(request, 'quiz/signup.html', {'form': form,'myurl':'http://www.tvashtaa.com'})


def loginview(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            request.session['username'] = user.username
            request.session['password']=user.password
            # session = Session.objects.get(session_key=request.session.session_key)
            # print(session)
            print('n',request.session['username'])
            print('p',request.session['password'])
            user.userprofile.name=user.username
            user.userprofile.save()
            user.userprofile.login_count = user.userprofile.login_count + 1
            user.userprofile.save()

            print(user.userprofile.login_count)
            if user.userprofile.login_count > 2:
                return render(request,'quiz/login.html',{'message':"You are not allowed to take exam"})
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form,'myurl':'http://www.tvashtaa.com'})

def logoutview(request):
    print(request.user.is_authenticated)
    try:
        del request.session['username']
    except:
        pass
    logout(request)
    return redirect('index')

def quizpage1(request,value):
    min = 60
    sec = 0
    global totalQuestions

    request.session['min']=min
    request.session['sec']=sec
    # before going to take test we should make all choices must be zero
    # for x in range(10):
    #     request.user.userprofile.ch1 = 0
    #     request.user.userprofile.save()
    request.user.userprofile.ch1 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch2 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch3 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch4 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch5 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch6 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch7 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch8 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch9 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch10 = 0
    request.user.userprofile.save()
    request.user.userprofile.score = 0
    request.user.userprofile.save()

    request.user.userprofile.ch11 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch12 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch13 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch14 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch15 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch16 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch17 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch18 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch19 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch20 = 0
    request.user.userprofile.save()

    request.user.userprofile.ch21 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch22 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch23 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch24 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch25 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch26 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch27 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch28 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch29 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch30 = 0
    request.user.userprofile.save()

    request.user.userprofile.ch31 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch32 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch33 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch34 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch35 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch36 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch37 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch38 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch39 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch40 = 0
    request.user.userprofile.save()

    request.user.userprofile.ch41 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch42 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch43 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch44 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch45 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch46 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch47 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch48 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch49 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch50 = 0
    request.user.userprofile.save()

    request.user.userprofile.ch51 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch52 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch53 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch54 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch55 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch56 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch57 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch58 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch59 = 0
    request.user.userprofile.save()
    request.user.userprofile.ch60 = 0
    request.user.userprofile.save()
    request.user.userprofile.score = 0
    request.user.userprofile.save()
    print('len',len(totalQuestions))

    try:
        if value == '0':
            totalQuestions = random.sample(list(Quiz.objects.all()), 60)
            queids = []
            for i in range(len(totalQuestions)):
                queids.append(totalQuestions[i].id)
            print('length', len(queids))
            print(queids)
            request.session['queids'] = queids
            page1id = request.session['queids'][0]
            question1 = get_object_or_404(Quiz, id=page1id)
            print('id', page1id)
            qus = len(totalQuestions) - 1
            context = {'questions': question1,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 1,
                       'myurl': 'http://www.tvashtaa.com'
                       }

            return render(request, 'quiz/page1.html', context)
    except(KeyError):
       pass

    try:
        if request.POST.get("minute") != None:
            min = request.POST.get("minute")
            sec = request.POST.get("second")
            request.session['min'] = min
            request.session['sec'] = sec
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    print("came1")
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print(score)
                    return render(request, "quiz/result.html",{'attemted': 1, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que1=get_object_or_404(Quiz, id=request.session['queids'][0])
                    choice1 = request.POST.get(str(que1.id))
                    print('choice1',choice1)
                    request.session['choice1'] = choice1
                    print('ch1', request.session['choice1'])

                    if (request.session['choice1'] == que1.answer):
                        request.user.userprofile.ch1 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)

                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que1,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               'totalqus': len(totalQuestions),
                               'counter': 1,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que1.answer,
                               'userans': request.session['choice1'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }
                    print("userans",request.session['choice1'])
                    return render(request, 'quiz/page1.html', context)

    except(KeyError):
       pass

def quizpage2(request, value):


    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page2id = request.session['queids'][1]
            question2 = get_object_or_404(Quiz, id=page2id)
            qus = len(totalQuestions) - 1
            context = {'questions': question2,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 2,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page2.html', context)
    except(KeyError):
      pass

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",{'attemted': 2, 'score': score, 'total': 60,'myurl': 'http://www.tvashtaa.com'})
                else:
                    que2 = get_object_or_404(Quiz, id=request.session['queids'][1])
                    choice2 = request.POST.get(str(que2.id))
                    request.session['choice2'] = choice2
                    if (choice2 == que2.answer):
                        request.user.userprofile.ch2 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que2,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 2,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que2.answer,
                               'userans': request.session['choice2'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }
                    return render(request, 'quiz/page2.html', context)
    except(KeyError):
        pass
def quizpage3(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page3id = request.session['queids'][2]
            question3 = get_object_or_404(Quiz, id=page3id)
            qus = len(totalQuestions) - 1
            context = {'questions': question3,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 3,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page3.html', context)
    except(KeyError):
        pass

    try:
        if value == '1':

            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",{'attemted': 3, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que3 = get_object_or_404(Quiz, id=request.session['queids'][2])
                    choice3 = request.POST.get(str(que3.id))
                    request.session['choice3'] = choice3
                    if (choice3 == que3.answer):
                        request.user.userprofile.ch3 = 1
                        request.user.userprofile.save()
                        print('cho')
                    # else:
                    #     request.user.userprofile.ch3 = 0
                    #     request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que3,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 3,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que3.answer,
                               'userans': request.session['choice3'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page3.html', context)
    except(KeyError):
        pass
def quizpage4(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page4id = request.session['queids'][3]
            question4 = get_object_or_404(Quiz, id=page4id)
            qus = len(totalQuestions) - 1
            context = {'questions': question4,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 4,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page4.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 4, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que4 = get_object_or_404(Quiz, id=request.session['queids'][3])
                    choice4 = request.POST.get(str(que4.id))
                    request.session['choice4'] = choice4
                    print('ans', que4.answer)
                    print('ch1', request.session['choice4'])
                    if (choice4 == que4.answer):
                        request.user.userprofile.ch4 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que4,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 4,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que4.answer,
                               'userans': request.session['choice4'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page4.html', context)
    except(KeyError):
        pass

def quizpage5(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page5id = request.session['queids'][4]
            question5 = get_object_or_404(Quiz, id=page5id)
            qus = len(totalQuestions) - 1
            context = {'questions': question5,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 5,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page5.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 5, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que5 = get_object_or_404(Quiz, id=request.session['queids'][4])
                    choice5 = request.POST.get(str(que5.id))
                    request.session['choice5'] = choice5
                    if (choice5 == que5.answer):
                        request.user.userprofile.ch5 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que5,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 5,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que5.answer,
                               'userans': request.session['choice5'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page5.html', context)
    except(KeyError):
        pass

def quizpage6(request, value):


    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page6id = request.session['queids'][5]
            question6 = get_object_or_404(Quiz, id=page6id)
            qus = len(totalQuestions) - 1
            context = {'questions': question6,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 6,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page6.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 6, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que6 = get_object_or_404(Quiz, id=request.session['queids'][5])
                    choice6 = request.POST.get(str(que6.id))
                    request.session['choice6'] = choice6
                    if (choice6 == que6.answer):
                        request.user.userprofile.ch6 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que6,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 5,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que6.answer,
                               'userans': request.session['choice6'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page6.html', context)
    except(KeyError):
        pass

def quizpage7(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page7id = request.session['queids'][6]
            question7 = get_object_or_404(Quiz, id=page7id)
            qus = len(totalQuestions) - 1
            context = {'questions': question7,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 7,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page7.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 7, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que7 = get_object_or_404(Quiz, id=request.session['queids'][6])
                    choice7 = request.POST.get(str(que7.id))
                    request.session['choice7'] = choice7
                    if (choice7 == que7.answer):
                        request.user.userprofile.ch7 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que7,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 7,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que7.answer,
                               'userans': request.session['choice7'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page7.html', context)
    except(KeyError):
        pass

def quizpage8(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page8id = request.session['queids'][7]
            question8 = get_object_or_404(Quiz, id=page8id)
            qus = len(totalQuestions) - 1
            context = {'questions': question8,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 8,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page8.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 8, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que8 = get_object_or_404(Quiz, id=request.session['queids'][7])
                    choice8 = request.POST.get(str(que8.id))
                    request.session['choice8'] = choice8
                    if (choice8 == que8.answer):
                        request.user.userprofile.ch8 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que8,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 8,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que8.answer,
                               'userans': request.session['choice8'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page8.html', context)
    except(KeyError):
        pass

def quizpage9(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page9id = request.session['queids'][8]
            question9 = get_object_or_404(Quiz, id=page9id)
            qus = len(totalQuestions) - 1
            context = {'questions': question9,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 9,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page9.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 9, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que9 = get_object_or_404(Quiz, id=request.session['queids'][8])
                    choice9 = request.POST.get(str(que9.id))
                    request.session['choice9'] = choice9
                    if (choice9 == que9.answer):
                        request.user.userprofile.ch9 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que9,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 9,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que9.answer,
                               'userans': request.session['choice9'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page9.html', context)
    except(KeyError):
        pass

def quizpage10(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page10id = request.session['queids'][9]
            question10 = get_object_or_404(Quiz, id=page10id)
            qus = len(totalQuestions) - 1
            context = {'questions': question10,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 10,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page10.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 10, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que10 = get_object_or_404(Quiz, id=request.session['queids'][9])
                    choice10 = request.POST.get(str(que10.id))
                    request.session['choice10'] = choice10
                    if (choice10 == que10.answer):
                        request.user.userprofile.ch10 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que10,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 10,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que10.answer,
                               'userans': request.session['choice10'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page10.html', context)
    except(KeyError):
        pass
def quizpage11(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page11id = request.session['queids'][10]
            question11 = get_object_or_404(Quiz, id=page11id)
            qus = len(totalQuestions) - 1
            context = {'questions': question11,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 11,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page11.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 11, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que11 = get_object_or_404(Quiz, id=request.session['queids'][10])
                    choice11 = request.POST.get(str(que11.id))
                    request.session['choice11'] = choice11
                    if (choice11 == que11.answer):
                        request.user.userprofile.ch11 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que11,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 11,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que11.answer,
                               'userans': request.session['choice11'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page11.html', context)
    except(KeyError):
        pass
def quizpage12(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page12id = request.session['queids'][11]
            question12 = get_object_or_404(Quiz, id=page12id)
            qus = len(totalQuestions) - 1
            context = {'questions': question12,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 12,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page12.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 12, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que12 = get_object_or_404(Quiz, id=request.session['queids'][11])
                    choice12 = request.POST.get(str(que12.id))
                    request.session['choice12'] = choice12
                    if (choice12 == que12.answer):
                        request.user.userprofile.ch12 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que12,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 12,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que12.answer,
                               'userans': request.session['choice12'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page12.html', context)
    except(KeyError):
        pass
def quizpage13(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page13id = request.session['queids'][12]
            question13 = get_object_or_404(Quiz, id=page13id)
            qus = len(totalQuestions) - 1
            context = {'questions': question13,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 13,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page13.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 13, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que13 = get_object_or_404(Quiz, id=request.session['queids'][12])
                    choice13 = request.POST.get(str(que13.id))
                    request.session['choice13'] = choice13
                    if (choice13 == que13.answer):
                        request.user.userprofile.ch13 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que13,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 13,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que13.answer,
                               'userans': request.session['choice13'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page13.html', context)
    except(KeyError):
        pass
def quizpage14(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page14id = request.session['queids'][13]
            question14 = get_object_or_404(Quiz, id=page14id)
            qus = len(totalQuestions) - 1
            context = {'questions': question14,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 14,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page14.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 14, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que14 = get_object_or_404(Quiz, id=request.session['queids'][13])
                    choice14 = request.POST.get(str(que14.id))
                    request.session['choice14'] = choice14
                    if (choice14 == que14.answer):
                        request.user.userprofile.ch14 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que14,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 14,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que14.answer,
                               'userans': request.session['choice14'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page14.html', context)
    except(KeyError):
        pass
def quizpage15(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page15id = request.session['queids'][14]
            question15 = get_object_or_404(Quiz, id=page15id)
            qus = len(totalQuestions) - 1
            context = {'questions': question15,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 15,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page15.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 15, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que15 = get_object_or_404(Quiz, id=request.session['queids'][14])
                    choice15 = request.POST.get(str(que15.id))
                    request.session['choice15'] = choice15
                    if (choice15 == que15.answer):
                        request.user.userprofile.ch15 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que15,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 15,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que15.answer,
                               'userans': request.session['choice15'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page15.html', context)
    except(KeyError):
        pass
def quizpage16(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page16id = request.session['queids'][15]
            question16 = get_object_or_404(Quiz, id=page16id)
            qus = len(totalQuestions) - 1
            context = {'questions': question16,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 16,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page16.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 16, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que16 = get_object_or_404(Quiz, id=request.session['queids'][15])
                    choice16 = request.POST.get(str(que16.id))
                    request.session['choice16'] = choice16
                    if (choice16 == que16.answer):
                        request.user.userprofile.ch16 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que16,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 16,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que16.answer,
                               'userans': request.session['choice16'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page16.html', context)
    except(KeyError):
        pass
def quizpage17(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page17id = request.session['queids'][16]
            question17 = get_object_or_404(Quiz, id=page17id)
            qus = len(totalQuestions) - 1
            context = {'questions': question17,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 17,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page17.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 17, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que17 = get_object_or_404(Quiz, id=request.session['queids'][16])
                    choice17 = request.POST.get(str(que17.id))
                    request.session['choice17'] = choice17
                    if (choice17 == que17.answer):
                        request.user.userprofile.ch17 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que17,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 17,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que17.answer,
                               'userans': request.session['choice17'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page17.html', context)
    except(KeyError):
        pass
def quizpage18(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page18id = request.session['queids'][17]
            question18 = get_object_or_404(Quiz, id=page18id)
            qus = len(totalQuestions) - 1
            context = {'questions': question18,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 18,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page18.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 18, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que18 = get_object_or_404(Quiz, id=request.session['queids'][17])
                    choice18 = request.POST.get(str(que18.id))
                    request.session['choice18'] = choice18
                    if (choice18 == que18.answer):
                        request.user.userprofile.ch18 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que18,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 18,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que18.answer,
                               'userans': request.session['choice18'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page18.html', context)
    except(KeyError):
        pass
def quizpage19(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page19id = request.session['queids'][18]
            question19 = get_object_or_404(Quiz, id=page19id)
            qus = len(totalQuestions) - 1
            context = {'questions': question19,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 19,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page19.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 19, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que19 = get_object_or_404(Quiz, id=request.session['queids'][18])
                    choice19 = request.POST.get(str(que19.id))
                    request.session['choice19'] = choice19
                    if (choice19 == que19.answer):
                        request.user.userprofile.ch19 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que19,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 19,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que19.answer,
                               'userans': request.session['choice19'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page19.html', context)
    except(KeyError):
        pass

def quizpage20(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page20id = request.session['queids'][19]
            question20 = get_object_or_404(Quiz, id=page20id)
            qus = len(totalQuestions) - 1
            context = {'questions': question20,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 20,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page20.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 20, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que20 = get_object_or_404(Quiz, id=request.session['queids'][19])
                    choice20 = request.POST.get(str(que20.id))
                    request.session['choice20'] = choice20
                    if (choice20 == que20.answer):
                        request.user.userprofile.ch20 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que20,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 20,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que20.answer,
                               'userans': request.session['choice20'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page20.html', context)
    except(KeyError):
        pass

def quizpage21(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page21id = request.session['queids'][20]
            question21 = get_object_or_404(Quiz, id=page21id)
            qus = len(totalQuestions) - 1
            context = {'questions': question21,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 21,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page21.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 21, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que21 = get_object_or_404(Quiz, id=request.session['queids'][20])
                    choice21 = request.POST.get(str(que21.id))
                    request.session['choice21'] = choice21
                    if (choice21 == que21.answer):
                        request.user.userprofile.ch21 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que21,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 21,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que21.answer,
                               'userans': request.session['choice21'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page21.html', context)
    except(KeyError):
        pass

def quizpage22(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page22id = request.session['queids'][21]
            question22 = get_object_or_404(Quiz, id=page22id)
            qus = len(totalQuestions) - 1
            context = {'questions': question22,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 22,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page22.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 22, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que22 = get_object_or_404(Quiz, id=request.session['queids'][21])
                    choice22 = request.POST.get(str(que22.id))
                    request.session['choice22'] = choice22
                    if (choice22 == que22.answer):
                        request.user.userprofile.ch22 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que22,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 22,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que22.answer,
                               'userans': request.session['choice22'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page22.html', context)
    except(KeyError):
        pass

def quizpage23(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page23id = request.session['queids'][22]
            question23 = get_object_or_404(Quiz, id=page23id)
            qus = len(totalQuestions) - 1
            context = {'questions': question23,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 23,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page23.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 23, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que23 = get_object_or_404(Quiz, id=request.session['queids'][22])
                    choice23 = request.POST.get(str(que23.id))
                    request.session['choice23'] = choice23
                    if (choice23 == que23.answer):
                        request.user.userprofile.ch23 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que23,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 23,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que23.answer,
                               'userans': request.session['choice23'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page23.html', context)
    except(KeyError):
        pass

def quizpage24(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page24id = request.session['queids'][23]
            question24 = get_object_or_404(Quiz, id=page24id)
            qus = len(totalQuestions) - 1
            context = {'questions': question24,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 24,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page24.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 24, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que24 = get_object_or_404(Quiz, id=request.session['queids'][23])
                    choice24 = request.POST.get(str(que24.id))
                    request.session['choice24'] = choice24
                    if (choice24 == que24.answer):
                        request.user.userprofile.ch24 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que24,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 24,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que24.answer,
                               'userans': request.session['choice24'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page24.html', context)
    except(KeyError):
        pass

def quizpage25(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page25id = request.session['queids'][24]
            question25 = get_object_or_404(Quiz, id=page25id)
            qus = len(totalQuestions) - 1
            context = {'questions': question25,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 25,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page25.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 25, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que25 = get_object_or_404(Quiz, id=request.session['queids'][24])
                    choice25 = request.POST.get(str(que25.id))
                    request.session['choice25'] = choice25
                    if (choice25 == que25.answer):
                        request.user.userprofile.ch25 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que25,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 25,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que25.answer,
                               'userans': request.session['choice25'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page25.html', context)
    except(KeyError):
        pass

def quizpage26(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page26id = request.session['queids'][25]
            question26 = get_object_or_404(Quiz, id=page26id)
            qus = len(totalQuestions) - 1
            context = {'questions': question26,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 26,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page26.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 26, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que26 = get_object_or_404(Quiz, id=request.session['queids'][25])
                    choice26 = request.POST.get(str(que26.id))
                    request.session['choice26'] = choice26
                    if (choice26 == que26.answer):
                        request.user.userprofile.ch26 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que26,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 26,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que26.answer,
                               'userans': request.session['choice26'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page26.html', context)
    except(KeyError):
        pass

def quizpage27(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page27id = request.session['queids'][26]
            question27 = get_object_or_404(Quiz, id=page27id)
            qus = len(totalQuestions) - 1
            context = {'questions': question27,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 27,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page27.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 27, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que27 = get_object_or_404(Quiz, id=request.session['queids'][26])
                    choice27 = request.POST.get(str(que27.id))
                    request.session['choice27'] = choice27
                    if (choice27 == que27.answer):
                        request.user.userprofile.ch27 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que27,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 27,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que27.answer,
                               'userans': request.session['choice27'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page27.html', context)
    except(KeyError):
        pass

def quizpage28(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page28id = request.session['queids'][27]
            question28 = get_object_or_404(Quiz, id=page28id)
            qus = len(totalQuestions) - 1
            context = {'questions': question28,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 28,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page28.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 28, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que28 = get_object_or_404(Quiz, id=request.session['queids'][27])
                    choice28 = request.POST.get(str(que28.id))
                    request.session['choice28'] = choice28
                    if (choice28 == que28.answer):
                        request.user.userprofile.ch28 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que28,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 28,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que28.answer,
                               'userans': request.session['choice28'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page28.html', context)
    except(KeyError):
        pass

def quizpage29(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page29id = request.session['queids'][28]
            question29 = get_object_or_404(Quiz, id=page29id)
            qus = len(totalQuestions) - 1
            context = {'questions': question29,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 29,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page29.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 29, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que29 = get_object_or_404(Quiz, id=request.session['queids'][28])
                    choice29 = request.POST.get(str(que29.id))
                    request.session['choice29'] = choice29
                    if (choice29 == que29.answer):
                        request.user.userprofile.ch29 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que29,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 29,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que29.answer,
                               'userans': request.session['choice29'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page29.html', context)
    except(KeyError):
        pass

def quizpage30(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page30id = request.session['queids'][29]
            question30 = get_object_or_404(Quiz, id=page30id)
            qus = len(totalQuestions) - 1
            context = {'questions': question30,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 30,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page30.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 30, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que30 = get_object_or_404(Quiz, id=request.session['queids'][29])
                    choice30 = request.POST.get(str(que30.id))
                    request.session['choice30'] = choice30
                    if (choice30 == que30.answer):
                        request.user.userprofile.ch30 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que30,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 30,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que30.answer,
                               'userans': request.session['choice30'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page30.html', context)
    except(KeyError):
        pass

def quizpage31(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page31id = request.session['queids'][30]
            question31 = get_object_or_404(Quiz, id=page31id)
            qus = len(totalQuestions) - 1
            context = {'questions': question31,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 31,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page31.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 31, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que31 = get_object_or_404(Quiz, id=request.session['queids'][30])
                    choice31 = request.POST.get(str(que31.id))
                    request.session['choice31'] = choice31
                    if (choice31 == que31.answer):
                        request.user.userprofile.ch31 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que31,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 31,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que31.answer,
                               'userans': request.session['choice31'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page31.html', context)
    except(KeyError):
        pass

def quizpage32(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page32id = request.session['queids'][31]
            question32 = get_object_or_404(Quiz, id=page32id)
            qus = len(totalQuestions) - 1
            context = {'questions': question32,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 32,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page32.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 32, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que32 = get_object_or_404(Quiz, id=request.session['queids'][31])
                    choice32 = request.POST.get(str(que32.id))
                    request.session['choice32'] = choice32
                    if (choice32 == que32.answer):
                        request.user.userprofile.ch32 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que32,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 32,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que32.answer,
                               'userans': request.session['choice32'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page32.html', context)
    except(KeyError):
        pass

def quizpage33(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page33id = request.session['queids'][32]
            question33 = get_object_or_404(Quiz, id=page33id)
            qus = len(totalQuestions) - 1
            context = {'questions': question33,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 33,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page33.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 33, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que33 = get_object_or_404(Quiz, id=request.session['queids'][32])
                    choice33 = request.POST.get(str(que33.id))
                    request.session['choice33'] = choice33
                    if (choice33 == que33.answer):
                        request.user.userprofile.ch33 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que33,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 33,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que33.answer,
                               'userans': request.session['choice33'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page33.html', context)
    except(KeyError):
        pass

def quizpage34(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page34id = request.session['queids'][33]
            question34 = get_object_or_404(Quiz, id=page34id)
            qus = len(totalQuestions) - 1
            context = {'questions': question34,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 34,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page34.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 34, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que34 = get_object_or_404(Quiz, id=request.session['queids'][33])
                    choice34 = request.POST.get(str(que34.id))
                    request.session['choice34'] = choice34
                    if (choice34 == que34.answer):
                        request.user.userprofile.ch34 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que34,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 34,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que34.answer,
                               'userans': request.session['choice34'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page34.html', context)
    except(KeyError):
        pass

def quizpage35(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page35id = request.session['queids'][34]
            question35 = get_object_or_404(Quiz, id=page35id)
            qus = len(totalQuestions) - 1
            context = {'questions': question35,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 35,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page35.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 35, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que35 = get_object_or_404(Quiz, id=request.session['queids'][34])
                    choice35 = request.POST.get(str(que35.id))
                    request.session['choice35'] = choice35
                    if (choice35 == que35.answer):
                        request.user.userprofile.ch35 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que35,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 35,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que35.answer,
                               'userans': request.session['choice35'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page35.html', context)
    except(KeyError):
        pass

def quizpage36(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page36id = request.session['queids'][35]
            question36 = get_object_or_404(Quiz, id=page36id)
            qus = len(totalQuestions) - 1
            context = {'questions': question36,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 36,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page36.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 36, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que36 = get_object_or_404(Quiz, id=request.session['queids'][35])
                    choice36 = request.POST.get(str(que36.id))
                    request.session['choice36'] = choice36
                    if (choice36 == que36.answer):
                        request.user.userprofile.ch36 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que36,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 36,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que36.answer,
                               'userans': request.session['choice36'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page36.html', context)
    except(KeyError):
        pass

def quizpage37(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page37id = request.session['queids'][36]
            question37 = get_object_or_404(Quiz, id=page37id)
            qus = len(totalQuestions) - 1
            context = {'questions': question37,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 37,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page37.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 37, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que37 = get_object_or_404(Quiz, id=request.session['queids'][36])
                    choice37 = request.POST.get(str(que37.id))
                    request.session['choice37'] = choice37
                    if (choice37 == que37.answer):
                        request.user.userprofile.ch37 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que37,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 37,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que37.answer,
                               'userans': request.session['choice37'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page37.html', context)
    except(KeyError):
        pass

def quizpage38(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page38id = request.session['queids'][37]
            question38 = get_object_or_404(Quiz, id=page38id)
            qus = len(totalQuestions) - 1
            context = {'questions': question38,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 38,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page38.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 38, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que38 = get_object_or_404(Quiz, id=request.session['queids'][37])
                    choice38 = request.POST.get(str(que38.id))
                    request.session['choice38'] = choice38
                    if (choice38 == que38.answer):
                        request.user.userprofile.ch38 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que38,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 38,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que38.answer,
                               'userans': request.session['choice38'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page38.html', context)
    except(KeyError):
        pass

def quizpage39(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page39id = request.session['queids'][38]
            question39 = get_object_or_404(Quiz, id=page39id)
            qus = len(totalQuestions) - 1
            context = {'questions': question39,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 39,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page39.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 39, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que39 = get_object_or_404(Quiz, id=request.session['queids'][38])
                    choice39 = request.POST.get(str(que39.id))
                    request.session['choice39'] = choice39
                    if (choice39 == que39.answer):
                        request.user.userprofile.ch39 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que39,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 39,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que39.answer,
                               'userans': request.session['choice39'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page39.html', context)
    except(KeyError):
        pass

def quizpage40(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page40id = request.session['queids'][39]
            question40 = get_object_or_404(Quiz, id=page40id)
            qus = len(totalQuestions) - 1
            context = {'questions': question40,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 40,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page40.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 40, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que40 = get_object_or_404(Quiz, id=request.session['queids'][39])
                    choice40 = request.POST.get(str(que40.id))
                    request.session['choice40'] = choice40
                    if (choice40 == que40.answer):
                        request.user.userprofile.ch40 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que40,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 40,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que40.answer,
                               'userans': request.session['choice40'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page40.html', context)
    except(KeyError):
        pass

def quizpage41(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page41id = request.session['queids'][40]
            question41 = get_object_or_404(Quiz, id=page41id)
            qus = len(totalQuestions) - 1
            context = {'questions': question41,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 41,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page41.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 41, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que41 = get_object_or_404(Quiz, id=request.session['queids'][40])
                    choice41 = request.POST.get(str(que41.id))
                    request.session['choice41'] = choice41
                    if (choice41 == que41.answer):
                        request.user.userprofile.ch41 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que41,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 41,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que41.answer,
                               'userans': request.session['choice41'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page41.html', context)
    except(KeyError):
        pass

def quizpage42(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page42id = request.session['queids'][41]
            question42 = get_object_or_404(Quiz, id=page42id)
            qus = len(totalQuestions) - 1
            context = {'questions': question42,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 42,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page42.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 42, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que42 = get_object_or_404(Quiz, id=request.session['queids'][41])
                    choice42 = request.POST.get(str(que42.id))
                    request.session['choice42'] = choice42
                    if (choice42 == que42.answer):
                        request.user.userprofile.ch42 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que42,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 42,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que42.answer,
                               'userans': request.session['choice42'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page42.html', context)
    except(KeyError):
        pass

def quizpage43(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page43id = request.session['queids'][42]
            question43 = get_object_or_404(Quiz, id=page43id)
            qus = len(totalQuestions) - 1
            context = {'questions': question43,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 43,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page43.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 43, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que43 = get_object_or_404(Quiz, id=request.session['queids'][42])
                    choice43 = request.POST.get(str(que43.id))
                    request.session['choice43'] = choice43
                    if (choice43 == que43.answer):
                        request.user.userprofile.ch43 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que43,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 43,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que43.answer,
                               'userans': request.session['choice43'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page43.html', context)
    except(KeyError):
        pass

def quizpage44(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page44id = request.session['queids'][43]
            question44 = get_object_or_404(Quiz, id=page44id)
            qus = len(totalQuestions) - 1
            context = {'questions': question44,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 44,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page44.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 44, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que44 = get_object_or_404(Quiz, id=request.session['queids'][43])
                    choice44 = request.POST.get(str(que44.id))
                    request.session['choice44'] = choice44
                    if (choice44 == que44.answer):
                        request.user.userprofile.ch44 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que44,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 44,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que44.answer,
                               'userans': request.session['choice44'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page44.html', context)
    except(KeyError):
        pass

def quizpage45(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page45id = request.session['queids'][44]
            question45 = get_object_or_404(Quiz, id=page45id)
            qus = len(totalQuestions) - 1
            context = {'questions': question45,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 45,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page45.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 45, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que45 = get_object_or_404(Quiz, id=request.session['queids'][44])
                    choice45 = request.POST.get(str(que45.id))
                    request.session['choice45'] = choice45
                    if (choice45 == que45.answer):
                        request.user.userprofile.ch45 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que45,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 45,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que45.answer,
                               'userans': request.session['choice45'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page45.html', context)
    except(KeyError):
        pass

def quizpage46(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page46id = request.session['queids'][45]
            question46 = get_object_or_404(Quiz, id=page46id)
            qus = len(totalQuestions) - 1
            context = {'questions': question46,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 46,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page46.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 46, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que46 = get_object_or_404(Quiz, id=request.session['queids'][45])
                    choice46 = request.POST.get(str(que46.id))
                    request.session['choice46'] = choice46
                    if (choice46 == que46.answer):
                        request.user.userprofile.ch46 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que46,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 46,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que46.answer,
                               'userans': request.session['choice46'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page46.html', context)
    except(KeyError):
        pass

def quizpage47(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page47id = request.session['queids'][46]
            question47 = get_object_or_404(Quiz, id=page47id)
            qus = len(totalQuestions) - 1
            context = {'questions': question47,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 47,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page47.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 47, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que47 = get_object_or_404(Quiz, id=request.session['queids'][46])
                    choice47 = request.POST.get(str(que47.id))
                    request.session['choice47'] = choice47
                    if (choice47 == que47.answer):
                        request.user.userprofile.ch47 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que47,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 47,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que47.answer,
                               'userans': request.session['choice47'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page47.html', context)
    except(KeyError):
        pass

def quizpage48(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page48id = request.session['queids'][47]
            question48 = get_object_or_404(Quiz, id=page48id)
            qus = len(totalQuestions) - 1
            context = {'questions': question48,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 48,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page48.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 48, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que48 = get_object_or_404(Quiz, id=request.session['queids'][47])
                    choice48 = request.POST.get(str(que48.id))
                    request.session['choice48'] = choice48
                    if (choice48 == que48.answer):
                        request.user.userprofile.ch48 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que48,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 48,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que48.answer,
                               'userans': request.session['choice48'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page48.html', context)
    except(KeyError):
        pass

def quizpage49(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page49id = request.session['queids'][48]
            question49 = get_object_or_404(Quiz, id=page49id)
            qus = len(totalQuestions) - 1
            context = {'questions': question49,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 49,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page49.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 49, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que49 = get_object_or_404(Quiz, id=request.session['queids'][48])
                    choice49 = request.POST.get(str(que49.id))
                    request.session['choice49'] = choice49
                    if (choice49 == que49.answer):
                        request.user.userprofile.ch49 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que49,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 49,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que49.answer,
                               'userans': request.session['choice49'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page49.html', context)
    except(KeyError):
        pass

def quizpage50(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
    try:
        if value == '0':
            page50id = request.session['queids'][49]
            question50 = get_object_or_404(Quiz, id=page50id)
            qus = len(totalQuestions) - 1
            context = {'questions': question50,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 50,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page50.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 50, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que50 = get_object_or_404(Quiz, id=request.session['queids'][49])
                    choice50 = request.POST.get(str(que50.id))
                    request.session['choice50'] = choice50
                    if (choice50 == que50.answer):
                        request.user.userprofile.ch50 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que50,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 50,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que50.answer,
                               'userans': request.session['choice50'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page50.html', context)
    except(KeyError):
        pass

def quizpage51(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page51id = request.session['queids'][50]
            question51 = get_object_or_404(Quiz, id=page51id)
            qus = len(totalQuestions) - 1
            context = {'questions': question51,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 51,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page51.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 51, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que51 = get_object_or_404(Quiz, id=request.session['queids'][50])
                    choice51 = request.POST.get(str(que51.id))
                    request.session['choice51'] = choice51
                    if (choice51 == que51.answer):
                        request.user.userprofile.ch51 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que51,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 51,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que51.answer,
                               'userans': request.session['choice51'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page51.html', context)
    except(KeyError):
        pass

def quizpage52(request, value):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page52id = request.session['queids'][51]
            question52 = get_object_or_404(Quiz, id=page52id)
            qus = len(totalQuestions) - 1
            context = {'questions': question52,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 52,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page52.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 52, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que52 = get_object_or_404(Quiz, id=request.session['queids'][51])
                    choice52 = request.POST.get(str(que52.id))
                    request.session['choice52'] = choice52
                    if (choice52 == que52.answer):
                        request.user.userprofile.ch52 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que52,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 52,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que52.answer,
                               'userans': request.session['choice52'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page52.html', context)
    except(KeyError):
        pass

def quizpage53(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page53id = request.session['queids'][52]
            question53 = get_object_or_404(Quiz, id=page53id)
            qus = len(totalQuestions) - 1
            context = {'questions': question53,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 53,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page53.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 53, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que53 = get_object_or_404(Quiz, id=request.session['queids'][52])
                    choice53 = request.POST.get(str(que53.id))
                    request.session['choice53'] = choice53
                    if (choice53 == que53.answer):
                        request.user.userprofile.ch53 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que53,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 53,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que53.answer,
                               'userans': request.session['choice53'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page53.html', context)
    except(KeyError):
        pass

def quizpage54(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page54id = request.session['queids'][53]
            question54 = get_object_or_404(Quiz, id=page54id)
            qus = len(totalQuestions) - 1
            context = {'questions': question54,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 54,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page54.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 54, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que54 = get_object_or_404(Quiz, id=request.session['queids'][53])
                    choice54 = request.POST.get(str(que54.id))
                    request.session['choice54'] = choice54
                    if (choice54 == que54.answer):
                        request.user.userprofile.ch54 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que54,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 54,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que54.answer,
                               'userans': request.session['choice54'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page54.html', context)
    except(KeyError):
        pass


def quizpage55(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page55id = request.session['queids'][54]
            question55 = get_object_or_404(Quiz, id=page55id)
            qus = len(totalQuestions) - 1
            context = {'questions': question55,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 55,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page55.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 55, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que55 = get_object_or_404(Quiz, id=request.session['queids'][54])
                    choice55 = request.POST.get(str(que55.id))
                    request.session['choice55'] = choice55
                    if (choice55 == que55.answer):
                        request.user.userprofile.ch55 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que55,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 55,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que55.answer,
                               'userans': request.session['choice55'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page55.html', context)
    except(KeyError):
        pass

def quizpage56(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page56id = request.session['queids'][55]
            question56 = get_object_or_404(Quiz, id=page56id)
            qus = len(totalQuestions) - 1
            context = {'questions': question56,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 56,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page56.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 56, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que56 = get_object_or_404(Quiz, id=request.session['queids'][55])
                    choice56 = request.POST.get(str(que56.id))
                    request.session['choice56'] = choice56
                    if (choice56 == que56.answer):
                        request.user.userprofile.ch56 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que56,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 56,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que56.answer,
                               'userans': request.session['choice56'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page56.html', context)
    except(KeyError):
        pass

def quizpage57(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page57id = request.session['queids'][56]
            question57 = get_object_or_404(Quiz, id=page57id)
            qus = len(totalQuestions) - 1
            context = {'questions': question57,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 57,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page57.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 57, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que57 = get_object_or_404(Quiz, id=request.session['queids'][56])
                    choice57 = request.POST.get(str(que57.id))
                    request.session['choice57'] = choice57
                    if (choice57 == que57.answer):
                        request.user.userprofile.ch57 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que57,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 57,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que57.answer,
                               'userans': request.session['choice57'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page57.html', context)
    except(KeyError):
        pass

def quizpage58(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page58id = request.session['queids'][57]
            question58 = get_object_or_404(Quiz, id=page58id)
            qus = len(totalQuestions) - 1
            context = {'questions': question58,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 58,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page58.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 58, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que58 = get_object_or_404(Quiz, id=request.session['queids'][57])
                    choice58 = request.POST.get(str(que58.id))
                    request.session['choice58'] = choice58
                    if (choice58 == que58.answer):
                        request.user.userprofile.ch58 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que58,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 58,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que58.answer,
                               'userans': request.session['choice58'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page58.html', context)
    except(KeyError):
        pass

def quizpage59(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page59id = request.session['queids'][58]
            question59 = get_object_or_404(Quiz, id=page59id)
            qus = len(totalQuestions) - 1
            context = {'questions': question59,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 59,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page59.html', context)
    except(KeyError):
        print()

    try:
        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 59, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que59 = get_object_or_404(Quiz, id=request.session['queids'][58])
                    choice59 = request.POST.get(str(que59.id))
                    request.session['choice59'] = choice59
                    if (choice59 == que59.answer):
                        request.user.userprofile.ch59 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que59,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 59,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que59.answer,
                               'userans': request.session['choice59'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page59.html', context)
    except(KeyError):
        pass

def quizpage60(request, value):

    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec

    try:
        if value == '0':
            page60id = request.session['queids'][59]
            question60 = get_object_or_404(Quiz, id=page60id)
            qus = len(totalQuestions) - 1
            context = {'questions': question60,
                       'min': request.session['min'],
                       'sec': request.session['sec'],
                       'qus': qus,
                       'totalqus': len(totalQuestions),
                       'counter': 60,
                       'myurl': 'http://www.tvashtaa.com'
                       }
            return render(request, 'quiz/page60.html', context)
    except(KeyError):
        print()

    try:

        if value == '1':
            if request.method == "POST":
                if (int(request.session['min']) == 0) and (int(request.session['sec']) == 0):
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    return render(request, "quiz/result.html",
                                  {'attemted': 60, 'score': score, 'total': 60, 'myurl': 'http://www.tvashtaa.com'})
                else:
                    que60 = get_object_or_404(Quiz, id=request.session['queids'][59])
                    choice60 = request.POST.get(str(que60.id))
                    request.session['choice60'] = choice60
                    if (choice60 == que60.answer):
                        request.user.userprofile.ch60 = 1
                        request.user.userprofile.save()
                    data = UserProfile.objects.get(user=request.user)
                    score = data.score
                    print('score', score)
                    percentage = 0
                    if score != 0:
                        percentage = (score / 60) * 100
                    context = {'questions': que60,
                               'min': request.session['min'],
                               'sec': request.session['sec'],
                               # 'qus': qus,
                               'totalqus': len(totalQuestions),
                               'counter': 60,
                               'myurl': 'http://www.tvashtaa.com',
                               'corrans': que60.answer,
                               'userans': request.session['choice60'],
                               'score': score,
                               'percentage': percentage,
                               'message': "please select the answer"
                               }

                    return render(request, 'quiz/page60.html', context)
    except(KeyError):
        pass

def results(request):
    data = UserProfile.objects.get(user=request.user)
    score = data.score
    # score=data.ch1+data.ch2+data.ch3+data.ch4+data.ch5+data.ch6+data.ch7+data.ch8
    # if (request.user):
    #     request.user.userprofile.score = score
    #     request.user.userprofile.save()

    print('score', score)

    return render(request, "quiz/result.html",
                  {'score': score, 'total': 60, 'attemted': 60, 'myurl': 'http://www.tvashtaa.com'})

def percentile(request):
    studentscores=[]
    rank=[]
    formatstudents=[]

    students=UserProfile.objects.all()
    #print(students[0].user.userprofile.user)

    for i in range(len(students)):
        studentscores.append(students[i].score)
        formatstudents.append(students[i].user.userprofile.user)

    score=request.user.userprofile.score
    print('sco',score)
    percentage=(score/60)*100
    print('per',percentage)
    if percentage >= 80:
        message="Successfull.Take certificate at Tvashtaa"
    else:
        print("You are not allowed to take exam again")
        message = "You got <80 percentage.Try one more time"


    df = {'names': formatstudents,
          'scores': studentscores,
          'rank':rank
          }
    df1 = pd.DataFrame(df, columns=['names', 'scores'])
    print(df1)

    df1['Percentile_rank'] = 100*(df1.scores.rank(pct=True))
    rank=df1['Percentile_rank']
    print('rank',rank)
    print(df1)

    if(request.user):
        df2=df1.loc[df1['names'] == request.user]
        print(df2)
        print(df2['Percentile_rank'])
        percentile=df2['Percentile_rank']
        print(percentile)
        #saving percentile in the datbase
        request.user.userprofile.percentile = df2['Percentile_rank']
        request.user.userprofile.save()
        iname = request.user
        if str(request.user) == 'shailaja1':
            name = zip(students, rank)
            return render(request, "quiz/percentile.html", {'name': name,'myurl':'http://www.tvashtaa.com'})

        for val in df2['Percentile_rank']:
            value=val
            print('value',value)
    # for login count
    print("iname",iname)

    # if (request.user):
    #     request.user.userprofile.login_count = request.user.userprofile.login_count+1
    #     request.user.userprofile.save()


    return render(request, "quiz/percentile.html",{'iname':iname,'percentile':value,'message':message,'myurl':'http://www.tvashtaa.com'})

def generatepdf(request):
    data = UserProfile.objects.get(user=request.user)
    percentage=(data.score/60)*100
    name = str(request.user)
    print('str', type(name))
    context={'user':name.title(),
             'percentage':percentage,
             'coursename':"R Programming",
             'date':datetime.date.today()}
    pdf=render_to_pdf('quiz/generatepdf.html',context)
    # return HttpResponse(pdf, content_type='application/pdf')
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Tvashtaa_%s.pdf" % ("Certificate")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def back(request):
    if request.POST.get("minute") != None:
        min = request.POST.get("minute")
        sec = request.POST.get("second")
        request.session['min'] = min
        request.session['sec'] = sec
        print('secback',sec)

