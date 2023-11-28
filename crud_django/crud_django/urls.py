from django.contrib import admin
from django.urls import path, include
from crud_app.api.viewsets import ClasseListCreateView, ClasseRetrieveView, ClasseUpdateView, ClasseDestroyView
from crud_app.api.viewsets import PersonagemListCreateView, PersonagemRetrieveView, PersonagemUpdateView, PersonagemDestroyView
from crud_app.views import create_class_view, list_classes_view, update_delete_view, create_personagem_view, list_personagem_view,update_delete_persona

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # API Classe URLs
    path('api/classes/', ClasseListCreateView.as_view(), name='classe-list-create'),
    path('api/classes/<int:pk>/', ClasseRetrieveView.as_view(), name='classe-detail'),
    path('api/classes/<int:pk>/update/', ClasseUpdateView.as_view(), name='classe-update'),
    path('api/classes/<int:pk>/delete/', ClasseDestroyView.as_view(), name='classe-delete'),
    
    # API Personagens URLs
    path('api/personagem/', PersonagemListCreateView.as_view(), name='personagem-list-create'),
    path('api/personagem/<int:pk>/', PersonagemRetrieveView.as_view(), name='personagem-detail'),
    path('api/personagem/<int:pk>/update/', PersonagemUpdateView.as_view(), name='personagem-update'),
    path('api/personagem/<int:pk>/delete/', PersonagemDestroyView.as_view(), name='personagem-delete'),

    # Frontend URLs Classes
    path('classes/create/', create_class_view, name='create_class'),
    path('classes/list/', list_classes_view, name='list_classes'),
    path('classes/update_delete/<int:class_id>/', update_delete_view, name='update_delete_classes'),
    
    #Frontend URLs Personagens
    path('personagem/create/', create_personagem_view, name='create_personagem'),
    path('personagem/list/', list_personagem_view, name='list_personagem'),
    path('personagem/update_delete/<int:persona_id>/', update_delete_persona, name='update_delete_personagem'),
]
