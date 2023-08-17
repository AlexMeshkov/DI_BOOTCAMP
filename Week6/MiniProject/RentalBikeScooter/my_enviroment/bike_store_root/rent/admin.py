from django.contrib import admin
from .models import Customer
from .models import Vehicle
from .models import VehicleType
from .models import VehicleSize
from .models import Rental
from .models import RentalRate
from .models import RentalStation
from .models import Address
from .models import VehicleAtRentalStation

# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(RentalStation)
admin.site.register(Address)
admin.site.register(VehicleAtRentalStation)
