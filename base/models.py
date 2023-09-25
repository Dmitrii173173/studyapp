from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Owner(models.Model): # massage mnogo soobsheini
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model): # room  1 komnata
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Lesson(models.Model):   # topic
    name = models.CharField(max_length=100)
    video_link = models.URLField(null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return self.name
    
class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} has access to {self.product.name}"
    

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)  # Флаг "Просмотрено"
    viewed_at = models.DateTimeField(null=True, blank=True)  # Время просмотра

    def __str__(self):
        return f"{self.user.username} viewed {self.lesson.name}"

    def mark_as_viewed(self):
        # Помечаем урок как просмотренный
        self.viewed = True
        self.viewed_at = timezone.now()
        self.save()
