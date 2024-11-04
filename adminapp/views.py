

from django.shortcuts import render
import random
import string
import calendar

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')


def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/Printer.html',a1)

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')

def randompagecall(request):
    return render(request,'adminapp/randomexample.html')

def randompagelogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
        a1={'ran':ran}
        return render(request,'adminapp/randomexample.html',a1)




from django.shortcuts import redirect
from django.contrib import auth

def logoutpagelogic(request):
    auth.logout(request)  # Logs out the user
    return redirect('projecthomepage')  # Redirect to the homepage or desired URL




def calculatorpagecall(request):
    return render(request,'adminapp/calculator.html')

def calculatorpagelogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})
def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')

from django.shortcuts import render
from datetime import datetime, timedelta
import calendar

from datetime import datetime, timedelta
import calendar
from django.shortcuts import render

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')


from django.shortcuts import render
from datetime import datetime, timedelta
import calendar


def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST.get('date1', 0))  # Get input from form
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number1)  # Calculate future date

        # Use %I instead of %-I for the 12-hour format on Windows
        formatted_date = future_date.strftime('%b. %d, %Y, %I %p')  # Format the date
        future_year = future_date.year
        is_leap_year = calendar.isleap(future_year)  # Check if it's a leap year

        leap_year_message = "Leap year" if is_leap_year else "Not a leap year"

        # Pass context variables to the template
        context = {
            'ran': future_date,  # Original future date for debugging if needed
            'formatted_date': formatted_date,  # Formatted future date
            'number_of_days': number1,  # Number of days added
            'future_year': future_year,  # Future year
            'leap_year_message': leap_year_message,  # Leap year status
        }
    else:
        # In case of a GET request, simply render the form without calculations
        context = {}

    return render(request, 'adminapp/datetimepage.html', context)


def loginpagecall(request):
    return render(request,'adminapp/loginpage.html')

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                  # Replace with your student homepage URL name
                # Make sure that 'StudentHomePage' is the name of the view, and 'studentapp' is the app namespace.
                #return render(request, 'adminapp/ProjectHomePageHomePage')
                return redirect('studentapp:StudentHomePage')

                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form':form, 'tasks':tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Fixed typo from get_object_or_484 to get_object_or_404
    task.delete()
    return redirect('add_task')

from .forms import StudentForm, FeedbackForm
from .models import StudentList

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})
def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')

from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file=request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'],dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales=df['Sales'].mean()
        df['Month']=df['Date'].dt.month
        monthly_sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x : month_names[x-1])
        plt.pie(monthly_sales,labels=monthly_sales.index, autopct = '%1.1f%%')
        plt.title('Sales Distribution Per Month')
        buffer = BytesIO()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return render(request,'adminapp/chart.html' , {
            'total_sales' : total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })
    return render(request,'adminapp/chart.html',{'form':UploadFileForm()})

def add_student_page_call(request):
    return render(request, 'adminapp/AddStudent.html')
'''
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

'''
from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})



def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('projecthomepage')  # Redirect to the same page after submission
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/feedback_form.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm

# View to list contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'adminapp/add_contact.html', {'contacts': contacts})

# View to add a contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send contact info to a specified email if requested
            if 'send_email' in request.POST:
                recipient_email = request.POST.get('recipient_email')
                send_mail(
                    subject='New Contact Created',
                    message=f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email],
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

# View to delete a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')