from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    LIT = 'LIT', 'Literatura'
    SCI = 'SCI', 'Ciências'
    GR = 'GR', 'Geral'

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    text = models.TextField()
    categories = models.CharField(
        max_length=3,
        choices = Categorias.choices,
        default = Categorias.GR,
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_category_label(self):
        return self.get_categories_display()
    
    def __str__(self):
        return self.title
        