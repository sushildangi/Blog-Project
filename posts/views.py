from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")

    paginator = Paginator(queryset_list, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "post_list.html", context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Create",
        "form": form
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance,
        "title": instance.title
    }
    return render(request, "post_detail.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Updated!")
    context = {
        "instance": instance,
        "title": instance.title,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:list")
