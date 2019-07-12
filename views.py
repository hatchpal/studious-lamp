import requests
from django.http import HttpResponse
from django.shortcuts import render


def page():

    pages = [
            {"name": "homepage", "path": "/"},
            {"name": "experience", "path": "experience"},
            {"name": "education", "path": "experience#education"},
            {"name": "skills", "path": "skills"},
            {"name": "interests", "path": "skills#interests"},
            {"name": "let's collaborate", "path": "contact"},
            {"name": "github", "path": "github"},
        ]
    return pages

def index(request):
    
    context = { "pages": page() }
    return render(request, 'index.html', context)

def experience_me(request):

    context = { "pages": page() }
    return render(request, 'experience.html', context)

def education_me(request):

    context = { "pages": page() }
    return render(request, 'experience.html', context)

def skills_me(request):

    context = { "pages": page() }
    return render(request, 'skills.html', context)

def interests_me(request):

    context = { "pages": page() }
    return render(request, 'skills.html', context)

def contact_me(request):

    context = { "pages": page() }
    return render(request, 'contact.html', context)

def github_api_example(request):
# We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/hatchpal/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
        "pages": page()
    }
    return render(request, 'github.html', context)


# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://api.github.com/users/michaelpb/repos')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)


