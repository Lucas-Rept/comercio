from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=220, unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Item(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.FloatField()
    unit = models.CharField(max_length=3, default="und")
    price = models.FloatField()
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    name = models.CharField(default="PAGAMENTO", max_length=20)
    quantity = models.IntegerField(default=1)
    unit = models.CharField(default='und', max_length=4)
    price = models.FloatField()
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
