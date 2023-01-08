from django.db import models
from green_agriculture.constant import *
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserDetails(BaseModel):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'user Details'
        ordering = ['-pk']


class AgriculturalScraps(BaseModel):
    scrap_title = models.CharField(max_length=50, null=True, blank=True)
    scrap_description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Agricultural Scrap'
        verbose_name_plural = 'Agricultural Scraps'
        ordering = ['-pk']


class FarmersNotebook(BaseModel):
    note_user = models.CharField(max_length=50, null=True, blank=True)
    note_title = models.CharField(max_length=50, null=True, blank=True)
    note_date = models.CharField(max_length=60, null=True, blank=True)
    note_description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Farmers Note'
        verbose_name_plural = 'Farmers Notes'
        ordering = ['-pk']


class MarketCategory(BaseModel):
    title = models.CharField(max_length=30, choices=CATEGORY, blank=True, null=True)
    category_img = models.CharField(max_length=3000, null=True, blank=True)

    class Meta:
        verbose_name = 'Market Category'
        verbose_name_plural = 'Market Categories'
        ordering = ['-pk']


class MarketForm(BaseModel):
    TRADE_ACTIONS = [
        (BUY, BUY),
        (SELL, SELL),
    ]
    item_name = models.CharField(max_length=80, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    price = models.CharField(max_length=6, null=True, blank=True)
    prod_image = models.CharField(max_length=3000, null=True, blank=True)
    prod_description = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY, blank=True, null=True)
    trade_type = models.CharField(max_length=10, choices=TRADE_ACTIONS, default=BUY)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10,null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Market Form'
        verbose_name_plural = 'Market form'
        ordering = ['-pk']


class Experience(BaseModel):
    title = models.CharField(max_length=80, null=True, blank=True)
    category = models.CharField(max_length=30, choices=AGRICULTURE_CATEGORY, default=FLOWERS)
    success_img = models.CharField(max_length=3000, null=True, blank=True)
    exp_description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['-pk']


class NewTool(BaseModel):
    title = models.CharField(max_length=80, null=True, blank=True)
    tools_img = models.CharField(max_length=3000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        verbose_name = 'New Tool'
        verbose_name_plural = 'New Tools'
        ordering = ['-pk']


class WonFarmer(BaseModel):
    what = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=30, choices=AGRICULTURE_CATEGORY, default=FLOWERS)
    description = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Won Farmer'
        verbose_name_plural = 'Won Farmers'
        ordering = ['-pk']


class EconomicMarket(BaseModel):
    name =  models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=30, choices=AGRICULTURE_CATEGORY, default=FLOWERS)
    quantity = models.CharField(max_length=10, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Economic Market'
        verbose_name_plural = 'Economic Markets'
        ordering = ['-pk']


class Terrace(BaseModel):
    user = models.CharField(max_length=80, null=True, blank=True)
    title = models.CharField(max_length=80, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    category = models.CharField(max_length=30, choices=AGRICULTURE_CATEGORY, default=FLOWERS)

    class Meta:
        verbose_name = 'Terrace'
        verbose_name_plural = 'Terraces'
        ordering = ['-pk']


class Scientist(BaseModel):
    name  = models.CharField(max_length=100, null=True, blank=True)
    scientist_img = models.CharField(max_length=3000, null=True, blank=True)
    words = models.CharField(max_length=3000, null=True, blank=True)

    class Meta:
        verbose_name = 'Scientist'
        verbose_name_plural = 'Scientists'
        ordering = ['-pk']


class CropCultivation(BaseModel):
    crop_name = models.CharField(max_length=100, null=True, blank=True)
    steps = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name = 'Crop Cultivation'
        verbose_name_plural = 'Crop Cultivations'
        ordering = ['-pk']


class AnimalHusbandry(BaseModel):
    animal_name = models.CharField(max_length=100, null=True, blank=True)
    husbandry = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name = 'Animal Husbandry'
        verbose_name_plural = 'Animals Husbandry'
        ordering = ['-pk']
