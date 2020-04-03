from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company
from api.models import Vacancy


# Create your views here.

def companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def companies_detail(request, company_id):
    try:
        companies = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(companies.to_json())


def vacancies_of_company(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies(request):
    vacansy = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacansy]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_detail(request, vacancy_id):
    try:
        vacancies = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancies.to_json())


def takeSalary(elem):
    return elem['salary']


def top(request):
    vacancies = Vacancy.objects.all()
    ans = []
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    vacancies_json.sort(key=takeSalary, reverse=True)
    for i in range(10):
        ans.append(vacancies_json[i])
    return JsonResponse(ans, safe=False)
