from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"one.html")


def images(request):
    bats=request.POST.get('t1')
    bolw=request.POST.get('t2')
    wk=request.POST.get('t3')
    if bats=="on":
        res1="yes"
    else:
        res1=None
    if bolw == "on":
        res2 = "yes"
    else:
        res2 = None
    if wk == "on":
        res3 = "yes"
    else:
        res3 = None
    data={'res1':res1,'res2':res2,'res3':res3}
    return render(request, "two.html", {'data1':data})