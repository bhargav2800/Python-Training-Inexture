	from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# ClassBased APIView
from rest_framework.views import APIView

# GenericViews
from rest_framework import generics
from rest_framework import mixins

# Viewsets
from rest_framework import viewsets

# Authentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated





# Create your views here.

# <<<<<<<<< ---------- Function Base api_view  ----------->>>>>>>>>>

# <------------- Converted to api_view()   -> Changes :-  Inseted of JsonResponse user Responce, Not need to pass request from JSONParse().parse(request)  we can direct get data from request.data , useed status codes ---------->

# @csrf_exempt
# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)  # Here, We have to set many=True Because We are Serializing Whole Queryset
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status=201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# <------------- Converted to api_view()  ---------->

# @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         # return HttpResponse(status=404)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data)
#
#
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         # return HttpResponse(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)







# <<<<<<<<< ---------- Class Base APIView  ----------->>>>>>>>>>

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)  # Here, We have to set many=True Because We are Serializing Whole Queryset
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_article_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            # return HttpResponse(status=404)
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_article_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def put(self, request, id):
        article = self.get_article_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_article_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# <<<<<<<<< ---------- Generic View  ----------->>>>>>>>>>

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)




# <<<<<<<<< ---------- ViewSets.ViewSet  ----------->>>>>>>>>>
# We Have to write whole method by our selves  like apiview   ... It hase various methods...

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# <<<<<<<<< ---------- viewSets.GenericViewset  ----------->>>>>>>>>>
# <<<<<<<<< ---------- Just Add the mixins according to need ---------->>>>>>>>>

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()






## <<<<<<<<< ---------- viewSets.ModelViewSet  ----------->>>>>>>>>>
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()





# Conclusion of ViewSets in DRF:
#
#     common Parameters:
#         - QuerySet
#         - authentication_classes
#         - permission_classes
#         - serializer_class
#         - lookup_field
#
#     Difference :
#         viewsets.ViewSet  -->> We Have to write All function(get,post,put, .....).
#         viewsets.GenericViewSet   --->>>  We have to just add mixins for all function(get,post,put,.....).
#         viewsets.ModelViewSet   --->>>  All functions are Inbuilt.


