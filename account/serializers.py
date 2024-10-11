#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ——————————————————
# 脚本说明：
# xxxxxxxxx
# ——————————————————

# ========================================
# 开始
# ))))))))) 模块包导入

from rest_framework import serializers

from .models import *

# ))))))))) 类名

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# ))))))))) 执行阶段

# ))))))))) 结束

# ========================================
# 结束
