from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blogs', views.allblogs, name='blogs'),

    path('add-blog/',views.addblogpage,name='addblogpage'),

    path('add-blog/addblogs',views.addblogshandler,name='abh'),

    path('add-blog/delete_blog',views.deleteblog,name='deleteblog'),
    path('d-forms',views.djangofroms,name='djangofrom'),
    path('forms',views.modelDjangoFrom,name='abc'),
    path('delete/<id>',views.deleteById),
    path('update/<id>',views.updateblog),
    path('update_data/<id>',views.updatedata)

]