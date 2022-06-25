from decimal import Decimal

from django.db import models

from django.contrib.auth.models import User



class User_module(models.Model):
    username=models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    cpassword = models.CharField(max_length=40)

    class Meta:
        db_table = "User_module"


class items(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price = models.IntegerField()
    image= models.URLField(max_length=300)

    class Meta:
        db_table = "items"


class storeItem(models.Model):
    a=0
    users=models.ForeignKey(User_module,on_delete=models.CASCADE)
    item = models.ForeignKey(items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    add=models.IntegerField(default=0)
    def total(self):
        b=self.item.price*self.quantity
        return b
    def get_cart_deal_total(self):
        a=self.a+self.total()
        return a

    class Meta:
        db_table="storeItem"

class orders(models.Model):
    ordername=models.CharField(max_length=60)

    class Meta:
        db_table="orders"
class bills(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    name_on_card = models.CharField(max_length=50)
    cardno=models.IntegerField()
    expmonth=models.IntegerField()
    expyear=models.IntegerField()
    cvv=models.IntegerField()
    class Meta:
        db_table="bills"
class book_table(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    guest = models.CharField(max_length=50)
    phone = models.IntegerField()
    date_table = models.DateField(max_length=50)
    time_table = models.TimeField(max_length=60)
    category = models.CharField(max_length=50)
    msg = models.CharField(max_length=50)

    class Meta:
        db_table="book_table"

class Query_table(models.Model):
    cid = models.AutoField(primary_key=True, serialize=False),
    uname=models.CharField(max_length=50)
    dcategory=models.CharField(max_length=50)
    dcapacity=models.CharField(max_length=50)
    dprice=models.CharField(max_length=50)
    dicategory = models.CharField(max_length=50)
    dicapacity = models.CharField(max_length=50)
    diprice = models.CharField(max_length=50)
    tcategory = models.CharField(max_length=50)
    tcapacity = models.CharField(max_length=50)
    tprice = models.CharField(max_length=50)
    pcategory = models.CharField(max_length=50)
    pcapacity = models.CharField(max_length=50)
    pprice = models.CharField(max_length=50)
    rcategory = models.CharField(max_length=50)
    rcapacity = models.CharField(max_length=50)
    rprice = models.CharField(max_length=50)
    decategory = models.CharField(max_length=50)
    decapacity = models.CharField(max_length=50)
    deprice = models.CharField(max_length=50)
    drcategory = models.CharField(max_length=50)
    drcapacity = models.CharField(max_length=50)
    drprice = models.CharField(max_length=50)
    maincategory = models.CharField(max_length=50)
    maincapacity = models.CharField(max_length=50)
    mprice = models.CharField(max_length=50)

    class Meta:
        db_table="Query_table"
class Feedback_form(models.Model):
    firstname=models.CharField(max_length=50)
    mailid=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    food=models.CharField(max_length=50)
    cleanliness=models.CharField(max_length=50)
    ResponseTime=models.CharField(max_length=50)
    recommend=models.CharField(max_length=50)
    rating=models.IntegerField()

    class Meta:
        db_table="Feedback_form"
class Contact_details(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    query = models.CharField(max_length=50)

    class Meta:
        db_table="Contact_details"
class orders_food(models.Model):
    cart_items = models.ForeignKey(storeItem, on_delete=models.CASCADE)
    total=models.IntegerField()

    class Meta:
        db_table="orders_food"

class ritem(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price = models.IntegerField()
    image= models.URLField(max_length=300)

    class Meta:
        db_table = "ritem"
class recommendations(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    kind=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    newvar=models.CharField(max_length=10)

    class Meta:
        db_table="recommendations"

    class storefertilizers(models.Model):
        a = 0
        users = models.ForeignKey(User_module, on_delete=models.CASCADE)
        items = models.ForeignKey(ritem, on_delete=models.CASCADE)
        quantity = models.IntegerField(default=1)
        add = models.IntegerField(default=0)

        def total(self):
            b = self.items.price * self.quantity
            return b

        def get_cart_deal_total(self):
            a = self.a + self.total()
            return a

        class Meta:
            db_table = "storefertilizers"
