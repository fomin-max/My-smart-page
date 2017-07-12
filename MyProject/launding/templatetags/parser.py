from django import template
import datetime
import feedparser
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


register = template.Library()


@register.filter(is_safe=True)
def numb_feed(feed_url, posts_to_show):
    try:
        feed = feedparser.parse(feed_url)
        posts = ""
        i = 0
        while i < posts_to_show:
            pub_date = feed['entries'][i].updated_parsed
            published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
            title = feed['entries'][i]['title']
            summ = feed['entries'][i]['summary']
            link = feed['entries'][i]['link']
            data = published
            posts = posts + "Дата публикации: " + str(data) + "<br>" + str(title) + "<br>" + str(summ) + "<br>" + "<a target=\"_blank\" rel=\"nofollow\" href=\"" + str(link) + "\">Читать далее...</a>" + "\n"
            # print(title, "\n", summ, "\n", link, "\n")
            i += 1
            # for i in range(posts_to_show):
            #     pub_date = feed['entries'][i].updated_parsed
            #     published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
            #     posts = {
            #         'title': feed['entries'][i].title,
            #         'summary': feed['entries'][i].summary,
            #         'link': feed['entries'][i].link,
            #         'date': published,
            #     }
    except:
        pass
    return posts



