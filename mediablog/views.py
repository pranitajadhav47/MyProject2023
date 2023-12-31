from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import blogcontain
from .forms import TestFromClass,ModelsDemoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

def allblogs(request):
    obj=blogcontain.objects.all()
    context={"all_blogs":obj}
    return render(request,'pages/blogs.html',context)

def addblogpage(request):
    return render(request,'pages/add_blogs.html')


def addblogshandler(request):
    if request.GET.get('title'):
        title_r=request.GET.get('title')
        description_r=request.GET.get('description')
       # author_r=request.GET.get('author')
        author_r=request.user
        no_of_line_r=request.GET.get('no_of_line')

        obj=blogcontain(title=title_r,description=description_r,
                     author=author_r,no_of_line=no_of_line_r)
        obj.save()
        return render(request,"pages/add_blogs.html",{"responce":"blog saved sucessfully"})
    else:
        return render(request,"pages/add_blogs.html",{"responce":"please fill from"})


def deleteblog(request):
     id1 = request.GET.get('id')
     
     blogcontain.objects.get(pk=id1).delete()
     context={"responce":"id deleted sucessfully"}
     return render(request,"pages/add_blogs.html",context)

def djangofroms(request):
    form=TestFromClass()
    return render(request,"pages/djangofroms.html",{"form":form})

def modelDjangoFrom(request):
    # dictionary for initial data with
    # field names as keys
    
    success = ''
    form = ModelsDemoForm(request.POST,request.FILES or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        print(request.user)
        obj.save()
        
        success = 'Successfully saved data'

    context={'form': form, 'success': success}
    return render(request, "pages/model_form.html", context)
@login_required(login_url="/admin/")
def deleteById(request,id):
    obj=blogcontain.objects.get(id=id)
    if obj.author == request.user:
        blogcontain.objects.get(pk=id).delete()
        success='successfully delted the blog'
    else:
        success=f"you cannot delete this blog author is{obj.author}"
    return render(request,'pages/blogs.html',{'success':success})

@login_required(login_url="/admin/")
def updateblog(request,id):

    obj=blogcontain.objects.get(id=id)
    if obj.author == request.user:
        pass
    else:
        return HttpResponse("you cannot delete")

    return render(request,'pages/update_view.html',{"data":obj})

def updatedata(request,id):
    success=''

    c_id=id

    c_title=request.POST.get('title')
    c_author=request.user
    c_description=request.POST.get('description')
    c_no_of_line=request.POST.get('no_of_line')
    print(c_id,c_title)

    obj=get_object_or_404(blogcontain,id=c_id)
    obj.title=c_title
    obj.author=c_author
    obj.description=c_description
    obj.no_of_line=c_no_of_line
    obj.save()
    success=f"{c_id}- data updated sucessfully"
    return render(request,'pages/blogs.html',{"success":success})


