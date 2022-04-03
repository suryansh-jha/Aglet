from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class ProductPayment(models.Model):
    name = models.CharField(max_length=255)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    amount = models.CharField(max_length=100)
    ShippingAddress = models.CharField(max_length=500)

    def __str__(self):
        return self.order_id


class comment (models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete= models.CASCADE)
    commenter_name = models.CharField(max_length= 200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)


class Detail(models.Model):
    rating = models.IntegerField()
    deliver_by = models.DateField()
    description = models.CharField(max_length=2000)


class ShippingAddress(models.Model):
    shipping_address_1 = models.CharField(max_length=1000)
    shipping_address_2 = models.CharField(max_length=1000)
    shipping_address_3 = models.CharField(max_length=1000)



