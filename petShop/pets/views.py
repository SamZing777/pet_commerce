from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# LoginRequiredMixin
# UserPassesTestMixin

from .models import (
	Animal,
	SubCategory,
	Pet
	)

from .forms import PetForm


class PetListPageView(generic.ListView):
	model = Pet
	context_object_name = 'pets'
	paginate_by = 16
	template_name = 'pets/pets.html'


class PetDetailPageView(generic.DetailView):
	model = Pet
	context_object_name = 'pet'
	template_name = 'pets/pet-detail.html'


class AddPetPageView(generic.CreateView):
	form_class = PetForm
	success_url = reverse_lazy('pets')
	template_name = 'pets/add-pet.html'
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class UpdatePetPageView(generic.UpdateView):
	model = Pet
	form_class = PetForm
	success_url = reverse_lazy('pets')
	template_name = 'pets/pet-update.html'
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
