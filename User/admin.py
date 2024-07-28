from django.contrib import admin

from .models import User, SimpleUser, History, HiddenHistory, PDFHistory


admin.site.register(User)

admin.site.register(SimpleUser)

admin.site.register(History)

admin.site.register(HiddenHistory)

admin.site.register(PDFHistory)
