from http.client import HTTPResponse

from django.shortcuts import render, redirect


from .models import Shop

# Create your views here.
def main_page(request):
    products = Shop.objects.all() # SELECT * FROM Shop;
    context = {'products': products}
    return render(request, 'index.html', context)


def add_product_view(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        price = form.get('price')
        count = form.get('count')
        image = request.FILES.get('image')
        product = Shop.objects.create(name=name, price=price, count=count, image=image)
        product.save()
        return redirect('home')
    return render(request, 'add_product.html')


def nimadir(request):
    return HTTPResponse("salom Dunyo")


def teacher(request):
    return HTTPResponse("Salom Teacher")


