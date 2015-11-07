from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'links/links_list.html')
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])
def new_link(request):
	return render(request, 'links/add_link.html',{})
	
# def view_link(request, id):
# 	return render(request, 'links/links_list.html', {})




	