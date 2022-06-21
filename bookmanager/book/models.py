from django.db import models

"""
docs.djangoproject.com/en/3.1
1. 模型类需要继承自models.Model
2. 系统自动为我们添加一个主键---id
3. 字段
    字段名=models.类型（选项）
    字段名其实就是数据表的字段名
    字段名不要使用python， mysql等的关键字
    字段名不要使用连续下划线（__）
4. 类型 MySQL的类型
5. 选项 是否有默认值， 是否唯一， 是否允许为Null
    CharField 必须设置 max_length
    verbose_name 主要是admin站点使用
6. 改变表的名称
    默认表的名称是： 子应用名_类名 都是小写
    修改表的名字
"""


class BookInfo(models.Model):

    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字
        verbose_name = '书籍管理'  # admin站点使用的

    # 重写str方法， 以显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键  系统会自动为外键添加 _id
    # 外键的级联操作 on_delete
    #     CASCADE 级联， 删除主表数据时连同一起删除外键表中的数据
    #     PROTECT 保护， 通过抛出ProtectedError异常， 来阻止删除主表中被外键应用的数据
    #     SET_NULL 设置为NULL， 仅在该字段null=True时可用
    #     SET_DEFAULT 设置为默认值， 仅在该字段设置了默认值时可用
    #     SET() 设置为特定值或者特定方法
    #     DO_NOTHING 不做任何操作， 如果数据库前置指明级联性， 此选项会抛出IntegrityError异常
    # 主表和从表
    # 1 对 多
    # 书籍  对 人物
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
