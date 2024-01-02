
from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from myapp.models import Item,SubCategory,AdminOffers,MainCategory,Banner
from myapp.forms import CreateItemForm, UpdateItemForm
from django.urls import reverse_lazy
from django.db.models import Q
from account.models import Vendor
from order.models import Reviews
from cart.cart import Cart
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    maincat = MainCategory.objects.all()
    banner = Banner.objects.all()
    item = Item.objects.all().order_by('-discount') [:5]
    test = Item.objects.all().order_by('name')[:4]
    top_deal = []
    for items in item:
        if items.discount > 20:
            top_deal.append(items)
    
    return render(request,'index.html',context={'maincat':maincat,'top_deal':top_deal,'banner':banner, 'test':test})



class ItemCreateView(LoginRequiredMixin,CreateView):
    model = Item
    template_name = "myapp/create.html/"
    form_class = CreateItemForm
    success_url = reverse_lazy('active_items')
    ## To add the logged in username to the Item feild automatically
    def form_valid(self, form):
        form.instance.vendor=self.request.user.vendor
        return super(ItemCreateView,self).form_valid(form)
    

def MainCategoryListView(request):
    item = Item.objects.all()
    color = []
    brand = []
    for i in item:
        color.append(i.color)
        brand.append(i.manufacturing_brand)
    color_set = set(color)
    brand_set = set(brand)
    color_id = request.GET.get('color')
    brand_id = request.GET.get('brand')
    if brand_id and color_id:
        item = Item.objects.filter(Q(color__icontains=color_id) & Q(manufacturing_brand__icontains=brand_id) | (Q(manufacturing_brand__icontains=brand_id)|Q(color__icontains=color_id)))
    elif brand_id:
         item = Item.objects.filter(Q(manufacturing_brand__icontains=brand_id))
    elif color_id:
        item = Item.objects.filter(Q(color__icontains=color_id))
    else:
        item
    return render(request,'myapp/products.html', {'item':item, 'color_set': color_set, 'brand_set':brand_set,})
    
    

class ItemUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Item
    form_class = UpdateItemForm
    template_name = 'myapp/update.html'
    success_url = reverse_lazy('active_items')
    success_message = 'Item Updated Successfully!'

class ItemDeleteView(LoginRequiredMixin,DeleteView):
    model = Item
    template_name = 'myapp/delete_item.html'
    success_url = reverse_lazy('active_items')


def sub_category(request):
    category_id = request.GET.get('category')
    sub_category = SubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'myapp/sub_category_drop_down.html', {'sub_category': sub_category})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query','')
        posts = Item.objects.filter(Q(name__icontains=query) | Q(tags__icontains=query) | Q(description__icontains=query)).order_by('-discount')
        
        color = []
        brand = []
        for i in posts:
            color.append(i.color)
            brand.append(i.manufacturing_brand)
        color_set = set(color)
        brand_set = set(brand)
        color_id = request.GET.get('color')
        brand_id = request.GET.get('brand')
        if brand_id and color_id:
            sub_cat = posts.filter(Q(color__icontains=color_id) & Q(manufacturing_brand__icontains=brand_id) | (Q(manufacturing_brand__icontains=brand_id)|Q(color__icontains=color_id)) )
        elif brand_id:
            sub_cat = posts.filter(Q(manufacturing_brand__icontains=brand_id))
        elif color_id:
            sub_cat = posts.filter(Q(color__icontains=color_id))
        else:
            posts

        
        return render(request, 'myapp/search.html', {'query':query, 'posts':posts,'color_set': color_set, 'brand_set':brand_set,})
    else:
        return render(request, 'myapp/search.html')


     
def product_detail(request,slug):
    cart = Cart(request)
    item=get_object_or_404(Item,slug=slug)
    review = Reviews.objects.filter(item=item).order_by('-created_at')
    offer=AdminOffers.objects.all()
    cat = Item.objects.filter(category=item.category).exclude(pk=item.pk)[0:4]
    return render(request,'myapp/product_detail.html',{'item':item,'offer':offer, 'cat':cat, 'cart':cart, 'review':review})

def category_page(request,slug):
    subcat = SubCategory.objects.filter(category__slug=slug)
    return render(request, 'myapp/category_page.html', {'subcat':subcat})

def subcategory_page(request,slug):
    sub_cat = Item.objects.filter(sub_category__slug=slug)
    color = []
    brand = []
    for i in sub_cat:
        color.append(i.color)
        brand.append(i.manufacturing_brand)
    color_set = set(color)
    brand_set = set(brand)
    color_id = request.GET.get('color')
    brand_id = request.GET.get('brand')
    if brand_id and color_id:
        sub_cat = sub_cat.filter(Q(color__icontains=color_id) & Q(manufacturing_brand__icontains=brand_id) | (Q(manufacturing_brand__icontains=brand_id)|Q(color__icontains=color_id)))
    elif brand_id:
         sub_cat = sub_cat.filter(Q(manufacturing_brand__icontains=brand_id))
    elif color_id:
        sub_cat = sub_cat.filter(Q(color__icontains=color_id))
    else:
        sub_cat

    return render(request, 'myapp/subcategory_page.html', {'sub_cat':sub_cat,'color_set': color_set, 'brand_set':brand_set,})

def store(request,vendor):
    item = Item.objects.filter(vendor__store_name=vendor)
    vendor_set = Vendor.objects.filter(store_name=vendor)
    color = []
    brand = []
    for i in item:
        color.append(i.color)
        brand.append(i.manufacturing_brand)
    color_set = set(color)
    brand_set = set(brand)
    color_id = request.GET.get('color')
    brand_id = request.GET.get('brand')
    if brand_id and color_id:
        item = item.filter(Q(color__icontains=color_id) & Q(manufacturing_brand__icontains=brand_id) | (Q(manufacturing_brand__icontains=brand_id)|Q(color__icontains=color_id)))
    elif brand_id:
         item = item.filter(Q(manufacturing_brand__icontains=brand_id))
    elif color_id:
        item = item.filter(Q(color__icontains=color_id))
    else:
        item
    for i in item:
        if i.vendor == vendor_set:
            vendor = i.vendor.store_name
    return render(request,'myapp/store.html',{'item':item,'vendor':vendor, 'vendor_set':vendor_set,'color_set': color_set, 'brand_set':brand_set,})





