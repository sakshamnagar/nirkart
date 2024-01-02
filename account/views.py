from django.shortcuts import render,redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import UserProfile, Address, Vendor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from order.models import Order, Reviews
from django.contrib.auth.views import PasswordChangeView
from collections import Counter

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            userprofile = UserProfile.objects.create(user=user)
            return redirect("profile")
        else:
            form = SignUpForm()
            messages.error(request,'Opps! Username or email address already exists. Please use a different username.')
    return render(request,'account/signup.html',context={'form':form})



@login_required
def profile(request):
    return render(request, 'account/userprofile/profile.html')


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Profile Updated Successfully!")
            return redirect('edit_profile')
    else:
        form = SignUpForm(instance=request.user)
    
    return render(request, 'account/userprofile/edit_profile.html',{'form':form})
          

class AddressCreateView(CreateView, ListView, LoginRequiredMixin):
    model = Address
    ordering = ['set_primary=True']
    template_name = "account/userprofile/address.html/"
    form_class = AddressForm
    success_url = reverse_lazy('address')
    ## To add the logged in username to the Item feild automatically
    def form_valid(self, form):
        form.instance.user=self.request.user
        if form.instance.set_primary == True:
            Address.objects.filter(set_primary=True).update(set_primary=False)
        return super(AddressCreateView,self).form_valid(form)
    ## To List the current user address
    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        queryset = queryset.filter(user=current_user)
        return queryset
    
class AddressUpdateView(LoginRequiredMixin,UpdateView):
    model = Address
    form_class = AddressUpdateForm
    template_name = 'account/userprofile/edit_address.html/'
    success_url = reverse_lazy('address')
    
    
class AddressDeleteView(LoginRequiredMixin,DeleteView):
    model = Address
    template_name = 'account/userprofile/delete_address.html'
    success_url = reverse_lazy('address')

class ChangePassword(LoginRequiredMixin,PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'account/userprofile/change_password.html'
    success_url = reverse_lazy('profile')
    success_message = 'Password Changed Sucessfully!'

@login_required
def my_order(request):
    orders = Order.objects.filter(Q(buyer=request.user), Q(status = 'Order_Placed') | Q(status = 'Order_Confirmed')).order_by("-created_at")
    completed_order = Order.objects.filter(Q(buyer=request.user), Q(status = 'Order_Shipped') | Q(status = 'Order_Cancelled')).order_by("-created_at")
    return render(request,'account/userprofile/my_orders.html',{'orders':orders, 'completed_order':completed_order})


@login_required
def my_reviews(request):
    review = Reviews.objects.filter(user=request.user).order_by("-created_at")
    order = Order.objects.filter(Q(buyer=request.user), Q(review = False), Q(status = 'Order_Shipped') | Q(status = 'Order_Cancelled'))
    return render(request,'account/userprofile/my_reviews.html',{'review':review,'order':order})



@login_required
def vendor_signup(request):
    form = VendorForm
    userprofile = UserProfile
    if request.method=='POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            userprofile = UserProfile.objects.filter(user=request.user).update(is_vendor=True)
            return redirect('profile')
        else:
            messages.error(request,'Store name already exists. Please enter a different sture name.')
    else:
        form = VendorForm()
    return render(request,'account/vendor_signup.html',context={'form':form})

@login_required
def vendor_dash(request):
    item = Item.objects.filter(vendor=request.user.vendor)
    order = Order.objects.filter(item_vendor=request.user.vendor)
    total_earnings = 0
    for i in order:
        total_earnings += i.item_price
    total_active_items = item.count()
    total_sold_items = order.count()

    return render(request,'account/vendor_dash/vendor_dash.html',{'total_earnings':total_earnings,'total_active_items':total_active_items,'total_sold_items':total_sold_items,})

@login_required
def active_items(request):
    item = Item.objects.filter(vendor=request.user.vendor)
    return render(request,'account/vendor_dash/active_items.html',{'item':item})

@login_required
def edit_seller_profile(request):
    if request.method == "POST":
        form = UpdateVendorForm(request.POST, instance=request.user.vendor)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Profile Updated Successfully!")
            return redirect('edit_seller_profile')
    else:
        form = UpdateVendorForm(instance=request.user.vendor)
    
    return render(request, 'account/vendor_dash/edit_seller_profile.html',{'form':form})


@login_required
def seller_order(request):
    orders = Order.objects.filter(Q(item_vendor=request.user), Q(status = 'Order_Placed') | Q(status = 'Order_Confirmed')).order_by("-created_at")
    completed_order = Order.objects.filter(Q(item_vendor=request.user), Q(status = 'Order_Shipped') | Q(status = 'Order_Cancelled')).order_by("-created_at")
    if request.method == "POST":
        status = request.POST.get('status')
        order = request.POST.get('order')
        Order.objects.filter(order_id=order).update(status=status)
    return render(request,'account/vendor_dash/orders.html',{'orders':orders, 'completed_order':completed_order,})

@login_required
def seller_review(request):
    review = Reviews.objects.filter(item__vendor=request.user.vendor).order_by('-created_at')
    review_length = review.count()
    total_review = 0
    one = []
    two = []
    three = []
    four = []
    five = []
    top_rated = []
    for rev in review:
        total_review += rev.rating
        if rev.rating == 1:
            one.append(rev.rating)
        elif rev.rating == 2:
            two.append(rev.rating)
        elif rev.rating == 3:
            three.append(rev.rating)
        elif rev.rating == 4:
            four.append(rev.rating)
        elif rev.rating == 5:
            five.append(rev.rating)
            top_rated.append(rev.item)
    one_bar = (len(one)/review_length)*100
    two_bar = (len(two)/review_length)*100
    three_bar = (len(three)/review_length)*100
    four_bar = (len(four)/review_length)*100
    five_bar = (len(five)/review_length)*100 
    if total_review > 0:
        avg_rating = total_review/review_length
    return render(request,'account/vendor_dash/review.html',{'review':review,'review_length':review_length ,'avg_rating':avg_rating,'one_bar':one_bar,'two_bar':two_bar,'three_bar':three_bar,'four_bar':four_bar,'five_bar':five_bar,
                                                             'one':one,'two':two,'three':three,'four':four,'five':five,'top_rated':top_rated[:3]})