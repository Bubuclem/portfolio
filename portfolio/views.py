'''
Errors and Exception Handling
'''
from django.shortcuts import render

def handler404(request, exception):
    '''
    404 Error Handler
    '''
    return render(request, 'errors/error.html')

def handler500(request):
    '''
    500 Error Handler
    '''
    return render(request, 'errors/error.html')
