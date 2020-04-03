from django.urls import path
from api.views import companies
from api.views import companies_detail
from api.views import vacancies
from api.views import vacancies_detail
from api.views import  vacancies_of_company
from api.views import top
urlpatterns = [
path('companies/', companies),
path('companies/<int:company_id>/', companies_detail),
path('companies/<int:company_id>/vacancies/', vacancies_of_company),
path('vacancies/', vacancies),
path('vacancies/<int:vacancy_id>/', vacancies_detail),
path('vacancies/top_ten/', top)
]