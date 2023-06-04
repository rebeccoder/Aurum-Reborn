from django.contrib import admin

# Register your models here.
from creators.models import Creator

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    pass

# creator = Creator(
#     name='Amara Thompson',
#     bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
#     location='Cornwall',
#     website='https://example.com',
#     image='media/amara-thompson.jpg'
# )

# creator.save()