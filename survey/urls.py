from django.urls import path
from . import apiviews

app_name = 'survey'

urlpatterns = [
    path('login/', apiviews.login, name='login'),

    path('survey/create/', apiviews.create, name='survey_create'),
    path('survey/update/<int:survey_id>/', apiviews.update, name='survey_update'),
    path('survey/view/', apiviews.view, name='survey_view'),
    path('survey/view/active/', apiviews.active_survey_view, name='active_survey_view'),

    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),

    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),

    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update')
]