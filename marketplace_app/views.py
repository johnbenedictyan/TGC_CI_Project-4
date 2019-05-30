from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import ListingForm,ListingImageForm
from project4_project import settings
from .models import Listing,ListingImage

# Create your views here.
def marketplace(request):
    return render(request,"marketplace.html")
    
def favourites(request):
    return render(request,"favourites.html")
    
def listingcreator(request):
    image_form_set = modelformset_factory(ListingImage,form=ListingImageForm, extra=4)
    if request.method=="GET":
        listing_creator_form = ListingForm()
        image_form = image_form_set(queryset=ListingImage.objects.none())
        return render(request,"listing-creator.html",{
            "listing_creator_form":listing_creator_form,
            "image_form":image_form
        })
    else:
        dirty_listing_creator_form = ListingForm(request.POST)
        dirty_image_form = image_form_set(request.POST, request.FILES,queryset=ListingImage.objects.none())
        if dirty_listing_creator_form.is_valid() and dirty_image_form.is_valid():
            dirty_listing_creator_form.save()
            for form in dirty_image_form:
                if form:
                    image = form["image"]
                    listing_image = ListingImage(image=image,listing=dirty_listing_creator_form)
                    listing_image.save()
                    
            messages.success(request, "The listing has been successfully created!")
            return redirect("home_page_link")
        else:
            messages.error(request,"We are unable to create this listing!")
            return render(request,"listing.html",{
                "listing_creator_form":dirty_listing_creator_form,
                "image_form":dirty_image_form
            }) 
        
    
def listingeditor(request,listing_id):
    if request.method=="GET":
        listing_from_db = get_object_or_404(Listing,id=listing_id)
        listing_editor_form = ListingForm(instance=listing_from_db)
        return render(request,"listing-editor.html",{
            "listing_editor_form":listing_editor_form
        })
    else:
        dirty_listing_editor_form = ListingForm(request.POST)
        if dirty_listing_editor_form.is_valid():
            dirty_listing_editor_form.save()
            messages.success(request, "The listing has been successfully updated!")
            return redirect("home_page_link")
        else:
            return render(request,"listing-editor.html",{
            "listing_editor_form":dirty_listing_editor_form
        })