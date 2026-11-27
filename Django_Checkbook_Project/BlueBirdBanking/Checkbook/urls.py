from django.urls import path
from . import views


urlpatterns = [
    #Sets the url path to home page index.html
    path('', views.home, name='index'),

    #Sets the url path to Create new account page
    path('create/', views.create_account, name='create'),

    # Pass the account's primary key (ID) from the URL to the balance view.
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transactions, name='transaction'),

]
