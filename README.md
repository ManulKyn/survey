# survey

Тестовый опросник на API

Как установить
1. Склонировать репозиторий к себе локально ерез команду git clone
2. pip install -r requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

Доступные URLS:
api/v1/login/
api/v1/survey/create/', apiviews.create, name='survey_create'),
api/v1/survey/update/<int:survey_id>/
api/v1/survey/view/
api/v1/survey/view/active/
api/v1/question/create/
api/v1/question/update/<int:question_id>/
api/v1/choice/create/
api/v1/choice/update/<int:choice_id>/
api/v1/answer/create/
api/v1/answer/view/<int:user_id>/
api/v1/answer/update/<int:answer_id>/
