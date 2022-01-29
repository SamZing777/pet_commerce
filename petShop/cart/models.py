import random
from django.db import models
from django.urls import reverse

from pets.models import Pet


class Cart(models.Model):
	cart_id = models.CharField(max_length=10, null=True, blank=True)
	item = models.ForeignKey(Pet, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)
	quantity = models.PositiveIntegerField()

	class Meta:
		ordering = ['-date_added']

	def __str__(self):
		return str(self.item)

	def get_absolute_url(self):
		return reverse('cart_item', args=[str(self.id)])

	def get_total(self):
		self.quantity * self.item.price

	def get_name(self):
		self.item.name

	def get_price(self):
		self.item.price

	def get_augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()

	def generate_cart_id(self):
		cart_id = ''
		characters = '0123456789'
		cart_id_length=9
		for x in range(cart_id_length):
			cart_id += characters[random.randint(0, len(characters) - 1)]
		return cart_id
