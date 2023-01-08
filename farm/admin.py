from django.contrib import admin
from farm.models import UserDetails, AgriculturalScraps, FarmersNotebook,\
    MarketCategory, MarketForm, Experience, NewTool, WonFarmer, EconomicMarket, AnimalHusbandry,\
    Terrace, Scientist, CropCultivation

class UserDetailsAdminView(admin.ModelAdmin):
    model = UserDetails
    list_display = ('id', 'user_name', 'phone_number', 'state')
    list_filter = ('city', 'state')
    search_fields = ('id', 'user_name', 'phone_number')

class AgriculturalScrapsAdminView(admin.ModelAdmin):
    model = AgriculturalScraps
    list_display = ('id', 'scrap_title')
    list_filter = ('scrap_title', )

class FarmersNotebookAdminView(admin.ModelAdmin):
    model = FarmersNotebook
    list_display = ('id', 'note_title', 'note_date')
    list_filter = ('note_date', )

class MarketFormAdminView(admin.ModelAdmin):
    model = MarketForm
    list_display = ('id', 'user_name', 'item_name', 'size', 'price', 'category', 'phone_number', 'state')
    list_filter = ('id', 'user_name', 'item_name', 'state')
    search_fields = ('user_name', 'phone_number', 'state')

class ExperienceAdminView(admin.ModelAdmin):
    model = Experience
    list_display = ('id', 'title', 'category', 'exp_description')
    list_filter = ('title', 'category')
    search_fields = ('id', 'title', 'category')

class NewToolAdminView(admin.ModelAdmin):
    model = NewTool
    list_display = ('id', 'title', 'price')
    list_filter = ('title', 'price')
    search_fields = ('id', 'title')

class WonFarmerAdminView(admin.ModelAdmin):
    model = WonFarmer
    list_display = ('id', 'what', 'category')
    list_filter = ('category', 'name')
    search_fields = ('id', 'name', 'contact')

class EconomicMarketAdminView(admin.ModelAdmin):
    model = EconomicMarket
    list_display = ('id', 'name', 'category')
    list_filter = ('category', 'name')
    search_fields = ('id', 'name', 'category')

class TerraceAdminView(admin.ModelAdmin):
    model = EconomicMarket
    list_display = ('id', 'user', 'category')
    list_filter = ('category', 'user')
    search_fields = ('id', 'user', 'category')

class ScientistAdminView(admin.ModelAdmin):
    model = Scientist
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name', 'words')

class CropCultivationAdminView(admin.ModelAdmin):
    model = CropCultivation
    list_display = ('id', 'crop_name')
    search_fields = ('id', 'crop_name')

class AnimalsHusbandryAdminView(admin.ModelAdmin):
    model = AnimalHusbandry
    list_display = ('id', 'animal_name')
    search_fields = ('id', 'animal_name')

admin.site.register(UserDetails, UserDetailsAdminView)
admin.site.register(AgriculturalScraps, AgriculturalScrapsAdminView)
admin.site.register(FarmersNotebook, FarmersNotebookAdminView)
admin.site.register(MarketCategory)
admin.site.register(MarketForm, MarketFormAdminView)
admin.site.register(Experience, ExperienceAdminView)
admin.site.register(NewTool, NewToolAdminView)
admin.site.register(WonFarmer, WonFarmerAdminView)
admin.site.register(EconomicMarket, EconomicMarketAdminView)
admin.site.register(Terrace, TerraceAdminView)
admin.site.register(Scientist, ScientistAdminView)
admin.site.register(CropCultivation, CropCultivationAdminView)
admin.site.register(AnimalHusbandry, AnimalsHusbandryAdminView)