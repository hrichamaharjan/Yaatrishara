from django.shortcuts import render
posts=[
    {
        'author':'Hrichaa',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August 27, 2021'
    },
    {
    'author':'Gaurav',
            'title':'Blog Post 2',
            'content':'Second Post Content',
            'date_posted':'August 27, 2021'

        }
]


def home(request):



    return render(request,'yaatri/index.html')
def blog(request):
    context={
        'posts': posts,
        'title':'Blog'
    }

    return render(request,'yaatri/blog.html',context)

# Create your views here.
