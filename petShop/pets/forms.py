from django import forms

from .models import Pet


class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = ['animal', 'name']

	def save(self, user=None):
		form = super(AddPetForm, self).save(commit=False)
		if user:
			form.user = user
		form.save()
		return form
