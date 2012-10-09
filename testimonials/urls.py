from django.conf.urls.defaults import patterns, url
from addons.testimonials.feeds import LatestEntriesFeed

urlpatterns = patterns('addons.testimonials.views',
    url(r'^testimonials/$', 'search', name="testimonials"),
    url(r'^testimonials/search/$', 'search_redirect', name="testimonial.search"),
    url(r'^testimonials/feed/$', LatestEntriesFeed(), name='testimonial.feed'),
    url(r'^testimonials/(?P<pk>\d+)/$', 'details', name="testimonial.view"),
)