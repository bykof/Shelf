from django.db import models


class Order(models.Model):
	order_date = models.DateTimeField()