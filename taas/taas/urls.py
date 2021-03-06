"""taas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from autotest.api import SutView, test_execution, upload_test_reporting, test_report_page, detail_test_execution

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sut/<uuid:uuid>/', SutView.as_view()),
    path('test-execution/<uuid:rq_jid>/console/', test_execution),
    path('test-execution/<int:te_id>/', detail_test_execution),
    path('test-reporting/<int:te_id>/', upload_test_reporting),
    path('test-reporting/<int:te_id>/<name>.html', test_report_page),
]
