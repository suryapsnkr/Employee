
from django.contrib import admin
from shree.models import Contact, Employee, Leave, Review
# Add this it change the header of the admin panel.
admin.site.site_header = 'LakshmiShree Administration'
# Add this it change the title of the admin panel.
admin.site.site_title = 'LakshmiShree Site Admin'

# Register your models here.
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Review)
admin.site.register(Contact)

