from django.template import Library

# 创建一个Library类的对象
register = Library()

# 自定义的过滤器函数，至少要有一个参数
@register.filter
def mod(num):
    return num % 2 == 0


# 至多两个参数
@register.filter
def mod_val(num, val):
    """判断num是否能被val整除"""
    return num % val == 0
