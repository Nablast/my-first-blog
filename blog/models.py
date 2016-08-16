from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
		
class UserGroup(models.Model):
    name = models.CharField(u'Nom', max_length=255)
	
    def __str__(self):
        return self.name
		
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userGroups = models.ManyToManyField(UserGroup, blank = True, related_name='users')
	
    def __str__(self):
        return self.user.username

class ShopList(models.Model):
	name = models.CharField(u'Nom', max_length=255)
	isDone = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=timezone.now)
	lastmaj_date = models.DateTimeField(default=timezone.now)
	userGroup = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='shopLists')
	
	def __str__(self):
		return self.name
	
class Object(models.Model):
    name = models.CharField(u'Nom', max_length=255)
    image = models.ImageField(blank = True)
	
    def __str__(self):
        return self.name
	
class Item(models.Model):
    object = models.ForeignKey(Object, related_name='items')
    quantity = models.IntegerField(u'Quantite', blank=True, default=1)
    shopList = models.ForeignKey(ShopList, related_name='items')
    isDone = models.BooleanField(default=False)
	
    def __str__(self):
        return self.object.name + ' (' + str(self.quantity) + ')'