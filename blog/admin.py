from django.contrib import admin
from .models import UserGroup, CustomUser, ShopList, Item, Object
from .forms import UserGroupForm

# admin.site.unregister(User)

class UserGroupAdmin(admin.ModelAdmin):

	form = UserGroupForm
	
	fieldsets = (
		(None, {'fields':('name','users')}),
	)

admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(CustomUser)
admin.site.register(ShopList)
admin.site.register(Item)
admin.site.register(Object)
