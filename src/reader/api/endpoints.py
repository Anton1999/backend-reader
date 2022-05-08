from django.conf.urls import url, include

api_urls = [

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/', include('rest_auth.urls')),
    url(r'^/rest-auth/vk/', include('social_django.urls')),
    url(r'^book/', include('book.urls')),
    url(r'^category/', include('genres.urls')),
    url(r'^account/', include('core.urls')),
]
