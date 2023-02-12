from .models import *
from rest_framework import serializers


class FeedBackFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeedBackForm
        fields = '__all__'

class SingletonModelAdvantagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelAdvantage
        fields = '__all__'


class SingletonModelExamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelExam
        fields = '__all__'

class SingletonModelExamsInfSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelExamInf
        fields = '__all__'


class ExamsInfSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamInf
        fields = '__all__'


class VideoTestimonialsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoTestimonial
        fields = '__all__' 


class SingletonModelContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelContactInfo
        fields = '__all__'


class SingletonModelAboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelAboutUs
        fields = '__all__'


class OurTeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'


class SingletonModelStudyAbroadSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingletonModelStudyAbroad
        fields = '__all__'

class HigherEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HigherEducation
        fields = '__all__'


class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class UnerversityGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = UnerversityGallery
        fields = '__all__'


class preparingFoExamerializers(serializers.ModelSerializer):
    class Meta:
        model = preparingFoExam
        fields = '__all__'

