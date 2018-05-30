from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'amadon_app/index.html')

def process(request):

    items = {'1': 19.99,
        '2': 24.99,
        '3': 4.99,
        '4': 49.99
    }
    qty = request.POST['quantity']
    if request.POST['product_id'] == str(1):
        request.session['price'] = 19.99 * int(qty)
    elif request.POST['product_id'] == str(2):
        request.session['price'] = 29.99 * int(qty)
    elif request.POST['product_id'] == str(3):
        request.session['price'] = 4.99 * int(qty)
    elif request.POST['product_id'] == str(4):
        request.session['price'] = 49.99 * int(qty)
    
    request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

    if 'item_count' not in request.session:
        request.session['item_count'] = 0
    request.session['item_count'] += int(request.POST['quantity'])
    
    if 'total_spent' not in request.session:
	    request.session['total_spent'] = 0
    request.session['total_spent'] += float(request.session['purchase'])

    return redirect('/amadon/checkout')


def checkout(request):
    return render(request, 'amadon_app/response.html')