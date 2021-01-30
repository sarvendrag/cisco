from django.shortcuts import render, redirect  
from .forms import RouterForm  
from .models import RouterDetails
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.  
def add(request):  
    if request.method == "POST":  
        form = RouterForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show')  
            except:  
                pass  
    else:  
        form = RouterForm()  
    return render(request,'index.html',{'form':form})  
def show(request):
    ctx = {}
    param = request.GET.get('q')
    if param:
        routerDetails = RouterDetails.objects.filter(Q(status=1),Q(hostname__icontains=param) | Q(sapid__icontains = param) | Q(loopback__icontains = param) | Q(mac_address__icontains = param))
    else:
        routerDetails = RouterDetails.objects.all().filter(status=1)

    if request.is_ajax():
        html = render_to_string(
            template_name="records.html", 
            context={"routerDetails": routerDetails}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
        
    ctx = {'routerDetails':routerDetails}
    return render(request,"show.html", context=ctx)  
def edit(request, id):  
    routerDetails = RouterDetails.objects.get(id=id)  
    return render(request,'edit.html', {'routerDetails':routerDetails})  
def update(request, id):  
    routerDetails = RouterDetails.objects.get(id=id)  
    form = RouterForm(request.POST, instance = routerDetails)  
    if form.is_valid():  
        form.save()  
        return redirect("/router/show")  
    return render(request, 'edit.html', {'routerDetails': routerDetails})  
def destroy(request, id):  
    routerDetails = RouterDetails.objects.filter(id=id)  
    routerDetails.update(status=0)  
    return redirect("/router/show")