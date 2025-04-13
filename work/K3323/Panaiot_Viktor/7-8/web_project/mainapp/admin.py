# mainapp/admin.py
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'specialty', 'rating', 'created_at')
    list_filter = ('specialty', 'rating')
    search_fields = ('name', 'email', 'message')
