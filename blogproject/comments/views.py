# -*-# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)

	# HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
	if request.method == 'POST':
		# 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了
		form = CommentForm(request.POST)

		# 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
		if form.is_valid():
			# 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
		else:
			comment_list = post.comment_set.all()
			context = {'post':post, 'form':form, 'comment_list':comment_list}
			return render(request, 'blog/detail.html', context=context)

	return redirect(post)

    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    # redirect 它的作用是对 HTTP 请求进行重定向（即用户访问的是某个 URL，但由于某些原因，服务器会将用户重定向到另外的 URL
    # redirect 既可以接收一个 URL 作为参数，也可以接收一个模型的实例作为参数（例如这里的 post）。
    # 如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url 方法，这样 redirect 会根据 get_absolute_url 方法返回的 URL 值进行重定向。





