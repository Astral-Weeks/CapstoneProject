from django.test import TestCase
from restaurant.models import Menu

# ///////////////////////////////////////////////////////////////
# Tests on the Menu API

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Strawberry Ice Cream", Price=8.0, Inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, 'Title: Strawberry Ice Cream  Price: 8.0  Inventory: 100')
    
    def test_delete_item(self):
        item_to_delete = Menu.objects.filter(Title="Strawberry Ice Cream")
        item_to_delete.delete()
        self.assertEqual(Menu.objects.count(), 0)
    
class MenuItemTest2(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Tomato Soup", Price=7.75, Inventory=25)
        itemstr = item.get_item()
        self.assertEqual(itemstr, 'Title: Tomato Soup  Price: 7.75  Inventory: 25')

class MenuTest3(TestCase):        
    def test_change_price(self):
        item_to_change = Menu.objects.create(Title="T-Bone Steak", Price=12.00, Inventory=20)
        item_to_change.Price = 13.50
        item_to_change.save()
        UpdatedTBoneSteak = item_to_change.get_item()
        self.assertEqual(UpdatedTBoneSteak, 'Title: T-Bone Steak  Price: 13.5  Inventory: 20')
