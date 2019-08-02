from django.contrib import admin
from app.models import Track, Speaker, Session

# Register your models here.
admin.site.register(Track)

# Custom class
class SpeakerAdmin(admin.ModelAdmin):
    # Default implementation (no changes) like 'name','title','bio'
#     list_display = ('name','title','bio',) # Must be a list end with ,
    list_display = ('name', 'bio',)
    
    # Controlling admin from fields
    fieldsets = (
        ("General Information",{        # Provide section name 
            "fields": ("name", "bio")   # List fields to display
        }),
        ("Social Media", {              # Provide section name
            "classes": ("collapse"),    # Hidden by default (**make sure you have that collapse
            "fields": ("twitter", "facebook",), # List of fileds to display
            "description": "Add social media here"  # Add a description 
        })
    )

admin.site.register(Speaker, SpeakerAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker',)
    # Enabling search option
    # When we have a lot of items, it can be a challenge 
    # to find the ones what we want
    search_fields = ['title', 'abstract']
    # Enabling filtering
    # If we have natural groups of objects, we can enable filtering
    list_filter = ('track__title', 'speaker',)

admin.site.register(Session, SessionAdmin)
