import datetime
import feedparser
from django import template

register = template.Library()


@register.filter(is_safe=True)
def city_feed(feed_url, posts_to_show):
    try:
        feed = feedparser.parse(feed_url)
        posts = ""
        i = 0
        # print(feed)
        while i < posts_to_show:
            pub_date = feed['entries'][i].updated_parsed
            published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
            title = feed['entries'][i]['title']
            summ = feed['entries'][i]['summary']
            link = feed['entries'][i]['link']
            term = feed['entries'][i]['tags'][0]['term']
            data = published
            posts = posts + "Дата публикации: " + str(data) + "<br>" + "<a target=\"_blank\" rel=\"nofollow\" href=\"" + str(link) + "\">Источник</a>" + "<br>" + str(title) + "<br>" + str("Категория: ") + str(term) + "\n"

            # + "<p><a target=\"_blank\" rel=\"nofollow\" href=\"" + str(link) + "\">Источник</a></p>" + "<br>" +

            # print(title, "\n", summ, "\n", link, "\n", term, "\n")
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
