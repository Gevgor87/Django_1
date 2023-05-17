from django.contrib import admin
from .models import Category, Base, Button_1, Button_2, Button_3, Button_4, Footer, Contack
# Register your models here.


admin.site.register(Category)
admin.site.register(Base)
admin.site.register(Button_1)
admin.site.register(Button_2)
admin.site.register(Button_3)
admin.site.register(Button_4)
admin.site.register(Footer)

@admin.register(Contack)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    list_display_links = ["name", "email"]
    search_fields = ["name", "email"]




