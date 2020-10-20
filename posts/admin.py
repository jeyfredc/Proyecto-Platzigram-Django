""" User admin classes. """
#Django
from django.contrib import admin
#Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post admin. """

    list_display = ('pk','user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo',)
    search_fields = ('user__name',)
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields' : (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields' : (
                ('created', 'modified'),
            )
        }),
    )

    readonly_fields = ('created', 'modified')
