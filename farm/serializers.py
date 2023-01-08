from farm.models import *
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'


class AgriculturalScrapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalScraps
        fields = ('id', 'scrap_title', 'scrap_description')


class FarmersNotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersNotebook
        fields = '__all__'

class MarketCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketCategory
        fields = ('id', 'title', 'category_img')

class MarketFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketForm
        fields = '__all__' #('id', 'user')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'title', 'category', 'success_img', 'exp_description')

class NewToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTool
        fields = '__all__' #('id', 'user')

class WonFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WonFarmer
        fields = '__all__' #('id', 'user')

class EconomicMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicMarket
        fields = ('id', 'name', 'quantity', 'price')

class TerraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrace
        fields = ('id', 'user', 'title', 'description', 'category')

class ScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = ('id', 'name', 'scientist_img', 'words')

class CropCultivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCultivation
        fields = ('id', 'crop_name', 'steps')

class AnimalHusbandrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalHusbandry
        fields = ('id', 'animal_name', 'husbandry')