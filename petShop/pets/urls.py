from django.urls import path

from .views import (
	PetListPageView,
	PetDetailPageView,
	AddPetPageView,
	UpdatePetPageView
	)

urlpatterns = [
	path('', PetListPageView.as_view(), name='pets'),
	path('<slug:slug>/', PetDetailPageView.as_view(), name='pet-detail'),
	path('add/', AddPetPageView.as_view(), name='add-pet'),
	path('<slug:slug>/update/', UpdatePetPageView.as_view(), name='update-pet')
]
