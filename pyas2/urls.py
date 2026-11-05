from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required

from pyas2 import views


urlpatterns = [
    path("as2receive/", views.ReceiveAs2Message.as_view(), name="as2-receive"),
    # Add the url again without slash for backwards compatibility
    path("as2receive", views.ReceiveAs2Message.as_view(), name="as2-receive"),
    path(
        "as2send/",
        staff_member_required(
            permission_required("pyas2.add_message", raise_exception=True)(
                views.SendAs2Message.as_view()
            )
        ),
        name="as2-send",
    ),
    path(
        "download/<str:obj_type>/<str:obj_id>/",
        staff_member_required(views.DownloadFile.as_view()),
        name="download-file",
    ),
]
