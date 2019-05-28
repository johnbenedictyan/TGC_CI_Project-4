from django.test import TestCase
from .models import UserAccount,Group
# Create your tests here.
# Test Cases needed:
# 1. A person can create a user
# 2. The system should check if the username exist
# 3. A person can update a user's details
# 4. A person can delete a user

class UserAccountTest(TestCase):
    def testCanCreateAccount(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider",bio="Hi im a penguinrider")
        ta.save()
        
        ta_from_db = UserAccount.objects.all().get(pk=ta.id)
        self.assertEquals(ta.username,ta_from_db.username)
        self.assertEquals(ta.password,ta_from_db.password)
        self.assertEquals(ta.email,ta_from_db.email)
        self.assertEquals(ta.first_name,ta_from_db.first_name)
        self.assertEquals(ta.last_name,ta_from_db.last_name)
        self.assertEquals(ta.bio,ta_from_db.bio)
        
    def testCanUpdateAccountDetails(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta.username="penguinrider123"
        ta.password="password12345"
        ta.email="qwe@qwe.com"
        ta.save()
        
        ta_from_db = UserAccount.objects.all().get(pk=ta.id)
        self.assertEquals(ta_from_db.username,"penguinrider123")
        self.assertEquals(ta_from_db.password,"password12345")
        self.assertEquals(ta_from_db.email,"qwe@qwe.com")
        
    def testCanDeleteAccount(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        UserAccount.objects.filter(id=ta.id).delete()
        ta_from_db=list(UserAccount.objects.all().filter(pk=ta.id))
        self.assertEquals(ta_from_db,[])
        
class GroupTest(TestCase):
    def testCanCreateGroup(self):
        tg = Group(name="",description="")
        tg.save()
        
        tg_from_db = Group.objects.all().get(pk=tg.id)
        self.assertEquals(tg_from_db.name,tg.name)
        self.assertEquals(tg_from_db.description,tg.description)
        
    def testGroupsCanHaveManyMembers(self):
        tg = Group(name="Guitar Club",description="For all things guitar related")
        tg.save()
        
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com")
        ta2.save()
        
        tg.members.add(ta,ta2)
        
        tg_from_db = Group.objects.all().get(pk=tg.id)
        self.assertEquals(tg_from_db.name,tg.name)
        self.assertEquals(tg_from_db.description,tg.description)
        self.assertEquals(tg_from_db.members.count(),2)
        self.assertEquals(tg_from_db.members.all()[0].username,ta.username)
        self.assertEquals(tg_from_db.members.all()[1].username,ta2.username)
        
    def testCanUpdateGroupDetails(self):
        tg = Group(name="Guitar Club",description="For all things guitar related")
        tg.save()
        
        tg.name="Golf Club"
        tg.description="Hit the small ball really hard"
        tg.save()
        
        tg_from_db = Group.objects.all().get(pk=tg.id)
        self.assertEquals(tg_from_db.name,"Golf Club")
        self.assertEquals(tg_from_db.description,"Hit the small ball really hard")
        
    def testCanRemoveGroupMembers(self):
        tg = Group(name="Guitar Club",description="For all things guitar related")
        tg.save()
        
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com")
        ta2.save()
        
        tg.members.add(ta,ta2)
        tg.members.remove(ta2)
        
        tg_from_db = Group.objects.all().get(pk=tg.id)
        self.assertEquals(tg_from_db.name,tg.name)
        self.assertEquals(tg_from_db.description,tg.description)
        self.assertEquals(tg_from_db.members.count(),1)
        self.assertEquals(tg_from_db.members.all()[0].username,ta.username)
        
    def testCanDeleteGroup(self):
        tg = Group(name="Guitar Club",description="For all things guitar related")
        tg.save()
        
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com")
        ta2.save()
        
        tg.members.add(ta,ta2)
        
        Group.objects.filter(id=tg.id).delete()
        tg_from_db = list(Group.objects.all().filter(pk=tg.id))
        self.assertEquals(tg_from_db,[])