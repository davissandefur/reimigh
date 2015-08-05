from django.shortcuts import render
from conjugate.models import Verb
from django.template import Context
from conjugate.form import ChoicesForm

def home(request):
    verbs = Verb.objects.all().order_by('verb')
    form = ChoicesForm()
    if request.POST:
        form = ChoicesForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['briathar']
            print(choice)
            context = Context({
                'verbs': verbs,
                'form': form,
                'choice': choice})
    else:
        context = Context({
            'verbs': verbs,
            'form': form
        })
    return render(request, 'table.html', context)
