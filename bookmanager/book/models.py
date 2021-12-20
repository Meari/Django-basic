from django.db import models

"""
1. 模型类需要继承自models.Model
2. 系统自动为我们添加一个主键---id
3. 字段
    字段名=models.类型（选项）
    字段名其实就是数据表的字段名
    字段名不要使用python， mysql等的关键字
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    # 重写str方法， 以显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
