from django.forms.models import model_to_dict
from requests import JSONDecodeError
from rest_framework.decorators import api_view
import json

from products.models import Product

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
        DRF API View
    """

    model_data = Product.objects.all().order_by("?").first()    
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price','sale_price'])
    return Response(data)

    #     json_data_str = json.dumps(data)
    #     # model instance (model_data)
    #     # turn a Python dict
    #     # serialization - return Json to my client
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})


