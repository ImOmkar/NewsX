from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('top_headlines/', views.top_headlines, name="Top_headlines"),
    path('search/', views.search_news, name="search"),


    #countries
    path('argentina/', views.argentina, name="argentina"),
    path('australia/', views.australia, name="australia"),
    path('austria/', views.austria, name="austria"),
    path('belgium/', views.belgium, name="belgium"),
    path('brazil/', views.brazil, name="brazil"),
    path('bulgaria/', views.bulgaria, name="bulgaria"),
    path('canada/', views.canada, name="canada"),
    path('china/', views.china, name="china"),
    path('colombia/', views.colombia, name="colombia"),
    path('cuba/', views.cuba, name="cuba"),
    path('czech/', views.czech, name="czech"),
    path('egypt/', views.egypt, name="egypt"),
    path('france/', views.france, name="france"),
    path('germany/', views.germany, name="germany"),
    path('greece/', views.greece, name="greece"),
    path('hongkong/', views.hongkong, name="hongkong"),
    path('hungary/', views.hungary, name="hungary"),
    path('india/', views.india, name="india"),
    path('indonesia/', views.indonesia, name="indonesia"),
    path('ireland/', views.ireland, name="ireland"),
    path('israel/', views.israel, name="israel"),
    path('italy/', views.italy, name="italy"),
    path('japan/', views.japan, name="japan"),
    path('latvia/', views.latvia, name="latvia"),
    path('lithuania/', views.lithuania, name="lithuania"),
    path('malaysia/', views.malaysia, name="malaysia"),
    path('mexico/', views.mexico, name="mexico"),
    path('morocco/', views.morocco, name="morocco"),
    path('netherland/', views.netherland, name="netherland"),
    path('nzealand/', views.nzealand, name="nzealand"),
    path('nigeria/', views.nigeria, name="nigeria"),
    path('norway/', views.norway, name="norway"),
    path('philip/', views.philip, name="philip"),
    path('poland/', views.poland, name="poland"),
    path('portugal/', views.portugal, name="portugal"),
    path('romania/', views.romania, name="romania"),
    path('russia/', views.russia, name="russia"),
    path('saudi/', views.saudi, name="saudi"),
    path('serbia/', views.serbia, name="serbia"),
    path('singapore/', views.singapore, name="singapore"),
    path('slovekia/', views.slovekia, name="slovekia"),
    path('slovenia/', views.slovenia, name="slovenia"),
    path('safrica/', views.safrica, name="safrica"),
    path('skorea/', views.skorea, name="skorea"),
    path('sweden/', views.sweden, name="sweden"),
    path('switz/', views.switz, name="switz"),
    path('taiwan/', views.taiwan, name="taiwan"),
    path('thailand/', views.thailand, name="thai"),
    path('turkey/', views.turkey, name="turkey"),
    path('uae/', views.uae, name="uae"),
    path('ukraine/', views.ukraine, name="ukraine"),
    path('uk/', views.uk, name="uk"),
    path('us/', views.us, name="us"),
    path('venuzuela/', views.venuzuela, name="venuzuela"),
]
