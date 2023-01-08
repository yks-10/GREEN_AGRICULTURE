from django.urls import path
from farm import views


urlpatterns = [
    path('', views.HealthView.as_view(), name="Health-Check"),
    path('user/', views.UserDetailView.as_view(), name="user"),
    path('scrap/', views.AgriculturalScrapsView.as_view(), name="scraps"),
    path('note/', views.FarmersNotebookView.as_view(), name="notes"),
    path('market-category/', views.MarketCategoryView.as_view(), name="category"),
    path('market-form/', views.MarketFormView.as_view(), name="form"),
    path('experience/', views.ExperienceView.as_view(), name="experience"),
    path('tool/', views.NewToolView.as_view(), name="new-tool"),
    path('farmer/', views.WonFarmerView.as_view(), name="won-farmer"),
    path('economic/', views.EconomicMarketView.as_view(), name="economic-market"),
    path('terrace/', views.TerraceView.as_view(), name="terrace"),
    path('scientist/', views.ScientistView.as_view(), name="scientist"),
    path('cultivation/', views.CropCultivationView.as_view(), name="cultivation"),
    path('husbandry/', views.AnimalHusbandryView.as_view(), name='husbandry')
]