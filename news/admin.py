from django.contrib import admin
from .model.sports_news import SportsNews
from .model.flatform import FlatFrom,Category

@admin.register(SportsNews)
class SportsNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(FlatFrom)
class FlatFormAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass