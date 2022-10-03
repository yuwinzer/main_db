from django.shortcuts import render
from .forms import OrderForm


def index(request):
    return render(request, "orders/orders.html")


def new_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "orders/orders.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'orders/new_order.html', {'form': form})
