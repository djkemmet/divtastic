from django.contrib import admin
from research import models
# Register your models here.
admin.site.register(models.symbol_lookup_model)
admin.site.register(models.user_profile_ideas)
admin.site.register(models.investment_type)