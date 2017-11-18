# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import myUser,Tutor,Student,Wallet,Transaction,Booking,Tag,Course

admin.site.register(myUser)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Booking)
admin.site.register(Tag)
admin.site.register(Course)

