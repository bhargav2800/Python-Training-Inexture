from django.urls import path, include

#FunctionBased View  ::: 
# from .views import article_list,article_detail

#ClassBased Viewv  :::
from .views import ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    #ClassBased View
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),


    #Generic View
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    
    #functionBased View 
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail)
]