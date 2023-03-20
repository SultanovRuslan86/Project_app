from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Clients

class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'full'),
        ('student', 'student'),
        ('discount', 'discount'),
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"type of plan: {self.plan_type}, discount_percent: {self.discount_percent}"

class Subscription(models.Model):
    client = models.ForeignKey(Clients, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

















