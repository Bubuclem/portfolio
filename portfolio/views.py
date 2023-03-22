'''
Errors and Exception Handling
'''
from django.shortcuts import render

def handler404(request, exception):
    '''
    404 Error Handler
    '''
    response = render(request, 'errors/error.html', {})
    response.status_code = 404
    return response

def handler500(request):
    '''
    500 Error Handler
    '''
    response = render(request, 'errors/error.html', {})
    response.status_code = 500
    return response
