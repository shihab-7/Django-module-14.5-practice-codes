from django.shortcuts import render, redirect
from .forms import UserForm, UserStudent

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['upload_your_picture']
            cv = form.cleaned_data[ 'upload_your_CV']
            with open('./first_app/upload/' + photo.name, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)
            with open('./first_app/upload/' + cv.name, 'wb+') as destination:
                for chunk in cv.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'home.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'home.html', {'form': form})

#model field rendering
def goto(request):
    if request.method == 'POST':
        form = UserStudent(request.POST, request.FILES)
        if form.is_valid():
            print (form.cleaned_data)
            form.save(commit=False)
            return redirect('home_page')
    else:
        form = UserStudent()
    return render(request, 'model.html', {'form': form})