# Smooth Selling
As the saying goes, "One man's trash in another man's treasure", find treasure in the treasure trove that is Smooth Selling today.
## UX
List of User Stories
- As a hoarder, I want to publish a listing, so that I can get rid of things I do not need.
- As someone who wants to buy a skateboard, I want to search for skateboard listings, so that I can find the one that suits me.
- As someone who needs more money, I want to publish listings, so that I can get more money.


## Features
### Existing Features
- listing Creation - Allows users to create their own listings, by having them fill up a listing creation form.
- listing Updating - Allows users to update their own listings, by having them fill up a listing update form.
- listing Deletion - Allows users to delete their own listings, with checks in place if they try to delete a listing they did not create.
- Searching for listings - Allows users to search for listings, by having them type in a search bar.
- User Creation - Allows users to create user accounts, by having them fill up a user creation form.
- User Account Details Updating - Allows users to update their user details, by having them fill up a user details updating form.
- User Deletion - Allows users to create their own listings, by having them fill up a listing creation form.
- View Counter - Allows the number of views on each listing to increase whenever a user clicks on that listing
- User & listing Photo Upload - Allows the user to upload photos for their listings as well as their profiles, by storing the photos on uploadcare.

### Features Left to Implement
- Comments Section: Where users can leave comments on each of the listings as well as other's users' comments.
- Review Section: Community driven review section, based of 5 stars, with the inclusion of certified reviewers whose reviews will be highlighted

## Technologies Used
- [Boostrap](https://getbootstrap.com/)
    - The project uses **Boostrap** to create a mobile responsive and stylish webpage.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** as it's main framework.
- [Pillow](https://pypi.org/project/Pillow/)
    - The project uses **Pillow** to allow for the uploading of photos to AWS S3.
- [coverage](https://coverage.readthedocs.io/en/v4.5.x/)
    - The project uses **coverage** to allow for test coverages to be generated.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - The project uses **boto3** to allow for the uploading of photos to AWS S3.
- [botocore](https://pypi.org/project/botocore/)
    - The project uses **botocore** to allow for the uploading of photos to AWS S3.
- [dj-database-url](https://pypi.org/project/dj-database-url/)
    - The project uses **dj-database-url** to allow django to communicate with Heroku's Postgresql.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - The project uses **django-crispy-forms** to allow for forms to be render in a bootstrap template.
- [gunicorn](https://gunicorn.org/)
    - The project uses **gunicorn** as a python WSGI HTTP server to deploy the app on Heroku.
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
    - The project uses **django-storages** to allow for the uploading of photos to AWS S3.
- [docutils](https://pypi.org/project/docutils/)
    - The project uses **docutils** to process documentation into useful formats, such as HTML, XML, and LaTeX. 
- [python-dateutil](https://pypi.org/project/python-dateutil/)
    - The project uses **python-dateutil** to allow python to get the current date.
- [urllib3](https://urllib3.readthedocs.io/en/latest/)
    - The project uses **urllib3** as a HTTP client.
- [jmespath](http://jmespath.org/)
    - The project uses **jmespath** as a query language for JSON.
- [psycopg2](https://pypi.org/project/psycopg2/)
    - The project uses **psycopg2** to allow django to communicate with Heroku's Postgresql.
- [pytz](https://pypi.org/project/pytz/)
    - The project uses **pytz** to allow for more accurate and cross platform timezone calculations.
- [whitenoise](http://whitenoise.evans.io/en/stable/)
    - The project uses **whitenoise** to allow static files to be served from AWS s3.
- [Stripe](https://stripe.com/)
    - The project uses **Stripe** to process credit card payment.
- [Axios](https://github.com/axios/axios/)
    - The project uses **Stripe** to simplify AJAX calls.
- [pyuploadcare](https://github.com/uploadcare/pyuploadcare/)
    - The project uses **pyuploadcare** to integrate django and UploadCare to upload photos.
- [uploadcare](https://uploadcare.com/)
    - The project uses **uploadcare** to upload and serve images.

## Testing
Manual Testing:

Automated Testings:
- There is automated testing for:
1. User authetication and pages which requires the user to be logged in.
2. The website pages can load correctly.
3. Listing Categories can be created,updated and deleted.
4. Listings can be created,updated and deleted.
5. Listing Comments can be created,updated,deleted and whether there can be multiple.
6. Listing Likes can be created,updated,deleted and whether there can be multiple.
7. User Accounts can be created,updated and deleted.
8. User Groups can be created,updated and deleted.

Interesting Bugs/Problems:

## Deployment
On the development version, sensitive information is stored in an env.py that is not pushed to github.
Where as on the deployed version, these sensitive information are stored in the Heroku Config Vars

To run the app locally:
1. Open the terminal.
2. Run this command.
```sh
$ python manage.py runserver <INSERT_YOUR_OWN_SERVER_IP>:<INSERT_YOUR_OWN_SERVER_PORT>
```
3. Click on the local host link address to open the app the web browser.

You can view the deployed version on [Heroku](https://tgc-ci-project-4.herokuapp.com/)
## Credits

### Content

### Media
- The photos used in this site were obtained from [Stock Snap](https://stocksnap.io/),[Pexels](https://www.pexels.com/),[Unsplash](https://unsplash.com/),[Pixabay](https://pixabay.com/)

### Acknowledgements

- The Boostrap Template was taken from [ColorLib](https://colorlib.com/wp/templates/)

