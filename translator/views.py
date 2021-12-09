from django.shortcuts import render
from . import translate
# Create your views here.

def translator_view(request): #request expect a request
    if request.method == "POST":
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text)

        return render(request,'translator.html', {'output_text':output, 'original_text': original_text}) #the value of output
        #will be injected into translator html
        #adding to the dict, allows us to inject the original back into the box
    else:
        return render(request, 'translator.html')
