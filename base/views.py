from django.shortcuts import render, redirect
from .models import Product, Lesson
from .forms import ProductForm
from .forms import LessonForm

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/home.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)

def lesson(request, pk):
    product = Lesson.objects.get(id=pk)
    context = {'lesson': lesson}
    return render(request, 'base/lesson.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/product_form.html', context)


def createLesson(request):
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/lesson_form.html', context)

def updateLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(instance=lesson)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/lesson_form.html', context)

def deleteLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('home')
    return render(request, 'base/detele.html', {'obj':lesson})


