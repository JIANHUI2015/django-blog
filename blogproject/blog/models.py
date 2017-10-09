# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	"""
	要求模型必须继承models.Model类
	CharField 指定了name的数据类型，CharField是字符型
	CharField的mac_length参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
	Django 内置的全部类型可以查看文档:
	https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
	"""
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Post(models.Model):
	# 文章标题
	title = models.CharField(max_length=70)

	# 文章正文
	# TextField存储大端文本，无长度限制
	body = models.TextField()

	# 创建时间和最近一次的修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	# 文章摘要 blank=True 代表摘要可以为空，CharField默认不允许为空
	excerpt = models.CharField(max_length=200, blank=True)

	# 关联分类与标签
	# 我们规定一篇文章只对应一个分类，一个分类底下可以有多篇文章，所以使用 ForeignKey 表明一对多的关系
	# 一篇文章对应多个标签， 一个标签底下也可以有多篇文章，使用ManyToManyField 表明多对多的关系
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)

	# 文章作者，由内置应用导入 django.contrib.auth.models import User
	author = models.ForeignKey(User)

	def __self__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk': self.pk})




