from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    
    post = Tech.objects.all()[::-1]
    posts = post[:2]

    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]

    #Model Showbiz | takes 4 last elements; its reversed
    showbiz_post_v = Showbiz.objects.all()[::-1]
    showbiz_post = showbiz_post_v[:2]

    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_nav_1 = showbiz_post_nav[2]
    showbiz_post_nav_2 = showbiz_post_nav[3]

    Header_Post_nav = HeaderPost.objects.all()[::-1]
    header_post_nav_1 = Header_Post_nav[5]

    sport_post_nav = Sport.objects.all()[::-1] 
    sport_post_nav_1 = sport_post_nav[3]
    sport_post_nav_2 = sport_post_nav[4]

    #Shobiz reversed posts 
    showbiz_post_3_1 = showbiz_post_v[2]
    showbiz_post_3_2 = showbiz_post_v[3]
    showbiz_post_3_3 = showbiz_post_v[4]
    showbiz_post_3_4 = showbiz_post_v[5]
    showbiz_post_3_5 = showbiz_post_v[6]
    showbiz_post_3_6 = showbiz_post_v[7]
    showbiz_post_3_7 = showbiz_post_v[8]
    showbiz_post_3_8 = showbiz_post_v[9]
    showbiz_post_3_9 = showbiz_post_v[10]
    showbiz_post_3_10 = showbiz_post_v[11]



    #Model Travel | takes 4 last elements; its reversed
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:1]
        
    #Travel reversed posts
    travel_post_4_1 = travel_post_v[1]
    travel_post_4_2 = travel_post_v[2]
    travel_post_4_3 = travel_post_v[3]
    travel_post_4_4 = travel_post_v[4]


    #Travel reversed posts 
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post = sport_post_v[:3]
    
    sport_post_1 = sport_post_v[3]
    sport_post_2 = sport_post_v[4]
    sport_post_3 = sport_post_v[5]
    sport_post_4 = sport_post_v[6]
    sport_post_5 = sport_post_v[7]
    sport_post_6 = sport_post_v[8]
    sport_post_7 = sport_post_v[9]
    sport_post_8 = sport_post_v[10]
    sport_post_9 = sport_post_v[11]
    sport_post_10 = sport_post_v[12]
    sport_post_11 = sport_post_v[13]
    sport_post_12 = sport_post_v[14]
    sport_post_13 = sport_post_v[15]
    sport_post_14 = sport_post_v[16]
    sport_post_15 = sport_post_v[17]

    #Nav Trending


    context = {
        'posts':posts,
        'header_post':header_post,
        'showbiz_post':showbiz_post,
        "travel_post":travel_post,
        "sport_post":sport_post,
        #Travel Dict 
        "travel_post_4_1":travel_post_4_1,
        "travel_post_4_2":travel_post_4_2,
        "travel_post_4_3":travel_post_4_3,
        "travel_post_4_4":travel_post_4_4,
        #Showbiz Dict 
        'showbiz_post_3_1':showbiz_post_3_1,
        'showbiz_post_3_2':showbiz_post_3_2,
        'showbiz_post_3_3':showbiz_post_3_3,
        'showbiz_post_3_4':showbiz_post_3_4,
        'showbiz_post_3_5':showbiz_post_3_5,
        'showbiz_post_3_6':showbiz_post_3_6,
        'showbiz_post_3_7':showbiz_post_3_7,
        'showbiz_post_3_8':showbiz_post_3_8,
        'showbiz_post_3_9':showbiz_post_3_9,
        'showbiz_post_3_10':showbiz_post_3_10,
        #Sport Dict 
        'sport_post_1':sport_post_1,
        'sport_post_2':sport_post_2,
        'sport_post_3':sport_post_3,
        'sport_post_4':sport_post_4,
        'sport_post_5':sport_post_5,
        'sport_post_6':sport_post_6,
        'sport_post_7':sport_post_7,
        'sport_post_8':sport_post_8,
        'sport_post_9':sport_post_9,
        'sport_post_10':sport_post_10,
        'sport_post_11':sport_post_11,
        'sport_post_12':sport_post_12,
        'sport_post_13':sport_post_13,
        'sport_post_14':sport_post_14,
        'sport_post_15':sport_post_15,
        #Nav Dict
        'showbiz_post_nav_1':showbiz_post_nav_1,
        'showbiz_post_nav_2':showbiz_post_nav_2,
        'header_post_nav_1':header_post_nav_1,
        'sport_post_nav_1':sport_post_nav_1,
        'sport_post_nav_2':sport_post_nav_2,


    }
    return render(request,'index.html',context)


def single(request,pk):

    post = Tech.objects.get(id=pk)

    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]

    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts

    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post = sport_post_v[:3]

    showbiz_post_2 =showbiz_post_nav[6]



    context = {
        "post":post,
        "showbiz_post_1":showbiz_post_1,
        "showbiz_post_2":showbiz_post_2,
        "sport_post":sport_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts
    }
    return render (request,'single-post.html',context)




def header_single(request,nid):
    headpost = HeaderPost.objects.get(id=nid)

    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts

    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]

    context = {
        'headpost':headpost,
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts

    }
    return render (request,'header-single-post.html',context)


def tech_single(request,pin):
    techpost = Tech.objects.get(id=pin)


    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts

    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]

    context = {
        'techpost':techpost,
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts

    }
    return render (request,'tech-single.html',context)





def showbiz_single(request,pin):
    showbizpost = Showbiz.objects.get(id=pin)

    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts

    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]

    context = {
        'showbizpost':showbizpost,
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts

    }
    return render (request,'showbiz-single-post.html',context)


def sport_single(request,nop):
    sportpost = Sport.objects.get(id=nop)

    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts

    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]

    context = {
        'sportpost':sportpost,
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts

    }
    return render (request,'sport-single-post.html',context)

def travel_single(request,suk):
    travelpost = Travel.objects.get(id=suk)

    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts
    #These var stands for popular
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]

    context = {
        'travelpost':travelpost,
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts
    }
    return render (request,'travel-single-post.html',context)






def about_us(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    lastest_post = Showbiz.objects.all()[::-1]
    lastest = lastest_post[2]
    header_about = HeaderPost.objects.all()[::-1]
    header_a = header_about[0]
    context = {
        "header_post":header_post,
        "lastest":lastest,
        "header_a":header_a
    }
    return render(request,'about.html',context)


def contact(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]

    context = {
        "header_post":header_post,

    }
    return render(request,'contact.html',context)


def category(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts
    # video_url = Video.objects.all()[::-1]
    # video = video_url[0]
    
    context = {
        "header_post":header_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,
        #end nav-bar-posts

        # "video":video,
    }
    return render(request,'category.html',context)


def sport_category(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts


    #variables for sport category templates
    sport = HeaderPost.objects.filter(category='Sport')[::-1] 
    sport_post_category_header = sport[:2]
    #-----------------------
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_category = sport_post_v[:8]


   

    context = {
        "header_post":header_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,

         #variables for sport category templates
        "sport_post_category_header":sport_post_category_header,
        "sport_post_category":sport_post_category,
    }
    return render (request,'sport-category.html',context)




def travel_category(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts


    #variables for sport category templates
    travel = HeaderPost.objects.filter(category='Travel')[::-1] 
    travel_post_category_header = travel[:2]
    #-----------------------
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post_category = travel_post_v[:8]


   

    context = {
        "header_post":header_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,

         #variables for sport category templates
        "travel_post_category_header":travel_post_category_header,
        "travel_post_category":travel_post_category,
    }
    return render (request,'travel-category.html',context)



def showbiz_category(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts


    #variables for sport category templates
    showbiz = HeaderPost.objects.filter(category='Showbiz')[::-1] 
    showbiz_post_category_header = showbiz[:2]
    #-----------------------
    showbiz_post_v = Showbiz.objects.all()[::-1] 
    showbiz_post_category = showbiz_post_v[:8]


   

    context = {
        "header_post":header_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,

         #variables for sport category templates
        "showbiz_post_category_header":showbiz_post_category_header,
        "showbiz_post_category":showbiz_post_category,
    }
    return render (request,'showbiz-category.html',context)




def tech_category(request):
    #Model header | takes 4 last elements; its reversed
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:5]
    #nav-bar-posts
    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]
    sport_post_v = Sport.objects.all()[::-1] 
    sport_post_trending = sport_post_v[:3]
    post = Tech.objects.all()[::-1]
    posts = post[:2]
    travel_post_v = Travel.objects.all()[::-1] 
    travel_post = travel_post_v[:4]
    Header_Post_v = HeaderPost.objects.all()[::-1]
    header_post = Header_Post_v[:6]
    #end nav-bar-posts


    #variables for sport category templates
    tech = HeaderPost.objects.filter(category='Tech')[::-1] 
    tech_post_category_header = tech[:2]
    #-----------------------
    tech_post_v = Tech.objects.all()[::-1] 
    tech_post_category = tech_post_v[:8]


   

    context = {
        "header_post":header_post,
        #nav-bar-posts
        "showbiz_post_1":showbiz_post_1,
        "sport_post_trending":sport_post_trending,
        "posts":posts,
        "travel_post":travel_post,
        "header_post":header_post,

         #variables for sport category templates
        "tech_post_category_header":tech_post_category_header,
        "tech_post_category":tech_post_category,
    }
    return render (request,'tech-category.html',context)