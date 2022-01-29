from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from djmoney.models.fields import MoneyField

User = get_user_model()



class Animal(models.Model):
	name = models.CharField(max_length=40)
	slug = AutoSlugField(populate_from='name', always_update=False)
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField(max_length=150)
	meta_description = models.CharField(max_length=200)
	timeStamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']
		db_table = 'Animals'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('animal', args=[str(self.slug)])


class SubCategory(models.Model):
	animal = models.ForeignKey(Animal, on_delete=models.CASCADE,
								null=True, blank=True, related_name='animals')
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name


class Pet(models.Model):
	seller = models.ForeignKey(User, on_delete=models.CASCADE,
								default=1)
	animal = models.ManyToManyField(Animal)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
							null=True, blank=True, related_name='pets')
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='name', always_update=False)
	breed = models.CharField(max_length=50)
	image = models.ImageField(upload_to='pets')
	old_price = MoneyField(max_digits=12, decimal_places=2, default_currency='USD',
							null=True, blank=True)
	price = MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
	is_featured = models.BooleanField(default=False)
	quantity = models.PositiveIntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet-detail', args=[str(self.slug)])

	def sale_price(self):
		if self.old_price > self.price:
			return self.price
		else:
			return None
