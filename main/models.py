from django.db import models
import uuid

# Create your models here.

# Model Bola
class Product(models.Model):

    # Attribute wajib
    name = models.CharField(max_length=255, default="", editable=False)
    price = models.PositiveBigIntegerField(default=0, editable=True)
    description = models.TextField(max_length=255, default="", editable=False)
    thumbnail = models.URLField(editable=True)
    category = models.CharField(default="", editable=False)
    is_featured = models.BooleanField(default=False, editable=True)
    
    # Attribute custom
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lingkar = models.FloatField(default=0, editable=False)
    stock = models.PositiveIntegerField(default=0, editable=True)
    review = models.SmallIntegerField(default=0, editable=True)
    reviewCount = models.PositiveIntegerField(default=0, editable=True)

    def __str__(self):
        return self.name
    
    def addStock(self, newStock):
        self.stock += newStock

    def reduceStock(self, soldStock):
        self.stock -= soldStock

    def giveReview(self, newReview):
        self.review = ((self.reviewCount * self.review) + newReview) / (self.review + 1)
        self.reviewCount += 1

# Model Transaksi
# class Transaksi(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     checkoutDate = models.DateField(editable=False)
#     orderOfTheDay = models.IntegerField(editable=False)

#     def __str__(self):
#         date = self.checkoutDate
#         return "TRX" + str(date.day) + str(date.month) + str(date.year) + str(self.orderOfTheDay)

#     def getItems(self):
#         return self.item_transaksi.all()
    
#     # Total harga seluruh item dalam transaksi
#     def totalHargaItems(self):
#         items = self.getItems
#         total_harga = 0

#         for item in items:
#             total_harga += item.totalHargaItem

#         return total_harga

# # Model SoldBola
# class SoldBola(models.Model):
#     id = models.UUIDField(primary_key=True, editable=True)
#     name = models.CharField(max_length=255, default="", editable=True)
#     price = models.PositiveBigIntegerField(default=0, editable=True)
#     stock = models.PositiveIntegerField(default=0, editable=True)
#     transaksi = models.ForeignKey(Transaksi, on_delete=models.SET_NULL, null=True, related_name='item_transaksi')

#     def totalHargaItem(self):
#         return self.price * self.stock