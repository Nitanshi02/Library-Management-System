from django.urls import path 
from system import views

urlpatterns=[
  path('', views.search_form),
  path('getd/',views.search_form1, name="my_function"),
  path('getd1/',views.fetch, name="my_function1"),
  path('getd2/',views.update, name="my_function2"),
  path('getd3/',views.update1, name="my_function3"),
  path('getd4/',views.issue, name="my_function4"),
  path('getd5/',views.issue1, name="my_function5"),
  path('getd6/',views.issue2, name="my_function6"),
  path('getd7/',views.returns, name="my_function7"),
  path('getd8/',views.retrieves, name="my_function8"),
  path('getd9/',views.display1,name="my_function9"),
  path('getd10/',views.issue_tab,name="my_function10"),
  path('getd11/',views.hello,name="my_function11"),
  path('getd12/',views.book,name="my_function12")
  
]
