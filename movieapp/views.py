from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
import requests
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import Rate,Comment,Favourite
# Create your views here.
def index(request):
    #To get the search data from the user
     if request.method=="POST":
               search=request.POST.get('search')
     else:
          search=request.POST.get('search','one piece')
     key='24a5b4be'
     API=f'http://www.omdbapi.com/?apikey={key}&s={search}'
     response=requests.get(API) #getting the data from the api
     data=response.json() #converting the data into json form
     search_data=data.get('Search',[]) # targeting the search data

     #checking if the data is received or not and send to index.html
     if(search_data):
          return render(request,'index.html',{'data':search_data})
     return render(request,'index.html')
    
#single detail page for single movie information
def detail(request,id):
     key='24a5b4be'
     API=f'http://www.omdbapi.com/?apikey={key}&i={id}'
     response=requests.get(API) #getting the data from the api
     data=response.json() #converting the data into json form
     rate=Rate.objects.filter(username=request.user.username,rate_id=id).first()
     vote=rate.vote if rate else 0
     comment=Comment.objects.filter(comment_id=id).order_by("-created_at")
     #checking if the data is received or not and send to index.html
     if(data):
          return render(request,'detail.html',{'data':data,'vote':vote,"comment":comment})
     return render(request,'detail.html')
    
def rate(request,id):
     vote=request.POST.get('select')
     try:
       rate = Rate.objects.get(username=request.user.username,rate_id=id)
     # Object exists
       rate.vote = vote
       rate.save()
       messages.success(request, "Successfully Updated")
       
     except Rate.DoesNotExist:
     # Object does not exist
         if request.method == "POST":
          rate= Rate(username=request.user.username,rate_id=id, vote=vote)
          rate.save()
          messages.success(request, "Successfully Added")
     return redirect('detail',id=id)   

def comment(request,id):
     comment=request.POST.get('comment')
     if request.user.is_authenticated:
          if request.method=="POST":
               user_comment=Comment(username=request.user.username,comment_id=id,comment=comment)
               user_comment.save()
               messages.success(request,"Successfully added comment")
               return redirect('detail',id=id)          
               
     else:
          messages.warning(request,"You must be Logged In")
          return redirect('detail',id=id)          

def delete(request,id,imdbID):
     print(id)
     print(request.user.username)
     comment=Comment.objects.filter(username=request.user.username,id=id)
     comment.delete()
     return redirect('detail',id=imdbID)

def favourite(request):
     movie_id=request.POST.get("id")
     movie_title=request.POST.get("title")
     movie_image=request.POST.get("image")
     card=Favourite.objects.filter(username=request.user.username,movie_id=movie_id)
     if card:
          messages.warning(request,"Already exist on your Watch List")
          return redirect('detail',id=movie_id)
          
     else:
          movie=Favourite(username=request.user.username,movie_id=movie_id,movie_title=movie_title,movie_image=movie_image)
          movie.save()
          messages.success(request,"Movie Succesfully added to you Favourite Watch List")
          return redirect('detail',id=movie_id)
def watch_list(request):
     movie=Favourite.objects.filter(username=request.user.username)
     if movie:
          return render(request,'watch.html',{'movie':movie})
     else:
          return render(request,'watch.html')

def watch_list_delete(request,id):
     print(id)
     print(request.user.username)
     movie=Favourite.objects.filter(username=request.user.username,movie_id=id)
     movie.delete()
     return redirect('watch_list')



def signup_user(request):
     if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password1')
          confirm_password=request.POST.get('password2')
          check_user=User.objects.filter(username=username)
          if(username==check_user):
               messages.warning(request,"Username already exists")
               return redirect("signup_user")
          if(password!=confirm_password):
               messages.warning(request,"Confirm password is not matching. Please Try again")
               return redirect("signup_user");
          user=User.objects.create_user(username=username,password=password)
          user.save()
          messages.warning(request,"Successfully Registered")
          return redirect("index")
     else:
          return render(request,'signup.html')


def login_user(request):
     if request.method=="POST":
          username=request.POST.get("username")  
          password=request.POST.get("password") 
          check_user=authenticate(request,username=username,password=password)
          if check_user:
               login(request,check_user)
               messages.success(request,"Successfully Logged In")
               return redirect("index")
          else:
               messages.warning(request,"There was some error please try again!")
               return redirect("login_user")
     return render(request,"login.html")

def logout_user(request):
     logout(request)
     return redirect("login_user")