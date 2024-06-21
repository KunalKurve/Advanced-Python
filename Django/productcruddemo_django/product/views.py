from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from product.forms import ProductForm  
from product.models import Product  
# Create your views here.  
def prod(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form}) 

def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products}) 
'''
def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})  

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})  

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")  
'''