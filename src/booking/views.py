from django.shortcuts import render


def booking(request):
    return render(
        request,
        'orders/orders.html',
    )