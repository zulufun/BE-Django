from django.db import models
from django.contrib.auth.models import models, AbstractUser
from ckeditor.fields import RichTextField

#User
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
# Create your models here.
class Category(models.Model): #courses_category
    name = models.CharField(max_length=100, null=False, unique=True)
    def __str__(self):
        return self.name
#base chung
class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.subject

########################
class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ["-id"]
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
        # db_table = 'lesson'
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique= True)
    def __str__(self):
        return self.name

