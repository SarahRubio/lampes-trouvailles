from django.urls import path

from objects.views import LightList, LightDetail, FindingList, FindingDetail, FurnitureList, FurnitureDetail

urlpatterns = [
    path('lampes', LightList.as_view(), name='light-list'),
    path('lampes/<int:pk>-<slug>', LightDetail.as_view(), name='light-detail'),
    path('meubles', FindingList.as_view(), name='finding-list'),
    path('meubles/<int:pk>-<slug>', FindingDetail.as_view(), name='finding-detail'),
    path('trouvailles', FurnitureList.as_view(), name='furniture-list'),
    path('trouvailles/<int:pk>-<slug>', FurnitureDetail.as_view(), name='furniture-detail'),
]
