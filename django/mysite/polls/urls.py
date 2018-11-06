from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index")
    # path('show-index', views.index, name="index")
    # path('show-index/from-poll', views.index, name="index"),

    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='question_details'),
    path('<int:question_id>/results/', views.results, name='question_results'),
    path('<int:question_id>/vote/', views.vote, name='question_votes')
]
