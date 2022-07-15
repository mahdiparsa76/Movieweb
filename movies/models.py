from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.db.models.fields import SlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# Create your models here.



class Movie(models.Model):
    title=models.CharField(max_length=100)
    poster=models.ImageField(upload_to='posters/',blank=True)
    actors=models.ManyToManyField('Actor')
    slug=models.SlugField(max_length=100,null=True,unique=True)
    year = models.CharField(max_length=4)
    imbd_rating = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    length = models.CharField(max_length=10)
    body=RichTextField()
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    genere=models.ManyToManyField('Genere')
    comments = GenericRelation(Comment)
    trailer = models.FileField(upload_to='trailers',null=True,blank=True)
   

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']

    def get_absolute_url(self):
        return reverse('Movie_detail', kwargs={'slug': self.slug})

class Video(models.Model):
   
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='episode')
    title=models.CharField(max_length=50)
    body=RichTextField()
    length=models.CharField(max_length=50,default=0)
    number=models.IntegerField()
    videoUrl=models.CharField(max_length=200)
    video = models.FileField(upload_to='videos',null=True)
    slug=models.SlugField(max_length=100,null=True)
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-number']

class Actor(models.Model):
    name=models.CharField(max_length=100)
    birthday=models.DateTimeField()
    country=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,null=True,unique=True)
    avatar=models.ImageField(upload_to='actors/',blank=True,null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url=''
        return url

class Act(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title + '|' + self.actor.name

class Genere(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()

    def __str__(self):
        return self.title



