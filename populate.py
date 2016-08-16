import os

def populate():

    # User 
    uMarion = add_User('Marion')
    uArthur = add_User('Arthur')
    uLucien = add_User('Lucien')

    # UserGroup
    colloc = add_UserGroup(a_name='colloc')
    
    # CustomUser
    cuMarion = add_CustomUser(a_user=uMarion)
    cuArthur = add_CustomUser(a_user=uArthur)
    cuLucien = add_CustomUser(a_user=uLucien)
    
    # Add User to Group
    add_To_Group(a_user=cuMarion, a_group=colloc)
    add_To_Group(a_user=cuArthur, a_group=colloc)
    add_To_Group(a_user=cuLucien, a_group=colloc)
    
    # List
    list1 = add_List(a_name='list1', a_group=colloc)
    list2 = add_List(a_name='list2', a_group=colloc)
    
    # Object
    bananeObject = add_Object(a_name='banane')
    melonObject = add_Object(a_name='melon')
    
    # Item
    bananeList1 = add_Item(a_object=bananeObject, a_quantity=2, a_shopList=list1)
    melonList1 = add_Item(a_object=melonObject, a_quantity=3, a_shopList=list1)
	
    for group in UserGroup.objects.all():
        print("--- Group : " + str(group))
        for shoplist in ShopList.objects.filter(userGroup=group):
            print("        " + str(shoplist))
            for item in Item.objects.filter(shopList=shoplist):
                print("                " + str(item))
    
def add_User(a_name):
    user = User.objects.get_or_create(username=a_name)[0]
    return user
    
def add_UserGroup(a_name):
    group = UserGroup.objects.get_or_create(name=a_name)[0]
    return group
    
def add_CustomUser(a_user):
    customUser = CustomUser.objects.get_or_create(user=a_user)[0]
    return customUser
    
def add_To_Group(a_user, a_group):
    a_group.users.add(a_user)
    
def add_List(a_name, a_group):
    list = ShopList.objects.get_or_create(name=a_name, userGroup=a_group)[0]
    return list
    
def add_Object(a_name):
    object = Object.objects.get_or_create(name=a_name)[0]
    return object
    
def add_Item(a_object, a_quantity, a_shopList):
    item = Item.objects.get_or_create(object=a_object, quantity=a_quantity, shopList=a_shopList)[0]
    return item

# Start execution here!
if __name__ == '__main__':
    print("Starting ShopList population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    import django
    django.setup()
    from django.contrib.auth.models import User
    from blog.models import CustomUser, UserGroup, Object, Item, ShopList
    populate()