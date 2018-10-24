# ModelImageSearch
ModelImageSearch (Python+Lucene+Django)：加载图片到Lucene，通过GUI搜索相似图片，并展示给用户

1. install python
2. install VS ( 4GB Space )
3. install python lib
    $ pip install numpy
    $ pip install scipy
    $ pip install image_match
4. startup elasicsearch
5. install Django

Q: 图片搜索后不显示问题
A：Django的static resource路径不对，修改settings.py里面的STATICFILES_DIRS

Q：安装image_match失败
A：安装VS
