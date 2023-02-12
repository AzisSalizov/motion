from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = FeedBackForm.objects.all()
    serializer_class = FeedBackFormSerializers
    

class SingletonAdvantageCreateApiView(generics.ListAPIView):
    queryset = SingletonModelAdvantage.objects.all()
    serializer_class = SingletonModelAdvantagesSerializers
    

class SingletonModelExamCreateApiView(generics.ListAPIView):
    queryset = SingletonModelExam.objects.all()
    serializer_class = SingletonModelExamsSerializers


class SingletonModelExamCreateApiView(generics.ListAPIView):
    queryset = SingletonModelExamInf.objects.all()
    serializer_class = SingletonModelExamsInfSerializers


class ExamInfVCreateApiView(generics.ListAPIView):
    queryset = ExamInf.objects.all()
    serializer_class = ExamsInfSerializers


class VideoTestimonialCreateApiView(generics.ListAPIView):
    queryset = VideoTestimonial.objects.all()
    serializer_class = VideoTestimonialsSerializers
    

class SingletonModelContactInfoCreateApiView(generics.RetrieveAPIView):
    queryset = SingletonModelContactInfo.objects.all()
    serializer_class = SingletonModelContactInfoSerializers
        

class SingletonModelAboutUsCreateApiView(generics.RetrieveAPIView):
    queryset = SingletonModelAboutUs.objects.all()
    serializer_class = SingletonModelAboutUsSerializers
         

class OurTeamCreateApiView(generics.ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializers

class SingletonModelStudyAbroadCreateApiView(generics.RetrieveAPIView):
    queryset = SingletonModelStudyAbroad.objects.all()
    serializer_class = SingletonModelStudyAbroadSerializers

class HigherEducationCreateApiView(generics.ListAPIView):
    queryset = HigherEducation.objects.all()
    serializer_class = HigherEducationSerializers


class SpecializationViewsSet(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializers

class CountryCreateApiView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class UniversityCreateApiView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers

class UnerversityGalleryCreateApiView(generics.ListAPIView):
    queryset = UnerversityGallery.objects.all()
    serializer_class = UnerversityGallerySerializers

class preparingFoExamCreateApiView(generics.RetrieveAPIView):
    queryset = preparingFoExam.objects.all()
    serializer_class = preparingFoExamerializers
    
    
