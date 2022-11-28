from django.contrib import admin
from .models import Event, Comment


# Register your models here.
admin.site.register(Event)
admin.site.register(Comment)

class RentalAdmin(admin.ModelAdmin):
  formfield_overrides = {
      map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
  }