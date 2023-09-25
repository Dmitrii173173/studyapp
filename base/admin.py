from django.contrib import admin
from .models import Product, Owner, Lesson, ProductAccess

admin.site.register(Product)
admin.site.register(Owner)
admin.site.register(Lesson)
admin.site.register(ProductAccess)
