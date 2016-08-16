from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import UserGroup, CustomUser, ShopList, Item

from .forms import UserGroupForm, ShopListForm

# Create your views here.

def home(request):
	userGroup_list = UserGroup.objects.all()
	return render(request, 'blog/home.html', {'userGroup_list' : userGroup_list})

	#####################################
	############ ShopLists ##############
	#####################################
	
def shopList_addItems(request, pk)
    shopList = get_object_or_404(ShopList, pk=pk)
	if request.method == "POST":
        form = ShopListForm(request.POST)
        if form.is_valid():
            shoplist = form.save()
            return redirect('blog.views.shopList_detail', pk1=pk, pk2=shoplist.pk)
	
def shopList_detail(request, pk1, pk2):
    shopList = get_object_or_404(ShopList, pk=pk2)
    userGroup = get_object_or_404(UserGroup, pk=pk1)
    return render(request, 'blog/shopList_detail.html', {'shopList': shopList})
	
def shopList_new(request,pk):
    userGroup = get_object_or_404(UserGroup, pk=pk)
    if request.method == "POST":
        form = ShopListForm(request.POST)
        if form.is_valid():
            shoplist = form.save()
            return redirect('blog.views.shopList_detail', pk1=pk, pk2=shoplist.pk)
    else:
        form = ShopListForm()
    return render(request, 'blog/shopList_new.html', {'form': form })
	
"""

def shopList_list(request):
    shopLists = ShopList.objects.filter(userGroup__users__contains='auth.User').order_by('created_date')
    return render(request, 'blog/shop_list.html', {'shopLists' : shopLists})

	
def shopList_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			shopList = form.save(commit=False)
			shopList.created_date = timezone.now()
			shopList.lastmaj_date = timezone.now()
			shopList.isDone = False
			shopList.save()
			return redirect('blog.views.shoplist_detail', pk=shopList.pk)
	else:
		form = PostForm()
	return render(request, 'blog/shoplist_edit.html', {'form': form})
	
def shopList_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.userGroup_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/userGroup_edit.html', {'form': form})
	
"""
	
	######################################
	############ UserGroup #############
	######################################
	
def userGroup_detail(request, pk):
    userGroup = get_object_or_404(UserGroup, pk=pk)
    return render(request, 'blog/userGroup_detail.html', {'userGroup':userGroup})
	

def userGroup_new(request):
    if request.method == "POST":
        form = UserGroupForm(request.POST)
        if form.is_valid():
            usergroup = form.save()
            return redirect('blog.views.userGroup_detail', pk=usergroup.pk)
    else:
        form = UserGroupForm()
    return render(request, 'blog/userGroup_new.html', {'form': form })

	
def userGroup_edit(request, pk):
    userGroup = get_object_or_404(UserGroup, pk=pk)
    if request.method == "POST":
        form = UserGroupForm(request.POST, instance=userGroup)
        if form.is_valid():
            usergroup = form.save()
            return redirect('blog.views.userGroup_detail', pk=usergroup.pk)
    else:
        form = UserGroupForm(instance=userGroup)
    return render(request, 'blog/userGroup_edit.html', {'form': form })