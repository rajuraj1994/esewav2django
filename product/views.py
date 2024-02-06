from django.shortcuts import render,redirect
from . models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userspage.auth import admin_only

# Create your views here.
@login_required
@admin_only
def index(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'product/index.html',context)
@login_required
@admin_only
def post_product(request):
    # to insert product 
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product added')
            return redirect('/products/addproduct/')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'product/addproduct.html',{'forms':form})
 # to show add product form
    context={
        'forms':ProductForm
    }
    return render(request,'product/addproduct.html',context)

@login_required
@admin_only
def post_category(request):
    # to insert category 
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added')
            return redirect('/products/addcategory/')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'product/addcategory.html',{'forms':form})
 # to show add category form
    context={
        'forms':CategoryForm
    }
    return render(request,'product/addcategory.html',context)

# to show all category
@login_required
@admin_only
def show_category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'product/showcategory.html',context)

# to delete category 
@login_required
@admin_only
def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'category deleted')
    return redirect('/products/showcategory')

# to delete category
@login_required
@admin_only 
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'product deleted')
    return redirect('/products')

# to edit category
@login_required
@admin_only
def update_category(request,category_id):
    instance=Category.objects.get(id=category_id)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category updated')
            return redirect('/products/showcategory/')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'product/updatecategory.html',{'forms':form})

    context={
        'forms':CategoryForm(instance=instance)
    }
    return render(request,'product/updatecategory.html',context)

# to update product
@login_required
@admin_only
def update_product(request,product_id):
    instance=Product.objects.get(id=product_id)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product updated')
            return redirect('/products')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'product/updateproduct.html',{'forms':form})

    context={
        'forms':ProductForm(instance=instance)
    }
    return render(request,'product/updateproduct.html',context)


    