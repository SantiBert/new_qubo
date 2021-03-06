from django.urls import path
from .views import (ProfileUpdate,
                    EmailUpdate,
                    NameUpdate,
                    AdministrationView,
                    IndexView,
                    SearchView
                    )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/name/', NameUpdate.as_view(), name="profile_name"),
    path('resultados/', SearchView.as_view(), name='search'),



]
