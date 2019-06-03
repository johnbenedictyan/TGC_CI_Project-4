from django.shortcuts import render,redirect
from marketplace_app.models import ListingCategory

# Create your views here.
def main_page(request):
    return render(request,"index.html")

def test_page(request):
    return render(request,"test.html")
    
def test_function(request):
    array = [
    ["Men's Fashion","Men's Clothes","Men's Watches","Men's Footwear","Men's Bags & Wallets","Men's Accessories"],
    ["Women's Fashion","Women's Clothes","Women's Watches","Women's Shoes","Women's Bags & Wallets","Women's Jewellery","Women's Accessories"],
    ["Kid's Fashion","Kid's Clothes","Kid's Watches","Kid's Footwear","Kid's Bags & Wallets","Kid's Accessories"],
    ["Luxury","Luxury Apparel","Luxury Accessories","Luxury Bags & Wallets","Luxury Watches","Luxury Shoes"],
    ["Health & Beauty","Makeup","Hair Care","Face & Skin Care","Bath & Body","Perfume & Deodorants","Hand & Foot Care","Men's Grooming"],
    ["Babies & Kids","Maternity","Nursing & Feeding","Strollers","Baby Bags & Carriers"],
    ["Books & Stationery","Fiction Books","Non-Fiction Books","Comics & Manga","Textbooks","Children's Books","Stationery"],
    ["Home & Living","Sofas","Home Decor","Bed & Mattresses","Shelves & Drawers","Furniture"],
    ["Home Appliances","Kitchenware","TV & Entertainment Systems","Cleaning & Laundry","Cooling & Air Care"],
    ["Cars","Cars for Sale","Parallel Imports","Commerical Vehicles","Vehicle Rentals"],
    ["Motorcycles","Motorcycles for Sale","Motorcycle Apparel","Motorcycle Parts & Accessories"],
    ["Bicycles","Bicycles for Sale","Bicycle Apparel","Bicycle Parts & Accessories"],
    ["Learning & Enrichment","Professional Skills","Workshops","Sport & Fitness Classes","Music & Art Classes","Enrichment & Tuition"],
    ["Music & Media","Music Instruments","CDs,DVDs & Other Media"],
    ["Photography","Cameras","Video Equipment","Drones","Lenses","Camera Accessories"],
    ["Design & Craft","Handmade Craft","Arts & Prints","Craft Supplies & Tools"],
    ["Sports","Sports Apparel","Braces & Supports","Sports & Games Equipment","Weight & Gym Equipment"],
    ["Vintage & Collectibles","Vintage Collectibles","Vintage Watches & Jewellery","Stamps & Prints","Currency"],
    ["Attractions","Events & Concerts","Gift Cards & Vouchers"],
    ["Toys & Games","Video Games","Stuffed Toys","Bricks & Figurines","Board Games & Cards"],
    ["Electronics","Headphones","Earphones","Audio Recording Equipment","Audio Production Equipment","Audio Parts & Accessories","Speakers"],
    ["Computers","Desktops for Sale","Desktop Parts & Accessories","Laptops for Sale","Laptop Parts & Accessories"],
    ["Everything Else"]
    ]

    for i in array:
        for j in i:
            ListingCategory.objects.create(name="{}".format(j),description="{}".format(j))
    return render(request,"test.html")