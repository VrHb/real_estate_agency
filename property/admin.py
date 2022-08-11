from django.contrib import admin

from .models import Flat, Appeal, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = (
        "address", "price", "new_building", "construction_year", "town",
        "owners_phonenumber", "owner_pure_number"
    )
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ("likes",)

class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "who_appeal",)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Appeal, AppealAdmin)
admin.site.register(Owner, OwnerAdmin)
