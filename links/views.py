
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect 
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
from links.forms import ResourceAddForm
from links.models import Resource


def home_page(request):
    resources = Resource.objects.all()

    return render(request, 'links/links_list.html', {'resources': resources})


def new_link(request):
    form = ResourceAddForm(request.POST or None)
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            if form.is_valid():
                form.save()
                messages.success(request, "The resource was successfully added.")
                return HttpResponseRedirect(reverse('home'), messages)
            else:
                messages.error(request, "Please, fix the following errors: ")

        elif request.POST.get('cancel_button') is not None:
            messages.error(request, "The addition of the resource was cancelled.")
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'links/add_link.html', {'form': form})
    
def view_link(request, id):
    return render(request, 'links/links_view.html', {})




    