from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed


# Create your views here.

# def http_response(request):
    # return HttpResponse('Hello HttpResponse')
    # response = HttpResponse()
    # response.write("<p>Hello, World!</p>")
    # response.write("<p>Hello, World Wide Web II!</p>")
    # return response

    # response = HttpResponse()
    # response.headers['Name'] = 'Andrei'
    # response.headers['Location'] = 'some location'
    # del response.headers['Location']
    # return response

# def http_response(request):
#     response = HttpResponse(headers={'Name': 'Andrei', 'Location': 'Italy'})
#     return response

def http_response(request):
    response = HttpResponseNotAllowed(['POST'])
    response.write("<p>This is a response.</p>")
    return response
