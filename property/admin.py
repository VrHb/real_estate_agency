from django.contrib import admin

from .models import Flat, Appeal, Owner

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = (
        "address", "price", "new_building", "construction_year", "town"
    )
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ("likes",)

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "who_appeal",)



class FlatsInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = [
        "flat",
        "owner"
    ]

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    inlines = [FlatsInline]

