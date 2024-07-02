from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("display_category", views.displayCategory, name="displayCategory"),
    path("listing/<int:id>",views.listing, name="listing"), 
    path("remove_watchlist/<int:id>",views.removeWatchlist, name="removeWatchlist"), 
    path("add_watchlist/<int:id>",views.addWatchlist, name="addWatchlist"),
    path("watchlist", views.displayWatchlist, name="watchlist"),
    path("add_comment/<int:id>",views.add_comment, name="addComment"),
]
