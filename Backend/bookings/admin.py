from django.contrib import admin

from .models import Booking, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "phone",
        "opening_time",
        "closing_time",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "location", "phone")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "restaurant",
        "booking_date",
        "booking_time",
        "guests",
        "created_at",
    )
    list_filter = ("booking_date", "restaurant")
    search_fields = (
        "customer_name",
        "customer_email",
        "customer_phone",
    )
