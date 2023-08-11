# flipbook/views.py
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseBadRequest
from urllib.parse import unquote
import os



def get_pdf_files():
    pdf_folder = 'flipbook/static/pdf_files'
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    return pdf_files

def index(request):
    pdf_files = get_pdf_files()
    return render(request, 'index.html', {'pdf_files': pdf_files})

def open_flipbook(request,file_name):
    decoded_file_name = unquote(file_name)
    pdf_files = get_pdf_files()
    if decoded_file_name not in pdf_files:
        return HttpResponseBadRequest("Invalid PDF file name")
    return render(request, 'open_flipbook.html', {'file_name': decoded_file_name})

def flipbooks(request):
    pdf_files = get_pdf_files()
    return render(request, 'flipbooks.html', {'pdf_files': pdf_files})


def login(request):
    pdf_files = get_pdf_files()
    return render(request, 'login.html', {'pdf_files': pdf_files})

def logout(request):
    pdf_files = get_pdf_files()
    return render(request, 'login.html', {'pdf_files': pdf_files})

def register(request):
    pdf_files = get_pdf_files()
    return render(request, 'register.html', {'pdf_files': pdf_files})

def pdf2flipbook(request):
    if 'pdf_file' in request.FILES:
        file = request.FILES['pdf_file']
        if file.name != '':
            destination_folder = 'flipbook/static/pdf_files'
            os.makedirs(destination_folder, exist_ok=True)
            file_name = file.name
            destination_path = os.path.join(destination_folder, file_name)
            with open(destination_path, 'wb') as destination_file:
                for chunk in file.chunks():
                    destination_file.write(chunk)
            return JsonResponse({'message': 'file sucessfully uploaded.'}, status=200)
    return JsonResponse({'error': 'No file selected or error in file upload.'}, status=400)

