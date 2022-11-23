from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Event, Comment

# Register your models here.
admin.site.register(Event)
admin.site.register(Comment)

class RentalAdmin(admin.ModelAdmin):
  formfield_overrides = {
      map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
  }