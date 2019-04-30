from django.urls import path

from .views import BookmarkList, BookmarkCreate, BookmarkUpdate, BookmarkDetail, BookmarkDelete

# namespace 이름 공간
# 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해서 사용
# namespace라는 인수가 존재

app_name = 'bookmark'
urlpatterns = [
    # path(url pattern, view, url pattern name),
    # 함수형 뷰 : 이름만
    # 클래스형 뷰 : 이름.as_view()
    # path, uuid, slug, int, str => custom converter
    # map/127.2222-34.3412/
    # convert -> location
    # map/<location:valu>/
    # converter
    # detail/abc/

    path('detail/<int:pk>/',BookmarkDetail.as_view(), name='detail'),
    path('delete/<int:pk>/',BookmarkDelete.as_view(), name='delete'),
    path('update/<int:pk>/',BookmarkUpdate.as_view(), name='update'),

    path('create/',BookmarkCreate.as_view(), name='create'),
    path('', BookmarkList.as_view(), name='index'),

]