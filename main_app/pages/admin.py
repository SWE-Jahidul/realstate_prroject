from django.contrib import admin

# Register your models here.

from .models import contract_details,top_house_details,agent_details,defualt_detials,index_house_details,index_defoult_change,why_we_choose_details,ledership_details,blog_post_create
from .models import about_page_defaut

admin.site.register(contract_details),
admin.site.register(top_house_details),
admin.site.register(agent_details),
admin.site.register(defualt_detials),
admin.site.register(index_house_details),
admin.site.register(index_defoult_change),
admin.site.register(why_we_choose_details),
admin.site.register(ledership_details),
admin.site.register(blog_post_create),
admin.site.register(about_page_defaut)
