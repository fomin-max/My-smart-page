# from django import template
# import datetime
# import feedparser
#
# register = template.Library()
#
#
# @register.inclusion_tag('Wd5PageApp/rssfeed.djhtml')
# def pull_feed(feed_url, posts_to_show=-51):
#     try:
#         feed = feedparser.parse(feed_url)
#         posts = {}
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
#     return {'posts': posts}
#

# $.ajax({
#     url: 'http://www.vesti.ru/vesti.rss',
#     dataType: 'xml',
#     success: function(data) {
# $(data).find("entry").each(function()
# {
#     alert(1);
# });
# },
# error: function()
# {
#     alert("Try again, fool!");
# }
# });
#
# $.get('http://www.vesti.ru/vesti.rss', function()
# {
# $(data).find("entry").each(function()
# { // or "item" or whatever
# suits
# your
# feed
# var
# el = $(this);
#
# console.log("------------------------");
# console.log("title      : " + el.find("title").text());
# console.log("author     : " + el.find("author").text());
# console.log("description: " + el.find("description").text());
# });
# });