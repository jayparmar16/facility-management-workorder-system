from django.db import models
from random import sample
import datetime
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

# Create your models here.
MAIN_TYPE = (
    ('Corrective Maintenance','Corrective Maintenance'),
    ('Scheduled Maintenance','Scheduled Maintenance')
)

TYPE_MAIN = (
    ('Civil','CIVIL'),
    ('MEP','MEP')
)

NATURE_CIVIL = (
    ('Painting','Painting'),
    ('Carpentry','Carpentry'),
    ('Masonry','Masonry')
)

NATURE_MEP = (
    ('Mechanical - Pump, motors, HVAC','Mechanical - Pump, motors, HVAC'),
    ('Electrical - lighting, switch','Electrical - lighting, switch'),
    ('Plumbing','Plumbing')
)

TYPE = (
    ('Normal','Normal'),
    ('Urgent','Urgent'),
    ('Emergency','Emergency'),
    ('Other','Other')
)
STATUS = (
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('In Progress','In Progress')
)
ITEMS = (
    ('Paint','Paint'),
    ('Manpower','Manpower'),
    ('Cement','Cement'),
    ('Steel','Steel'),
    ('Concrete','Concrete'),
    ('Glass','Glass'),
    ('Brick','Brick'),
)

class Item(models.Model):
    item_code = models.IntegerField()
    item = models.CharField(choices=ITEMS,max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.item
    


class MainRequest(models.Model):
    
    def create_request_no():
        z = 'RM'+''.join(sample("0123456789", 4))
        return z
    
    user = CurrentUserField()
    Request_Number = models.CharField(default=create_request_no(), unique=True, max_length=100)
    Maintenance = models.CharField(default='Corrective Maintenance', max_length=100)
    Maintenance_Type = models.CharField(choices=TYPE_MAIN, max_length=200)
    Nature_Civil = models.CharField(choices=NATURE_CIVIL, max_length=200,  null=True, blank=True)
    Nature_MEP = models.CharField(choices=NATURE_MEP, max_length=200, null=True, blank=True)
    Type_Nature = models.CharField(choices=TYPE, max_length=200)
    Zone = models.CharField(max_length=200)
    Flat = models.CharField(max_length=200)
    Building = models.CharField(max_length=200)
    Floor = models.CharField(max_length=200)
    Complaint_Details = models.TextField(max_length=200)
    date_created = models.DateTimeField(default=datetime.datetime.today(),editable=False)
    status = models.CharField(choices=STATUS,default='Pending', max_length=20) 
    expected_date_n = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=10),editable=False)
    expected_date_u = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=1),editable=False)
    expected_date_i = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=3),editable=False)
    expected_date_o = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=10),editable=False)
    # image_1 = models.ImageField(blank=True, null=True)
    # image_2 = models.ImageField(blank=True, null=True)
    # after_image_1 = models.ImageField(blank=True, null=True)
    # after_image_2 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.Request_Number

class Completion(models.Model):
    mr = models.ForeignKey(MainRequest, to_field='Request_Number', on_delete=models.CASCADE,blank=True,null=True)
    user = CurrentUserField()
    tech_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=datetime.datetime.today(),editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=15)
    work_details = models.TextField(max_length=200)
    
    def __str__(self):
        return str(self.mr)
    
    @property
    def total_price(self):
        tp = self.quantity * self.item.price
        return tp
    



    