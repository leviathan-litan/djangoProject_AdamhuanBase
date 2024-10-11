#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ——————————————————
# 脚本说明：
# xxxxxxxxx
# ——————————————————

# ========================================
# 开始
# ))))))))) 模块包导入
from django.urls import path, re_path, include
from django.contrib import admin

# Django Rest Framework
from rest_framework.routers import DefaultRouter

from .views import *

# ))))))))) Django Rest Framework
drf_router = DefaultRouter()
drf_router.register('users', UserViewSet)

# ))))))))) Django URL Patterns
urlpatterns = [
    # 首页
    path('', index),

    # Django Rest Framework
    path('drf/', include(drf_router.urls)),
]

# ))))))))) 结束

# ========================================
# 结束
