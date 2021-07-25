from django.urls import path
from .views import AccountCreateview, SigninView, BalanceView, TransactonView, PaymentHistory, \
    SignoutView, TransactionFilterView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login", SigninView.as_view(), name="signin"),
    path("register", AccountCreateview.as_view(), name="signup"),
    path("home", login_required(TemplateView.as_view(template_name="home.html"), login_url="signout"), name="home"),
    path("balance", BalanceView.as_view(), name="bal"),
    path("transfer", TransactonView.as_view(), name="transact"),
    path("payhis", PaymentHistory.as_view(), name="payhis"),
    path("logout", SignoutView.as_view(), name="signout"),
    path("filter", TransactionFilterView.as_view(), name="filter")
]
