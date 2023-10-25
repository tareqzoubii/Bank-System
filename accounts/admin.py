from django.contrib import admin
from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin
# from .serializers import CreateUserSerializer
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CreateUserSerializer
#     add_fieldsets = (
#         ('None', {'fields' : ('username','email','password1', 'password2')}),
#         ('Personal Information', {'fields' : ('first_name','last_name','id_number','phone_number','account_number', 'ammount', 'role')})
#     )

admin.site.register(CustomUser)