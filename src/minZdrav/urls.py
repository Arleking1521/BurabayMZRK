from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from logRegisPages.views import  registration, activate, user_login, user_logout, CustomPasswordResetView, CustomPasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news.views import post_new
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('static_pages.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    
    
]
urlpatterns += i18n_patterns(
    path('news/', include('news.urls')),
    path('new-news/', post_new, name = 'new_new'),
    path('med-services/', include('medServices.urls')),
    path('rules/', include('info_page.urls')),
    path('viewSovet/', include('viewSovet.urls')),
    path('contacts/', include('contact_pages.urls')),
    path('histories/', include('history_legends.urls')),
    path('ceo-info/', include('ceoInfo.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('organization-structure/', include('orgStruct.urls')),
    path('rights-acts/', include('ProvActs.urls')),
    path('workers-info/', include('workersInfo.urls')),
    path('anticorruption/', include('antiCorruptions.urls')),
    path('about/', include('aboutPage.urls')),    
    path('reviews/', include('reviewsBlog.urls')),
    path('advertisement/', include('advertisement.urls')),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('registration/', registration, name = 'registr'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)