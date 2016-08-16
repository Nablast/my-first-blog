from django import forms
from django.contrib import admin

from .models import UserGroup, CustomUser, ShopList, Item, Object

class UserGroupForm(forms.ModelForm):

	class Meta:
		model = UserGroup
		users = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all())
		fields = ('name','users')

	users = forms.ModelMultipleChoiceField(
		CustomUser.objects.all(),
		required = False,
	)
	
	def __init__(self, *args, **kwargs):
		super(UserGroupForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.initial['users'] = self.instance.users.values_list('pk', flat = True)
			
	def save(self, *args, **kwargs):
		instance = super(UserGroupForm,self).save(*args, **kwargs)
		if instance.pk:
			for user in instance.users.all():
				if user not in self.cleaned_data['users']:
					#remove users which have been unselected
					instance.users.remove(user)
			for user in self.cleaned_data['users']:
				if user not in instance.users.all():
					#We add newly selected users
					instance.users.add(user)
		return instance
		
class ShopListForm(forms.ModelForm):

	class Meta:
		model = ShopList
		fields = ('name',)

	#items = forms.ModelMultipleChoiceField(Item.objects.all(), required = False,)