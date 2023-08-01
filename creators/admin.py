from django.contrib import admin

# Register your models here.
from creators.models import Creator


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    pass
