from django.shortcuts import render, get_object_or_404, redirect
from .models import tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import TweetForm, UserRegistrationForm


def tweetlist(request):
    tweets = tweet.objects.all().order_by("-date_created")
    return render(request, "tweet_list.html", {"tweets": tweets})


# Create your views here.


@login_required
def tweet_create(request):
    if request.method == "POST":
        print("FILES:", request.FILES)  # Debug print
        print("POST:", request.POST)  # Debug print
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            if "photo" in request.FILES:
                new_tweet.photo = request.FILES["photo"]
            new_tweet.user = request.user
            new_tweet.save()
            return redirect("tweetlist")
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {"form": form})


@login_required
def tweet_edit(request, tweet_id):
    tweetu = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    print(tweetu)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweetu)
        if form.is_valid():
            tweeti = form.save(commit=False)
            tweeti.user = request.user
            tweeti.save()
            return redirect("tweetlist")
    else:
        form = TweetForm(instance=tweetu)
    return render(request, "tweet_form.html", {"form": form})


@login_required
def tweet_delete(request, tweet_id):
    # tweetu = None
    tweetu = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    print(tweetu)
    if request.method == "POST":
        tweetu.delete()
        return redirect("tweetlist")

    return render(request, "del_confirm.html", {"tweet": tweetu})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("tweetlist")

    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        results = tweet.objects.filter(text__contains=searched)
        return render(request, "searchu.html", {"tweets": results})

    return render(request, "searchu.html")
