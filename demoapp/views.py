from .forms import NewForm
from django.shortcuts import redirect, render
from .models import frutables
# Create your views here.
def fun(request):
    product=frutables.objects.all()
    return render(request,'index.html',{'product':product})

def details(request,shop_id):
    fruits=frutables.objects.get(id=shop_id)
    return render(request,'details.html',{'fruits':fruits})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        image=request.FILES.get('image')
        adding=frutables(name=name,desc=desc,price=price,image=image)
        adding.save()
        print('saved succefully')
    return render(request,'add_product.html')

def update(request,id):
    obj=frutables.objects.get(id=id)
    form=NewForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'obj':obj,'form':form})

def delete(request,id):
    if request.method=='POST':
        object=frutables.object.get(id=id)
        object.delete()
        return redirect('/')
    return render(request,'delete.html')