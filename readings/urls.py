from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_readings/', views.all_readings, name='all_readings'),
    path('one_card/', views.one_card, name='one_card'),
    path('three_cards/<int:reading_type>', views.three_cards, name='three_cards'),
    path('cards/', views.CardsListView.as_view(), name='all_cards'),
    path('cards/<int:card_id>', views.card, name='card'),
    path('cards/<slug:attribute>', views.filter_by, name='filter_cards'),
    path('profile/', views.profile, name='profile'),
    path('change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('register/', views.register, name='register'),
    path('my_readings/', views.ReadingsByUserListView.as_view(), name='my_readings'),
    path('delete/<uuid:reading_id>', views.delete_reading, name='delete_reading'),
    path('search/', views.search, name='search'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]