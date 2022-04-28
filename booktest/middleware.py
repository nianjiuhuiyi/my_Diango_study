from django.http import HttpResponse

"""这是老版本1.8的写法了"""
# class BlockIpMiddleware(object):
#     BLOCK_IPS = ["192.168.108.218"]
#     # 这个函数名字一定要是这样的
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         user_ip = request.META["REMOTE_ADDR"]
#         if user_ip in BlockIpMiddleware.BLOCK_IPS:
#             return HttpResponse("403 Forbidden\r\n")


from django.http import HttpResponseForbidden


# 第一种写法
# class BlockIpMiddleware(object):
#     BLOCK_IPS = ["192.168.2.125"]
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         return self.get_response(request)
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         user_ip = request.META["REMOTE_ADDR"]
#         if user_ip in BlockIpMiddleware.BLOCK_IPS:
#             # return HttpResponse("403 Forbidden\r\n")
#             return HttpResponseForbidden("403 Forbidden\r\n")  # 两个是一样的


# 第二种写法
class BlockIpMiddleware(object):
    BLOCK_IPS = ["192.168.2.125"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META["REMOTE_ADDR"]
        if user_ip in BlockIpMiddleware.BLOCK_IPS:
            return HttpResponseForbidden("403 Forbidden\r\n")

        response = self.get_response(request)
        return response
