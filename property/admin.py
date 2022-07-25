from django.contrib import admin

from .models import Flat, Appeal


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
    raw_id_fields = ("flat", "who_appeal")

admin.site.register(Flat, FlatAdmin)
admin.site.register(Appeal, AppealAdmin)
