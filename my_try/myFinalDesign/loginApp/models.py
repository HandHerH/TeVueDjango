from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)  # 昵称，最大长度100字符
    username = models.CharField(max_length=100, unique=True)  # 用户名，不能重复
    phone = models.CharField(max_length=13, unique=True)  # 电话号
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True, default=None)  # 邮箱字段，允许为空
    password = models.CharField(max_length=128)  # 密码，128字符长度（通常存储哈希后的密码）
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间，自动记录用户创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间，记录用户信息更新的时间

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
