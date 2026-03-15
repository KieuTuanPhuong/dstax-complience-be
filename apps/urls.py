from django.urls import include, path

urlpatterns = [
    path("tax_compliance/", include("apps.tax_compliance.urls")),
]
