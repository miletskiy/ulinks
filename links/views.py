from django.shortcuts import render

# Create your views here.
from links.forms import ResourceAddForm

def home_page(request):
	return render(request, 'links/links_list.html')
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])
def new_link(request):
	return render(request, 'links/add_link.html',{'form': ResourceAddForm()})
	
# def view_link(request, id):
# 	return render(request, 'links/links_list.html', {})




	