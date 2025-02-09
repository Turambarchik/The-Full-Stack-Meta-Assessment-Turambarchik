from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import BookingForm
from .models import Menu, Booking
from datetime import datetime
import json

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def reservations(request):
    date_param = request.GET.get("date")
    if date_param:
        bookings = Booking.objects.filter(reservation_date=date_param)  # Filter bookings by the specified date
    else:
        bookings = Booking.objects.all()  # If no date is provided, return all bookings (My improvement)

    booking_list = list(bookings.values("first_name", "reservation_date", "reservation_slot"))

    return JsonResponse({"bookings": booking_list}, safe=False)



def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "book.html", {"form": form})

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, "menu.html", {"menu": menu_data})

def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk) if pk else None
    return render(request, "menu_item.html", {"menu_item": menu_item})

@csrf_exempt
def bookings(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        exist = Booking.objects.filter(
            reservation_date=data["reservation_date"],
            reservation_slot=data["reservation_slot"]
        ).exists()

        if exist:
            return JsonResponse({"error": "This slot is already booked."}, status=400)

        booking = Booking(
            first_name=data["first_name"],
            reservation_date=data["reservation_date"],
            reservation_slot=data["reservation_slot"],
        )
        booking.save()

        return JsonResponse({"message": "Booking successful."}, status=201)

    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = json.loads(serializers.serialize("json", bookings))

    return JsonResponse({"bookings": booking_json}, safe=False)
