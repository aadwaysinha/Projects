from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.http import HttpResponse, HttpResponseRedirect

testKW = {'hello': 'whhatp',
          'what': 'yolo',
          'light': 'found it',
          'heavy': 'oh yeeeea'}

# Create your views here.
class keyword(TemplateView):
    template_name = 'keyword.html'

def SpeechFormView(request):
    form = forms.SpeechForm()

    if request.method == 'POST':
        form = forms.SpeechForm(request.POST or None)

        if form.is_valid():
            #keyword extraction function
            print('Validation successful.')
            transcript = form.cleaned_data['data']
            #https://stackoverflow.com/questions/32274852/django-dictionary-passed-in-redirect-is-not-showing-in-template
            if transcript in testKW:
                request.session['kw'] = testKW[transcript]
                print('found key')
            else:
                request.session['kw'] = 'sorry. no result found'
                print('key not found')
            return HttpResponseRedirect('/voice/keyword/')

    return render(request, 'speechForm.html', {'speechForm': form})  #speechForm is the form instance
                                                                     #which will be loaded in the html
