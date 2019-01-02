# my_postapi

# API使用方法

1、linux下curl：
curl http://192.168.1.193:8000/send/email -X POST --header '{'content-type': 'application/json'}' --data '{"data": [{"subject": "testsubject"}, {"context": "testcontext"}, {"tomail": "xxx@qq.com"}]}'

2、Python:

![](https://raw.githubusercontent.com/opser-gavin/my_postapi/master/others/my_postapi.png)