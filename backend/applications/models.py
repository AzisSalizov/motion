from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class SingletonModel(models.Model):
    
    def save(self , *args , **kwargs):
        self.pk = 1
        super().save(*args , **kwargs)



class FeedBackForm(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    surname = models.CharField(verbose_name='Фамилия', max_length=200)
    email = models.EmailField(verbose_name='Почта', max_length=200)
    phone = models.IntegerField(verbose_name='Номер телефона')
    company = models.CharField(verbose_name='Компания' , max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class SingletonModelAdvantage(SingletonModel):
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    

class SingletonModelExam(SingletonModel):
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class SingletonModelExamInf(SingletonModel):
    img = models.ImageField(upload_to='images')
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    sub_title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
class ExamInf(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    sub_title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class VideoTestimonial(models.Model):
    url = models.URLField(verbose_name='Ссылка видеролика')


    def __str__(self):
        return self.url


class SingletonModelContactInfo(SingletonModel):
    phone = models.IntegerField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта', max_length=200)
    telegram = models.CharField(verbose_name='Ссылка телеграма',max_length=200)
    whatsapp = models.CharField(verbose_name='Ссылка whatsapp',max_length=200)
    instagram = models.CharField(verbose_name='Ссылка instagram',max_length=200)
    youtube = models.CharField(verbose_name='Ссылка youtube',max_length=200)

    def __str__(self):
        return self.email
    

class SingletonModelAboutUs(SingletonModel):
    img = models.ImageField(upload_to='images')
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    sub_title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = models.TextField(verbose_name='Описание')


    def __str__(self):
        return self.title

class OurTeam(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(verbose_name='Имя', max_length=200)
    position = models.CharField(verbose_name='Позиция' , max_length=200)


    def __str__(self):
        return self.name


class SingletonModelStudyAbroad(SingletonModel):
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    img = models.ImageField(upload_to='images')
    sub_title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = RichTextField(verbose_name='Описание')


    def __str__(self):
        return self.title


class HigherEducation(models.Model):
    title = models.CharField(verbose_name='Высшее образование' , max_length=200)


    def __str__(self):
        return self.title


class Specialization(models.Model):
    title = models.CharField(verbose_name='Cпециализация' , max_length=200)


    def __str__(self):
        return self.title

class Country(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(verbose_name='Название' , max_length=200)


    def __str__(self):
        return self.name

class University(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(verbose_name='Название' , max_length=200)
    location = models.CharField(verbose_name='Местоположения' , max_length=200)
    DateOfFoundation = models.IntegerField('Дата основания')
    country = models.ForeignKey(Country , on_delete=models.CASCADE)
    TypeOfPrograms = models.CharField('Тип Программы', max_length=200)
    age = models.IntegerField()
    language = models.CharField('Языки',max_length=200)
    Cost = RichTextField(verbose_name='Стоимость')
    icon = models.FileField(upload_to='images')
    fac_university = models.CharField(max_length=200)
    NominalDuration = models.CharField('Номинальная продолжительность', max_length=200)
    Awards = models.CharField('Награды' , max_length=200)
    TuitionFee = models.CharField('Плата за обучение' , max_length=200)
    ApplicationFee = models.CharField('Плата за подачу заявления',max_length=200)
    RegistrationFee = models.CharField('Регистрационный сбор',max_length=200)
    EntryQualication = models.CharField('Вступление Квалификация',max_length=200)
    Pre_deadline = models.CharField('До дедлайна',max_length=200)
    ApplicationDeadline = models.CharField('Срок подачи заявки' , max_length=200)
    StudiesCommence = models.CharField('Учеба Начало' , max_length=200)


    def __str__(self):
        return self.name


class UnerversityGallery(models.Model):
    university = models.ForeignKey(University , on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.university


class preparingFoExam(SingletonModel):
    title = models.CharField(verbose_name='Заголовок' , max_length=200)
    img = models.ImageField(upload_to='images')
    sub_title = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr = RichTextField(verbose_name='Описание')
    sub_title_two = models.CharField(verbose_name='Заголовок' , max_length=200)
    descr_two = RichTextField(verbose_name='Описание')


    def __str__(self):
        return self.title
    
