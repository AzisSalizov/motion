from django.urls import path
from backend.applications import views


urlpatterns = [
    path('feedback' , views.FeedbackCreateAPIView.as_view()),
    path('advantages' , views.SingletonAdvantageCreateApiView.as_view()),
    path('exam' , views.SingletonModelExamCreateApiView.as_view()),
    path('exams' , views.SingletonModelExamCreateApiView.as_view()),
    path('exams_inf' , views.ExamInfVCreateApiView.as_view()),
    path('contact_info' , views.SingletonModelContactInfoCreateApiView.as_view()),
    path('about_us' , views.SingletonModelAboutUsCreateApiView.as_view()),
    path('our_team' , views.OurTeamCreateApiView.as_view()),
    path('study_abroad' , views.SingletonModelStudyAbroadCreateApiView.as_view()),
    path('higher_education' , views.HigherEducationCreateApiView.as_view()),
    path('specialization' , views.SpecializationViewsSet.as_view()),
    path('country' , views.CountryCreateApiView.as_view()),
    path('university' , views.UniversityCreateApiView.as_view()),
    path('university_gallery' , views.UnerversityGalleryCreateApiView.as_view()),
    path('preparing_for_exam' , views.preparingFoExamCreateApiView.as_view()),
]
