from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total + 69
        free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context