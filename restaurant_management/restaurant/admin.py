from django.contrib import admin
from restaurant.models import TableBooking,MenuItem, InventoryItem, Table, Order, OrderItem,Employee,Role,Department

admin.site.register(TableBooking)
admin.site.register(MenuItem)
admin.site.register(InventoryItem)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
