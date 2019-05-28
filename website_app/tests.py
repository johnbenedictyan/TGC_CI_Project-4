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
        
        
class UserAuthenticationTest(TestCase):
    def testCanRegisterAccount(self):
        response = self.client.post('/account/register/', {
            'username':'testuser',
            'first_name':'test',
            'last_name':'user',
            'email':'testuser@testing.com',
            'password1':'password123123',
            'password2':'password123123'
        }) 
        self.assertRedirects(response, '/account/login/')
    
    def testCannotRegisterAccount_UsernameTaken(self):
        user = UserAccount.objects.create(username='testuser')
        user.set_password('password12345')
        user.save()
        response = self.client.post('/account/register/', {
            'username':'testuser',
            'first_name':'test',
            'last_name':'user',
            'email':'testuser@testing.com',
            'password1':'password123123',
            'password2':'password123123'
        }) 
        self.assertFormError(response, 'registerform', 'username', 'This username is already taken.')
    
    def testCannotRegisterAccount_PasswordMismatch(self):
        response = self.client.post('/account/register/', {
            'username':'testuser',
            'first_name':'test',
            'last_name':'user',
            'email':'testuser@testing.com',
            'password1':'password123123',
            'password2':'password123'
        }) 
        self.assertFormError(response, 'registerform', 'password2', 'The two password fields didn\'t match.')
    
    def testCannotRegisterAccount_MissingData(self):
        response = self.client.post('/account/register/', {}) 
        self.assertFormError(response, 'registerform', 'username', 'This field is required.')
        self.assertFormError(response, 'registerform', 'first_name', 'This field is required.')
        self.assertFormError(response, 'registerform', 'last_name', 'This field is required.')
        self.assertFormError(response, 'registerform', 'email', 'This field is required.')
        self.assertFormError(response, 'registerform', 'password1', 'This field is required.')
        self.assertFormError(response, 'registerform', 'password2', 'This field is required.')
    
    def testCanLogin(self):
        user = UserAccount.objects.create(username='testuser')
        user.set_password('password12345')
        user.save()
        response = self.client.post('/account/login/', {
            'username':'testuser',
            'password':'password12345'
        }) 
        self.assertRedirects(response, '/')
    
    def testCannotLogin_UserDoesNotExist(self):
        response = self.client.post('/account/login/', {
            'username':'ghostuser',
            'password':'password12345'
        }) 
        self.assertFormError(response, 'loginform', 'username', 'This user does not exist.')
    
    def testCannotLogin_IncorrectPassword(self):
        user = UserAccount.objects.create(username='testuser')
        user.set_password('password12345')
        user.save()
        response = self.client.post('/account/login/', {
            'username':'testuser',
            'password':'wrongpassword'
        }) 
        self.assertFormError(response, 'loginform', 'password', 'Incorrect Password.')
        
    def testCannotLogin_MissingData(self):
        response = self.client.post('/account/login/', {}) 
        self.assertFormError(response, 'loginform', 'username', 'This field is required.')
        self.assertFormError(response, 'loginform', 'password', 'This field is required.')
    