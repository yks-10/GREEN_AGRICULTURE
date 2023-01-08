from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from farm.models import UserDetails, AgriculturalScraps, \
    FarmersNotebook, MarketCategory, MarketForm, Experience, \
    NewTool, WonFarmer, EconomicMarket, Terrace, Scientist, CropCultivation, AnimalHusbandry
from farm.serializers import UserDetailSerializer, AgriculturalScrapsSerializer,\
    FarmersNotebookSerializer, MarketCategorySerializer, MarketFormSerializer, ExperienceSerializer,\
    NewToolSerializer, WonFarmerSerializer, EconomicMarketSerializer, TerraceSerializer,\
    ScientistSerializer, CropCultivationSerializer, AnimalHusbandrySerializer


class HealthView(APIView):
    def get(self, request):
        """
            @description: This API used to check if server is active or not
            @param request:
            @return: "SUCCESS"
        """
        response = {"status": "success"}
        return Response(response)

class UserDetailView(APIView):

    def get(self, request):
        """
            to get the specific user
            @param request: phone number
            @return: deta
        """
        try:
            phone_number = request.GET.get("phone_number")
            if phone_number:
                detail = UserDetails.objects.get(phone_number=phone_number)
                serializer = UserDetailSerializer(detail)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            to create a user detail
            @param request: data
            @return: success
        """
        try:
            data = request.data
            name = data.get('name')
            phone_number = data.get('phone_number', None)
            address = data.get('address', None)
            city = data.get('city', None)
            state = data.get('state', None)
            exists = UserDetails.objects.get(phone_number=phone_number)
            if exists:
                exists.user_name = name
                exists.phone_number = phone_number
                exists.address = address
                exists.city = city
                exists.state = state
                exists.save()
            else:
                UserDetails.objects.create(user_name=name, phone_number=phone_number,
                                           address=address, city=city, state=state)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class AgriculturalScrapsView(APIView):

    def get(self, request):
        """
            All agricultural scraps
        """
        try:
            detail = AgriculturalScraps.objects.all()
            serializer = AgriculturalScrapsSerializer(detail, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            to create a user detail
            @param request: scraps_title, scraps_description
            @return: success
        """
        try:
            data = request.data
            title = data.get('scrap_title')
            description = data.get('scrap_description', None)
            AgriculturalScraps.objects.create(scrap_title=title, scrap_description=description)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class FarmersNotebookView(APIView):
    """
        return the note
    """

    def get(self, request):
        """
            All agricultural scraps
        """
        note_user = request.GET.get("note_user")
        try:
            if note_user:
                detail = FarmersNotebook.objects.filter(note_user=note_user)
                serializer = FarmersNotebookSerializer(detail, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            to create a user detail
            @param request: scraps_title, scraps_description
            @return: success
        """
        try:
            data = request.data
            note_user = data.get('note_user')
            note_title = data.get('note_title')
            note_date = data.get('note_date')
            note_description = data.get('note_description', None)
            FarmersNotebook.objects.create(note_user=note_user, note_title=note_title, note_date=note_date,
                                           note_description=note_description)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class MarketCategoryView(APIView):
    """
        category for the market
    """

    def get(self, request):
        """
            to view all the category
        """
        try:
            category =  MarketCategory.objects.all()
            serializer =  MarketCategorySerializer(category, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """
            to add a category
        """
        try:
            data = request.data
            title = data.get('title')
            category_img = data.get('category_img', None)
            MarketCategory.objects.create(title=title, category_img=category_img)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class MarketFormView(APIView):
    def get(self, request):
        """
            to view all the category
        """

        t_type = request.GET.get("trade_type")
        category = request.GET.get("category")
        try:
            form_data = MarketForm.objects.filter(trade_type=t_type.upper(), category=category.upper())
            serializer = MarketFormSerializer(form_data, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """
            adds the mark form details
        """
        try:
            data = request.data
            item_name = data.get('item_name')
            size = data.get('size', None)
            price = data.get('price', None)
            prod_image = data.get('prod_image', None)
            prod_description = data.get('prod_description', None)
            category = data.get('category', None)
            trade_type = data.get('trade_type', None)
            user_name = data.get('user_name', None)
            phone_number = data.get('phone_number', None)
            address = data.get('address', None)
            city = data.get('city', None)
            state = data.get('state', None)
            MarketForm.objects.create(item_name=item_name, size=size, price=price, prod_image=prod_image,
                                      prod_description=prod_description, category=category, trade_type=trade_type,
                                      user_name=user_name, phone_number=phone_number, address=address, city=city, state=state)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class ExperienceView(APIView):
    """
        experience for the market
    """

    def get(self, request):
        """
            to view all the experience
        """
        try:
            experience =  Experience.objects.all()
            serializer =  ExperienceSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            to add a experience
        """
        try:
            data = request.data
            title = data.get('title')
            category = data.get('category', None)
            success_img = data.get('success_img', None)
            exp_description = data.get('exp_description', None)
            Experience.objects.create(title=title, category=category, success_img=success_img, exp_description=exp_description)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class NewToolView(APIView):
    """
        NewToolView add and view the tools
    """

    def get(self, request):
        """
            to view all the tool
        """
        try:
            experience =  NewTool.objects.all()
            serializer =  NewToolSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new tool
        """
        try:
            data = request.data
            title = data.get('title')
            tools_img = data.get('tools_img', None)
            description = data.get('description', None)
            price = data.get('price', None)
            NewTool.objects.create(title=title, tools_img=tools_img, description=description,
                                      price=price)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class WonFarmerView(APIView):
    """
        WonFarmerView add and view to succeed farmer
    """

    def get(self, request):
        """
            to view all to succeed farmer
        """
        try:
            experience =  WonFarmer.objects.all()
            serializer =  WonFarmerSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new tool
        """
        try:
            data = request.data
            what = data.get('what')
            category = data.get('category', None)
            description = data.get('description', None)
            name = data.get('name', None)
            contact = data.get('contact', None)
            WonFarmer.objects.create(what=what, category=category, description=description,
                                      name=name, contact=contact)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class EconomicMarketView(APIView):
    """
        EconomicMarketView add and view to succeed farmer
    """

    def get(self, request):
        """
            to view all to economic market
        """
        try:
            experience =  EconomicMarket.objects.all()
            serializer =  EconomicMarketSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new economic
        """
        try:
            data = request.data
            name = data.get('name')
            category = data.get('category', None)
            quantity = data.get('quantity', None)
            price = data.get('price', None)
            EconomicMarket.objects.create(name=name, category=category, quantity=quantity,
                                      price=price)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class TerraceView(APIView):
    """
        TerraceView add and view to terrace
    """

    def get(self, request):
        """
            to view all to terrace
        """
        user = request.GET.get("user")
        try:
            if user:
                detail = Terrace.objects.filter(user=user)
                serializer = TerraceSerializer(detail, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new terrace
        """
        try:
            data = request.data
            user = data.get('user')
            title = data.get('title', None)
            description = data.get('description', None)
            category = data.get('category', None)
            Terrace.objects.create(user=user, title=title, description=description, category=category)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class ScientistView(APIView):
    """
        ScientistView add and view to scientist
    """

    def get(self, request):
        """
            to view all to scientist
        """
        try:
            experience =  Scientist.objects.all()
            serializer =  ScientistSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new terrace
        """
        try:
            data = request.data
            name = data.get('name')
            scientist_img = data.get('scientist_img', None)
            words = data.get('words', None)
            Scientist.objects.create(name=name, scientist_img=scientist_img, words=words)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class CropCultivationView(APIView):
    """
        CropCultivationView add and view to Crop cultivation technique
    """

    def get(self, request):
        """
            to view all to scientist
        """
        try:
            experience =  CropCultivation.objects.all()
            serializer =  CropCultivationSerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new terrace
        """
        try:
            data = request.data
            crop_name = data.get('crop_name')
            steps = data.get('steps', None)
            CropCultivation.objects.create(crop_name=crop_name, steps=steps)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class AnimalHusbandryView(APIView):
    """
        AnimalHusbandryView add and view to animal husbandry
    """

    def get(self, request):
        """
            to view all to scientist
        """
        try:
            experience =  AnimalHusbandry.objects.all()
            serializer =  AnimalHusbandrySerializer(experience, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            adds a new husbandry
        """
        try:
            data = request.data
            animal_name = data.get('animal_name')
            husbandry = data.get('husbandry', None)
            AnimalHusbandry.objects.create(animal_name=animal_name, husbandry=husbandry)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)