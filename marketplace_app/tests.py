from django.test import TestCase
from .models import ListingCategory, Listing, ListingComment, ListingImage
from user_accounts_app.models import UserAccount

# Create your tests here.
# Test Cases needed:
# 1. A person can create a listing DONE
# 2. A person can update a listing's details
# 3. A person can delete a listing

class ListingCategoryTest(TestCase):
    def testCanCreateListingCategory(self):
        LC = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        LC.save()
        
        LC2 = ListingCategory.objects.all().get(pk=LC.id)
        self.assertEquals(LC.name,LC2.name)
        self.assertEquals(LC.description,LC2.description)
        
    def testCanUpdateListingCategory(self):
        LC = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        LC.save()
        
        LC.name="fashion"
        LC.description="Fashion is a popular style, especially in clothing, footwear, lifestyle, accessories, makeup, hairstyle and body. Fashion is a distinctive and often constant trend in the style in which people present themselves."
        LC.save()
        
        
        lc_from_db = ListingCategory.objects.all().get(pk=LC.id)
        self.assertEquals(lc_from_db.name,"fashion")
        self.assertEquals(lc_from_db.description,"Fashion is a popular style, especially in clothing, footwear, lifestyle, accessories, makeup, hairstyle and body. Fashion is a distinctive and often constant trend in the style in which people present themselves.")
        
    def testCanDeleteListingCategory(self):
        LC = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        LC.save()
        
        LC2 = ListingCategory.objects.all().get(pk=LC.id)
        self.assertEquals(LC.name,LC2.name)
        self.assertEquals(LC.description,LC2.description)
        
        ListingCategory.objects.filter(id=LC.id).delete()
        lc_from_db = list(ListingCategory.objects.all().filter(pk=LC.id))
        self.assertEquals(lc_from_db,[])
        
class ListingTest(TestCase):
    def testCanCreateListing(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        test_listing.categories.add(test_lc_1)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(test_listing.name,tl_from_db.name)
        self.assertEquals(test_listing.description,tl_from_db.description)
        self.assertEquals(test_listing.price,tl_from_db.price)
        self.assertEquals(test_listing.location,tl_from_db.location)
        self.assertEquals(test_listing.used,tl_from_db.used)
        self.assertEquals(tl_from_db.categories.count(),1)
        self.assertEquals(tl_from_db.categories.all()[0].name,"furniture")
        self.assertEquals(tl_from_db.seller.username,ta.username)
        self.assertEquals(tl_from_db.seller.password,ta.password)
        self.assertEquals(tl_from_db.seller.email,ta.email)
        
    def testListingCanHaveManyCategories(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        
        test_lc_2 = ListingCategory(name="rustic",description="""
        simple and often rough in appearance; typical of the countryside """)
        
        test_lc_2.save()
        
        test_listing.categories.add(test_lc_1,test_lc_2)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(tl_from_db.categories.count(),2)
        self.assertEquals(tl_from_db.categories.all()[0].name,"furniture")
        self.assertEquals(tl_from_db.categories.all()[1].name,"rustic")
        
    def testCanDeleteListing(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        test_listing.categories.add(test_lc_1)
        
        Listing.objects.filter(id=test_listing.id).delete()
        tl_from_db = list(Listing.objects.all().filter(pk=test_listing.id))
        self.assertEquals(tl_from_db,[])
    
    def testCanUpdateListingDetails(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",seller=ta)
        test_listing.save()
        
        test_listing.name="Stool"
        test_listing.description="Not so rustic stool"
        test_listing.price=14.99
        test_listing.location="Yishun Avenue 2"
        test_listing.save()
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        self.assertEquals(tl_from_db.name,"Stool")
        self.assertEquals(tl_from_db.description,"Not so rustic stool")
        self.assertEquals(tl_from_db.price,14.99)
        self.assertEquals(tl_from_db.location,"Yishun Avenue 2")
    
    def testCanRemoveCategory(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        
        test_lc_2 = ListingCategory(name="rustic",description="""
        simple and often rough in appearance; typical of the countryside """)
        
        test_lc_2.save()
        
        test_listing.categories.add(test_lc_1,test_lc_2)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(tl_from_db.categories,test_listing.categories)
        
        test_listing.categories.remove(test_lc_1)
        new_tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(new_tl_from_db.categories.count(),1)
        self.assertEquals(new_tl_from_db.categories.all()[0].name,"rustic")
        
class ListingCommentTest(TestCase):
    def testCanCreateComent(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        test_listing.categories.add(test_lc_1)
        test_listing.likes.add(ta)
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        tc_from_db = ListingComment.objects.all().get(pk=tc.id)
        self.assertEquals(tc_from_db.comment,tc.comment)
        self.assertEquals(tc_from_db.user,ta2)
        self.assertEquals(tc_from_db.listing,test_listing)
    
    def testCanUpdateComment(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        test_listing.categories.add(test_lc_1)
        test_listing.likes.add(ta)
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        tc.comment="I have received a new product and now it is not wonky"
        tc.save()
        
        tc_from_db = ListingComment.objects.all().get(pk=tc.id)
        
        self.assertEquals(tc_from_db.comment,"I have received a new product and now it is not wonky")
        
    def testCanDeleteComment(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_lc_1 = ListingCategory(name="furniture",description="""
        Furniture refers to movable objects intended to support various human activities such as seating 
        (e.g., chairs, stools, and sofas), eating (tables), and sleeping (e.g., beds). """)
        
        test_lc_1.save()
        test_listing.categories.add(test_lc_1)
        test_listing.likes.add(ta)
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        ListingComment.objects.filter(id=tc.id).delete()
        
        tc_from_db = list(ListingComment.objects.all().filter(pk=tc.id))
        
        self.assertEquals(tc_from_db,[])
        
    def testPostCanHaveMultipleCommentsFromTheSamePerson(self):
        #Multiple Comments From the Same Person
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        tc2 = ListingComment(comment="This product looks alright",user=ta2,listing=test_listing)
        tc2.save()
        
        self.assertEquals(ListingComment.objects.all().count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2).count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2)[0].listing,test_listing)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2)[1].listing,test_listing)
        
    def testPostCanHaveMultipleCommentsFromDifferentPeople(self):
        #Multiple Comments From Different People
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        ta3 = UserAccount(username="girafferider",password="qwerty",email="qazwsx@qaz.com",first_name="giraffe",last_name="rider")
        ta3.save()
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        tc2 = ListingComment(comment="I love waffles",user=ta3,listing=test_listing)
        tc2.save()
        
        self.assertEquals(ListingComment.objects.all().filter(user=ta2).count(),1)
        self.assertEquals(ListingComment.objects.all().filter(user=ta3).count(),1)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2)[0].listing,test_listing)
        self.assertEquals(ListingComment.objects.all().filter(user=ta3)[0].listing,test_listing)
        
    def testUsersCanHaveMultipleCommentsOnDifferentListingsFromTheSameSeller(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing2 = Listing(name="Stool",description="Rustic stuhl, not so very rustic.",price=43.99,location="Yishun Avenue 1",used=True,seller=ta)
        test_listing2.save()
        
        tc = ListingComment(comment="This product looks wonky",user=ta2,listing=test_listing)
        tc.save()
        
        tc2 = ListingComment(comment="This product looks alright",user=ta2,listing=test_listing2)
        tc2.save()
        
        self.assertEquals(ListingComment.objects.all().count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2).count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2)[0].listing,test_listing)
        self.assertEquals(ListingComment.objects.all().filter(user=ta2)[1].listing,test_listing2)
        
    def testUsersCanHaveMultipleCommentsOnDifferentListingsFromDifferentSellers(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        ta3 = UserAccount(username="girafferider",password="qwerty",email="qazwsx@qaz.com",first_name="giraffe",last_name="rider")
        ta3.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing2 = Listing(name="Stool",description="Rustic stuhl, not so very rustic.",price=43.99,location="Yishun Avenue 1",used=True,seller=ta2)
        test_listing2.save()
        
        tc = ListingComment(comment="This product looks wonky",user=ta3,listing=test_listing)
        tc.save()
        
        tc2 = ListingComment(comment="This product looks alright",user=ta3,listing=test_listing2)
        tc2.save()
        
        self.assertEquals(ListingComment.objects.all().count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta3).count(),2)
        self.assertEquals(ListingComment.objects.all().filter(user=ta3)[0].listing,test_listing)
        self.assertEquals(ListingComment.objects.all().filter(user=ta3)[1].listing,test_listing2)
        
class ListingLikesTest(TestCase):
    def testListingCanBeLiked(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing.likes.add(ta2)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(tl_from_db.likes,test_listing.likes)
        self.assertEquals(tl_from_db.likes.all()[0].username,"rhinorider")
        self.assertEquals(ta2.liked_listings.count(),1)
        
    def testListingCanBeUnliked(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing.likes.add(ta2)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(tl_from_db.likes,test_listing.likes)
        self.assertEquals(ta2.liked_listings.count(),1)
        
        test_listing.likes.remove(ta2)
        
        new_tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        
        self.assertEquals(new_tl_from_db.likes.count(),0)
        self.assertEquals(ta2.liked_listings.count(),0)
    
    def testListingCanHaveManyLikes(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        ta3 = UserAccount(username="girafferider",password="qwerty",email="qazwsx@qaz.com",first_name="giraffe",last_name="rider")
        ta3.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing.likes.add(ta2)
        test_listing.likes.add(ta3)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        self.assertEquals(tl_from_db.likes,test_listing.likes)
        self.assertEquals(tl_from_db.likes.all()[0].username,"rhinorider")
        self.assertEquals(tl_from_db.likes.all()[1].username,"girafferider")
        self.assertEquals(ta2.liked_listings.count(),1)
        self.assertEquals(ta3.liked_listings.count(),1)
    
    def testUser_Can_Have_Many_Likes_On_Different_Listings_From_The_Same_Seller(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing2 = Listing(name="Stool",description="Rustic stuhl, not so very rustic.",price=43.99,location="Yishun Avenue 1",used=True,seller=ta)
        test_listing2.save()
        
        test_listing.likes.add(ta2)
        test_listing2.likes.add(ta2)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        tl2_from_db = Listing.objects.all().get(pk=test_listing2.id)
        self.assertEquals(tl_from_db.likes,test_listing.likes)
        self.assertEquals(tl2_from_db.likes,test_listing2.likes)
        self.assertEquals(tl_from_db.likes.all()[0].username,ta2.username)
        self.assertEquals(tl2_from_db.likes.all()[0].username,ta2.username)
        self.assertEquals(ta2.liked_listings.count(),2)
        
    def testUser_Can_Have_Many_Likes_On_Different_Listings_From_Different_Sellers(self):
        ta = UserAccount(username="penguinrider",password="password123",email="asd@asd.com",first_name="penguin",last_name="rider")
        ta.save()
        
        ta2 = UserAccount(username="rhinorider",password="asd123",email="qwe@qwe.com",first_name="rhino",last_name="rider")
        ta2.save()
        
        ta3 = UserAccount(username="girafferider",password="qwerty",email="qazwsx@qaz.com",first_name="giraffe",last_name="rider")
        ta3.save()
        
        test_listing = Listing(name="Bench",description="Rustic Bench, very rustic.",price=53.99,location="Bedok Avenue 1",used=True,seller=ta)
        test_listing.save()
        
        test_listing2 = Listing(name="Stool",description="Rustic stuhl, not so very rustic.",price=43.99,location="Yishun Avenue 1",used=True,seller=ta2)
        test_listing2.save()
        
        test_listing.likes.add(ta3)
        test_listing2.likes.add(ta3)
        
        tl_from_db = Listing.objects.all().get(pk=test_listing.id)
        tl2_from_db = Listing.objects.all().get(pk=test_listing2.id)
        
        self.assertEquals(tl_from_db.likes,test_listing.likes)
        self.assertEquals(tl2_from_db.likes,test_listing2.likes)
        self.assertEquals(tl_from_db.likes.all()[0].username,ta3.username)
        self.assertEquals(tl2_from_db.likes.all()[0].username,ta3.username)
        self.assertEquals(ta3.liked_listings.count(),2)

