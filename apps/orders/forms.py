from django.forms import ModelForm

from apps.orders.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'customer', 'deadline', 'source', 'note']


# order = Order.objects.get(pk=1)
# form = OrderForm(instance=order)
