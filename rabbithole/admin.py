from django.contrib import admin
from .models import channel
from .models import cat_submissions
from .models import sub_cat_submissions
	
admin.site.register(channel)
admin.site.register(cat_submissions)
admin.site.register(sub_cat_submissions)

