from django.shortcuts import render
from django.http import HttpResponse
from .models import cat_submissions
from .models import sub_cat_submissions
from .models import channel
import requests
import json
import locale
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils import formats
import random
from django.core.paginator import Paginator

# Issue: Eliminate redundancies
# Intent: Set up admin review & flag database / interface
# Intent: Set up caching to update Youtube API data based on etag or fixed intervals


def one(request):

    return render(request, 'rabbithole/index.html')


def two(request, cat_id):

    if "submission" not in cat_id:

        sub_cats = channel.objects.filter(
            cat=cat_id).order_by().values('sub_cat').distinct()
        unique_sub_cats = list(sub_cats.values_list('sub_cat', flat=True))
        unique_sub_cats_shuffled = random.sample(
            unique_sub_cats, len(unique_sub_cats))
        unique_sub_cat_json = json.dumps(
            list(unique_sub_cats_shuffled), cls=DjangoJSONEncoder)
        original_cat = cat_id

        context = {
            'unique_sub_cat_json': unique_sub_cat_json,
            'original_cat': original_cat,
        }

        template = 'rabbithole/subcat.html'

    else:

        cat_submission = request.POST["cat_submission"]
        cat_submission = channel(cat=cat_submission)
        cat_submission.save()

        cats = channel.objects.filter(
            cat=cat_id).order_by().values('cat').distinct()
        unique_cats = list(cats.values_list('cat', flat=True))
        unique_cats_shuffled = random.sample(unique_cats, len(unique_cats))
        unique_cat_json = json.dumps(
            list(unique_cats_shuffled), cls=DjangoJSONEncoder)

        context = {
            'unique_cat_json': unique_cat_json,
        }

        template = 'rabbithole/index.html'

    return render(request, template, context)


def three(request, cat_id, subcat_id):

    print(subcat_id)

    if "submission" not in subcat_id:

        channels_ordered = list(channel.objects.filter(
            cat=cat_id).filter(sub_cat=subcat_id))
        channels = random.sample(channels_ordered, len(channels_ordered))
        original_cat = cat_id
        original_sub_cat = subcat_id

        context = {
            'channels': channels,
            'original_cat': original_cat,
            'original_sub_cat': original_sub_cat,
        }

        template = 'rabbithole/channellist.html'

    else:

        sub_cat_submission = request.POST["sub_cat_submission"]
        sub_cat_submission = channel(cat=cat_id, sub_cat=sub_cat_submission)
        sub_cat_submission.save()

        sub_cats = channel.objects.filter(
            cat=cat_id).order_by().values('sub_cat').distinct()
        unique_sub_cats = list(sub_cats.values_list('sub_cat', flat=True))
        unique_sub_cats_shuffled = random.sample(
            unique_sub_cats, len(unique_sub_cats))
        unique_sub_cat_json = json.dumps(
            list(unique_sub_cats), cls=DjangoJSONEncoder)
        original_cat = cat_id

        context = {
            'sub_cats': sub_cats,
            'original_cat': original_cat,
            'unique_sub_cat_json': unique_sub_cat_json,
        }

        template = 'rabbithole/subcat.html'

    return render(request, template, context)


def four(request, cat_id, subcat_id, channel_id):

    channels_ordered = list(channel.objects.filter(
        cat=cat_id).filter(sub_cat=subcat_id))
    channels = random.sample(channels_ordered, len(channels_ordered))
    paginator = Paginator(channels, 4)
    original_cat = cat_id
    original_sub_cat = subcat_id

    context = {
        'channels': channels,
        'original_cat': original_cat,
        'original_sub_cat': original_sub_cat,
    }

    template = 'rabbithole/channellist.html'

    channel_submission = request.POST["channel_submission"]
    username = channel_submission

    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics%2Csnippet&forUsername={}&key=AIzaSyA4zyuxHi6kaQ1p79FGdrTI-eEyeJWsQzQ"

    r = requests.get(url.format(username)).json()

    subs = '{:,}'.format(int(r["items"][0]["statistics"]["subscriberCount"]))
    views = '{:,}'.format(int(r["items"][0]["statistics"]["viewCount"]))
    uploads = '{:,}'.format(int(r["items"][0]["statistics"]["videoCount"]))

    subsfinal = subs.replace(',', ' ')
    viewsfinal = views.replace(',', ' ')
    uploadsfinal = uploads.replace(',', ' ')

    channel_data = {
        'subscribers': subsfinal,
        'viewcount': viewsfinal,
        'uploads': uploadsfinal,
        'title': r["items"][0]["snippet"]["title"],
        'customUrl': r["items"][0]["snippet"]["customUrl"],
        'channel_name': r["items"][0]["snippet"]["title"],
        'thumbnail': r["items"][0]["snippet"]["thumbnails"]['default']['url'],
    }

    channel_submission = channel(cat=cat_id, sub_cat=subcat_id, channel_name=channel_data["channel_name"].lower(
    ), uploads=channel_data["uploads"], subscribers=channel_data["subscribers"], viewcount=channel_data["viewcount"], thumbnail=channel_data["thumbnail"], customUrl=channel_data["customUrl"])
    channel_submission.save()

    return render(request, template, context)
