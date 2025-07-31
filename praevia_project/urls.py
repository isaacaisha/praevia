# /home/praevia/praevia/praevia_project/urls.py

from django.contrib import admin
from django.urls import path, include
from praevia_app import views_api
from django.conf import settings
from django.views.generic import RedirectView
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls.static import static


admin.site.site_header  =  "Fasto Dashboard"  
admin.site.site_title  =  "Dashboard"
admin.site.index_title  =  "Dashboard"
#handler403 = 'dashboard.views.custom_permission_denied_view'
#handler404 = 'dashboard.views.custom_page_not_found_view'

urlpatterns = [
    # 1) Root URL (“/”) → redirect to the dashboard URL by its name
    #path(
    #    '',
    #    RedirectView.as_view(pattern_name='praevia_app:dashboard', permanent=False),
    #    name='root-redirect'
    #),

    # 2) Admin site
    path('admin/', admin.site.urls),

    # Custom API Root - now points to your custom APIRootView
    path('praevia/api/', views_api.RootAPIView.as_view(), name='api-root'),

    # 3) Built‑in auth views (login, logout, password reset at /accounts/…)
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace='accounts')),
    # 2FA default URLs (login, setup, backup tokens, QR, etc.)
    #path('account/', include('two_factor.urls', namespace='two_factor')),
    path('', include(tf_urls)),  # Include 2FA URLs

    # 4) Your custom user URLs (register, etc.); still lives under /register/, /login/, etc.
    path('users/', include('users.urls', namespace='users')),

    # 5) Dashboard pages under /dashboard/
    path('',include('fasto.urls', namespace='fasto')),
    #path('dashboard/', include('dashboard.urls', namespace='dashboard')),

    # 6) praevia_app
    path('praevia/', include(('praevia_app.urls','praevia_app'), namespace='praevia_app')),

    # Serve favicon.ico
    path('favicon.ico', RedirectView.as_view(url='/static/ico/favicon_api.ico', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
