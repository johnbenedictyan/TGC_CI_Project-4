from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import ListingForm
from project4_project import settings
from .models import Listing
from django.contrib.auth.decorators import login_required

# Create your views here.
def marketplace(request):
    return render(request,"marketplace.html")

@login_required    
def favourites(request):
    return render(request,"favourites.html")

@login_required    
def listingcreator(request):
    if request.method=="GET":
        listing_creator_form = ListingForm()
        return render(request,"listing-creator.html",{
            "listing_creator_form":listing_creator_form,
        })
    else:
        dirty_listing_creator_form = ListingForm(request.POST)
        if dirty_listing_creator_form.is_valid():
            dirty_listing_creator_form.save()
            messages.success(request, "The listing has been successfully created!")
            return redirect("home_page_link")
        else:
            messages.error(request,"We are unable to create this listing!")
            return render(request,"listing.html",{
                "listing_creator_form":dirty_listing_creator_form,
            }) 
        
@login_required    
def listingeditor(request,listing_id):
    if request.method=="GET":
        listing_from_db = get_object_or_404(Listing,pk=listing_id)
        if listing_from_db.seller.id == request.user.id:
            listing_editor_form = ListingForm(instance=listing_from_db)
            return render(request,"listing-editor.html",{
                "listing_editor_form":listing_editor_form
            })
        else:
            messages.error(request,"You are not the seller of this listing!")
            return redirect("marketplace_link")
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