from django.http import JsonResponse

def products(request):
    if request.method == 'GET':
        product = {

        }
        return JsonResponse(product)
