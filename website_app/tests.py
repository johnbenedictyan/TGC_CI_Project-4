from django.test import TestCase,Client
from user_accounts_app.models import UserAccount
# Create your tests here.
class WebsiteTest(TestCase):
    def testCanLoadMainPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def testCanLoadMarketPlacePage(self):
        response = self.client.get('/marketplace/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace.html')
    
    def testCanLoadLoginPage(self):
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def testCanLoadRegisterPage(self):
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        
    def testCannotLoadNonExistentPage(self):
        response = self.client.get('/flyingpenguin')
        self.assertEqual(response.status_code, 404)
    
    def testCannotAccessLoginRequiredPagesAnonymously(self):
        response = self.client.get('/account/account_details/', follow=True)
        self.assertRedirects(response, '/account/login/?next=/account/account_details/')
        self.assertTemplateUsed(response, 'login.html')
        
    def testCanAccessLoginRequiredPagesWhenLoggedIn(self):
        user = UserAccount.objects.create(username='testuser')
        user.set_password('password12345')
        user.save()
        self.client.login(username="testuser",password="password12345")
        response = self.client.get('/account/account_details/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_details.html')
        