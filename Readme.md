
# Web 开发 9：Django 框架基础

在本篇文章中，我们将深入探讨 Django 框架的基础知识。Django 是一个功能强大且流行的 Python Web 框架，它提供了一套完整的工具和功能，用于开发高效、可扩展的 Web 应用程序。

## 什么是 Django？

Django 是一个基于 Python 的免费开源 Web 框架，由一群富有经验的开发者创建和维护。它遵循了 MVC（模型-视图-控制器）的软件设计模式，旨在帮助开发人员快速构建复杂的 Web 应用程序。

## Django 的特性

Django 框架具有许多强大的特性，使其成为 Web 开发的首选框架之一：

- **强大的 ORM（对象关系映射）**：Django 提供了一个简单而强大的 ORM，使开发人员可以使用 Python 代码来操作数据库，而无需直接编写 SQL 查询语句。

- **自动化的管理界面**：Django 自动生成管理界面，使开发人员可以轻松管理数据库记录和模型。

- **灵活的 URL 配置**：Django 的 URL 配置非常灵活，可以根据需要定义各种 URL 模式，并将它们映射到相应的视图函数。

- **模板引擎**：Django 提供了内置的模板引擎，使开发人员可以将业务逻辑和显示逻辑分离，实现更好的代码组织和可维护性。

- **强大的表单处理**：Django 的表单处理功能简单易用，可以轻松处理表单验证、数据存储等任务。

## 安装 Django

在开始使用 Django 之前，我们需要先安装它。可以使用以下命令来安装 Django：

```bash
pip install django
```

确保您已经安装了适当版本的 Python，并且已经配置了正确的环境变量。

## 创建 Django 项目

在安装 Django 后，我们可以通过以下命令来创建一个新的 Django 项目：

```bash
django-admin startproject myproject
```

这将创建一个名为 "myproject" 的新目录，其中包含 Django 项目的基本结构和配置文件。

## 运行 Django 开发服务器

在项目目录下，我们可以使用以下命令来启动 Django 开发服务器：

```bash
python manage.py runserver
```

这将启动开发服务器，并将您的 Django 应用程序运行在本地主机的默认端口上（通常是 8000）。

## 创建 Django 应用程序

在 Django 中，应用程序是组织代码的基本单元。可以使用以下命令来创建一个新的 Django 应用程序：

```bash
python manage.py startapp myapp
```

这将创建一个名为 "myapp" 的新目录，其中包含 Django 应用程序的代码文件。

## 编写视图函数

在 Django 中，视图函数负责处理用户的请求，并返回相应的响应。可以在应用程序的 views.py 文件中编写视图函数。

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!")
```

在上面的示例中，我们定义了一个名为 "hello" 的视图函数，它接受一个请求对象作为参数，并返回一个包含 "Hello, Django!" 的 HTTP 响应。

## 配置 URL 映射

要将视图函数与特定的 URL 进行映射，我们需要在应用程序的 urls.py 文件中进行配置。

```python
from django.urls import path
from .views import hello

urlpatterns = [
    path('hello/', hello),
]
```

在上述示例中，我们将 "/hello/" URL 映射到了之前定义的 "hello" 视图函数。

## 运行 Django 服务器

现在，我们已经完成了 Django 项目的基本配置和代码编写。可以使用以下命令来启动 Django 开发服务器：

```bash
python manage.py runserver
```

在浏览器中访问 http://localhost:8000/hello/，您将看到 "Hello, Django!" 的响应。


## 一个例子
我们将创建一个名为 "todo" 的 Django 项目，用于构建一个简单的待办事项应用程序。

1. 在 "tasks.py" 文件中，编写您的视图函数。可以编写一个简单的视图函数来显示待办事项列表：

```python
from django.shortcuts import render

def task_list(request):
    tasks = ['Task 1', 'Task 2', 'Task 3']
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
```


2. 在 "urls.py" 文件中，将以下代码添加到 "urlpatterns" 列表中：

```python
from django.urls import path
from .tasks import task_list

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
]
```

这是将 "/tasks/" URL 映射到之前定义的 "task_list" 视图函数。

3. 在终端窗口中，输入以下命令来启动 Django 开发服务器：

```bash
python manage.py runserver
```

开发服务器将在本地主机的默认端口（通常是 8000）上运行。

4. 在浏览器中访问 http://localhost:8000/tasks/，您将看到待办事项列表。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3c7d12b14dc341f781bbd1ee0693f3cc.png)


[]()

## 结语

在本篇文章中，我们介绍了 Django 框架的基础知识。我们了解了 Django 的特性、安装过程、项目和应用程序的创建，以及视图函数和 URL 映射的配置。希望这篇文章能够帮助您入门 Django 开发，并为您构建高效、可扩展的 Web 应用程序提供指导。

如果您对 Django 框架有更多的兴趣和需求，可以继续学习 Django 的高级特性，如模型定义、表单处理、用户认证等。

感谢阅读！

参考链接：

- [Django 官方网站](https://www.djangoproject.com/)
- [Django 文档](https://docs.djangoproject.com/)
