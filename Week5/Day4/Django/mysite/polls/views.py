from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    message = "Hello, this is my first page"
    return HttpResponse(message)


def post(request, post_id: int):
    data = {1: "This is 1st post", 2: "Second post"}
    post = data.get(post_id, "no such post")
    return HttpResponse(post)


def about(request):
    text = """<h1> BLABLAVLA</h1>\n""" * 100
    return HttpResponse


def all_posts(request, author_name: str):
    try:
        author = Author.objects.get(name=author_name)
        author_posts = author.post_set.all()
        content = ""
        for post in author_posts:
            content += post.title + "\n"
        return HttpResponse(content)
    except Author.DoesNotExist:
        return HttpResponse("No such author")
