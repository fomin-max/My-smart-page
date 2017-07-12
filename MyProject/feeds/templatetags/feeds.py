# from django import template
# import datetime
# import feedparser
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
#
#
# register = template.Library()
#
#
# @register.inclusion_tag('Wd5PageApp/rssfeed.djhtml')
# def pull_feed(feed_url, posts_to_show=1):
#     global posts, out
#     try:
#         feed = feedparser.parse(feed_url)
#         posts = {}
#         out = feed['entries'][0]['summary_detail']['value']
#         for i in range(posts_to_show):
#             pub_date = feed['entries'][i].updated_parsed
#             published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
#             posts = {
#                 'title': feed['entries'][i].title,
#                 'summary': feed['entries'][i].summary,
#                 'link': feed['entries'][i].link,
#                 'date': published,
#             }
#     except:
#         pass
#     return HttpResponse(out, content_type="text/plain")
#
