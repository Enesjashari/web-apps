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

    # Header_Post_v = HeaderPost.objects.all()[::-1]
    # header_post = Header_Post_v[:5]

    showbiz_post_nav = Showbiz.objects.all()[::-1]
    showbiz_post_1 = showbiz_post_nav[:3]

    showbiz_post_2 =showbiz_post_nav[6]

    test = 'enes'


    context = {
        'post':post,
        "showbiz_post_1":showbiz_post_1,
        "showbiz_post_2":showbiz_post_2,
        "test":test,
    }
    return render (request,'single-post.html',context)




def header_single(request,nid):
    headpost = HeaderPost.objects.get(id=nid)

    context = {
        'headpost':headpost,
    }
    return render (request,'header-single-post.html',context)






def showbiz_single(request,pin):
    showbizpost = Showbiz.objects.get(id=pin)

    context = {
        'showbizpost':showbizpost,
    }
    return render (request,'showbiz-single-post.html',context)


def sport_single(request,nop):
    sportpost = Sport.objects.get(id=nop)

    context = {
        'sportpost':sportpost,
    }
    return render (request,'sport-single-post.html',context)

def travel_single(request,suk):
    travelpost = Travel.objects.get(id=suk)

    context = {
        'travelpost':travelpost,
    }
    return render (request,'travel-single-post.html',context)






def about_us(request):
    lastest_post = Showbiz.objects.all()[::-1]
    lastest = lastest_post[2]
    context = {
        "lastest":lastest,
    }
    return render(request,'about.html',context)







# Views
def test1(request):

    var1 = 'Django'
    var2 = 'Framework '
    var3 = 'Python'

    context = {
        "var1":var1,
        "var2":var2,
        "var3":var3,

    }
    return render(request,'test1.html',context)

def test2(request):
    var4 = 'PHP'

    context = {

        "var4":var4,

    }
    return render(request,'test2.html',context)
