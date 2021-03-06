from django.conf.urls import url
from products.views import UserProducHistoryView
from .views import AccountHomeView, AccountEmailActivateView, UserDetailUpdateView

urlpatterns = [
	url(r'^history/products/$', UserProducHistoryView.as_view(), name='user-product-history'),
	url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
	url(r'^$', AccountHomeView.as_view(), name='home'),
	url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
	url(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),

]