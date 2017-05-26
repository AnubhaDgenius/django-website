from django.contrib import admin

from gallery.models import Notice, Owner,Ques

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'cr_date')
    list_filter = ['cr_date']
    search_fields = ['subject', 'message']
admin.site.register(Notice, NoticeAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','name_pet','type','breed')
    list_filter = ['type', 'breed']
    search_fields = ['breed']
admin.site.register(Owner, UserAdmin)

class QuesAdmin(admin.ModelAdmin):
    list_display = ('question',)
    list_filter = ['user', 'notice']
    search_fields = ['question', 'answer']
admin.site.register(Ques, QuesAdmin)

