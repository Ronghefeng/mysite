
# 部署 django 项目
## uWSGI 启动服务器
uwsgi --http :8000 --module mysite.wsgi   
### uWSGI + Nginx 部署参考
https://pythondjango.cn/python/tools/6-uwsgi-configuration/

## Gunicorn 启动服务
gunicorn mysite.wsgi

### Gunicorn + Nginx 部署参考链接
https://docs.gunicorn.org/en/latest/deploy.html
