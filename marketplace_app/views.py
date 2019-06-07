from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import ListingForm
from project4_project import settings
from .models import Listing, ListingCategory
from django.contrib.auth.decorators import login_required
from user_accounts_app.models import UserAccount
from django.db.models import Q

def search_marketplace(current_user,search_terms=None):
    if search_terms:
        selected_listings = Listing.objects.filter(Q(name__icontains=search_terms)|Q(description__icontains=search_terms)).exclude(seller=current_user)
        number_of_listings = selected_listings.count()
    else:
        selected_listings = Listing.objects.all().exclude(seller=current_user)
        number_of_listings = selected_listings.count()
    return [selected_listings,number_of_listings]
    
def sort_by_new(current_user,search_terms=None):
    if search_terms:
        selected_listings = Listing.objects.filter(Q(name__icontains=search_terms)|Q(description__icontains=search_terms)).exclude(seller=current_user).order_by('date_time_listed')
        number_of_listings = selected_listings.count()
    else:
        selected_listings = Listing.objects.all().exclude(seller=current_user).order_by('date_time_listed')
        number_of_listings = selected_listings.count()
    return [selected_listings,number_of_listings]

def sort_by_price_low_to_high(current_user,search_terms=None):
    if search_terms:
        selected_listings = Listing.objects.filter(Q(name__icontains=search_terms)|Q(description__icontains=search_terms)).exclude(seller=current_user).order_by('price')
        number_of_listings = selected_listings.count()
    else:
        selected_listings = Listing.objects.all().exclude(seller=current_user).order_by('price')
        number_of_listings = selected_listings.count()
    return [selected_listings,number_of_listings]

def sort_by_price_high_to_low(current_user,search_terms=None):
    if search_terms:
        selected_listings = Listing.objects.filter(Q(name__icontains=search_terms)|Q(description__icontains=search_terms)).exclude(seller=current_user).order_by('price').desc()
        number_of_listings = selected_listings.count()
    else:
        selected_listings = Listing.objects.all().exclude(seller=current_user).order_by('price').desc()
        number_of_listings = selected_listings.count()
    return [selected_listings,number_of_listings]

def sort_by_highest_rated(current_user,search_terms=None):
    if search_terms:
        selected_listings = Listing.objects.filter(Q(name__icontains=search_terms)|Q(description__icontains=search_terms)).exclude(seller=current_user).order_by('likes').desc()
        number_of_listings = selected_listings.count()
    else:
        selected_listings = Listing.objects.all().exclude(seller=current_user).order_by('likes').desc()
        number_of_listings = selected_listings.count()
    return [selected_listings,number_of_listings]
    
search_dict = {
    "sort_by_new":sort_by_new,
    "sort_by_price_low_to_high":sort_by_price_low_to_high,
    "sort_by_price_high_to_low":sort_by_price_high_to_low,
    "sort_by_highest_rated":sort_by_highest_rated,
    "search_marketplace":search_marketplace
}

# Create your views here.
def marketplace(request):
    current_user = request.user
    liked_listing_list = list(Listing.objects.filter(likes=current_user).exclude(seller=current_user).values_list('id', flat=True))
    if request.GET.get("search-terms"):
        search_terms = request.GET.get("search-terms")
        print("SEARCHING")
        if request.GET.get("sort_by"):
            if(request.GET.get("sort_by")=="new"):
                data = search_dict["sort_by_new"](current_user,search_terms)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            elif(request.GET.get("sort_by")=="price_high_to_low"):
                data = search_dict["sort_by_price_high_to_low"](current_user,search_terms)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            elif(request.GET.get("sort_by")=="price_low_to_high"):
                data = search_dict["sort_by_price_low_to_high"](current_user,search_terms)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            else:
                data = search_dict["sort_by_highest_rated"](current_user,search_terms)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
        else:
            data = search_dict["search_marketplace"](current_user,search_terms)
            return render(request,"marketplace.html",{
                "all_listings":data[0],
                "number_of_listings_found":data[1],
                "liked_listing_list":liked_listing_list
                })
    else:
        if request.GET.get("sort_by"):
            if(request.GET.get("sort_by")=="new"):
                data = search_dict["sort_by_new"](current_user)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            elif(request.GET.get("sort_by")=="price_high_to_low"):
                data = search_dict["sort_by_price_high_to_low"](current_user)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            elif(request.GET.get("sort_by")=="price_low_to_high"):
                data = search_dict["sort_by_price_low_to_high"](current_user)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
            else:
                data = search_dict["sort_by_highest_rated"](current_user)
                return render(request,"marketplace.html",{
                    "all_listings":data[0],
                    "number_of_listings_found":data[1],
                    "liked_listing_list":liked_listing_list
                    })
        else:
            data = search_dict["search_marketplace"](current_user)
            return render(request,"marketplace.html",{
                "all_listings":data[0],
                "number_of_listings_found":data[1],
                "liked_listing_list":liked_listing_list
                })

def categories(request,category_id):
    current_user = request.user
    requested_category = ListingCategory.objects.get(pk=category_id)
    all_listings_in_this_category = Listing.objects.filter(categories=requested_category).exclude(seller=current_user)
    number_of_listings_found = all_listings_in_this_category.count()
    liked_listing_list = list(Listing.objects.filter(likes=current_user).exclude(seller=current_user).values_list('id', flat=True))
    return render(request,"categories.html",{
        "requested_category":requested_category,
        "all_listings_in_this_category":all_listings_in_this_category,
        "number_of_listings_found":number_of_listings_found,
        "liked_listing_list":liked_listing_list
    })

def single_listing(request,listing_id):
    requested_listing = Listing.objects.get(pk=listing_id)
    user_has_liked_this_post = False
    if request.user in list(requested_listing.likes.all()):
        user_has_liked_this_post = True
    return render(request,"single-product-details.html",{
        "requested_listing":requested_listing,
        "user_has_liked_this_post":user_has_liked_this_post
    })

@login_required
def my_listings(request):
    all_listings = Listing.objects.filter(seller=request.user)
    number_of_listings_found = all_listings.count()
    return render(request,"my_listings.html",{
        "all_listings":all_listings,
        "number_of_listings_found":number_of_listings_found
    })

@login_required
def favourite(request,listing_id):
    current_listing = Listing.objects.get(pk=listing_id)
    current_user = request.user
    if current_user in current_listing.likes.all():
        try:
            current_listing.likes.remove(current_user)
            response = "The listing has been successfully unliked"
        except:
            response = "Something went wrong!"
            
        return JsonResponse({
            "response":response
        }, status=204)
    else:
        try:
            current_listing.likes.add(current_user)
            response = "The listing has been successfully liked"
        except:
            response = "Something went wrong!"
            
        return JsonResponse({
            "response":response
        }, status=204)
    
@login_required    
def favourite_listings(request):
    current_user = request.user
    favourite_listings = Listing.objects.filter(likes=current_user)
    return render(request,"favourites.html",{
        "favourite_listings":favourite_listings
    })

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
            new_listing = dirty_listing_creator_form.save(commit=False)
            new_listing.seller = request.user
            new_listing.save()
            messages.success(request, "The listing has been successfully created!")
            return redirect("main_page_link")
        else:
            messages.error(request,"We are unable to create this listing!")
            return render(request,"listing-creator.html",{
                "listing_creator_form":dirty_listing_creator_form,
            }) 
        
@login_required    
def listingeditor(request,listing_id):
    listing_from_db = get_object_or_404(Listing,pk=listing_id)
    if listing_from_db.seller == request.user and listing_from_db is not None:
        if request.method=="GET":
            listing_editor_form = ListingForm(instance=listing_from_db)
            return render(request,"listing-editor.html",{
                "listing_editor_form":listing_editor_form,
                "current_listing":listing_from_db
            })
        else:
            dirty_listing_editor_form = ListingForm(request.POST,instance=listing_from_db)
            if dirty_listing_editor_form.is_valid():
                dirty_listing_editor_form.save()
                messages.success(request, "The listing has been successfully updated!")
                return redirect("main_page_link")
            else:
                return render(request,"listing-editor.html",{
                "listing_editor_form":dirty_listing_editor_form
            })
    else:
            messages.error(request,"You are not the seller of this listing!")
            return redirect("marketplace_link")
            
@login_required
def delete_listing(request,listing_id):
    Listing.objects.filter(pk=listing_id).delete()
    messages.success(request, "The listing has been successfully deleted!")
    return redirect("my_listings_link")