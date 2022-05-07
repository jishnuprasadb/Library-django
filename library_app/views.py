from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from library_app.forms import LoginRegister, UserRegister, Book_Add
from library_app.models import Book


def home(request):
    return render(request,'home.html')

def admin_home(request):
    return render(request,'admin_home.html')
def user_home(request):
    return render(request,'user_home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, 'Invalid Credentiels')
    return render(request, 'login.html')

def user_registration(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, 'user register successful')
            return redirect('login_view')
    return render(request, 'user_register.html', {'login_form': login_form, 'user_form': user_form})

def book_add(request):
    form = Book_Add()
    if request.method == 'POST':
        form = Book_Add(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'book added successfully')
            return redirect('book_add')
    return render(request, 'book_add.html', {'form': form})

def book_view(request):
    dataset = Book.objects.all()
    print(dataset)
    context = {
        'data': dataset
    }
    return render(request, 'book_view.html', context)

def book_update(request, id):
    obj = Book.objects.get(id=id)
    form = Book_Add(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('book_view')
    else:
        form=Book_Add(instance=obj)
    return render(request, 'book_update.html', {'form': form})

def book_delete(request,id):
    obj=get_object_or_404(Book,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('book_view')
    return render(request,'book_delete.html')

def user_book_view(request):
    dataset = Book.objects.all()
    print(dataset)
    context = {
        'data': dataset
    }
    return render(request, 'user_book_view.html', context)
