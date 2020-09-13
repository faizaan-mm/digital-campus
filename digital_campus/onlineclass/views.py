from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    Index(Home Page) View
    '''
    return render(request, 'onlineclass/index.html')