# ModelImageSearch

##### What is ModelImageSearch
ModelImageSearch help user find similar image that user upload by GUI from ElasticSearch.

ModelImageSearch (Python+ElasticSearch+Django)：Load images into elasticsearch. Compare with given image and find similiar images to user.

ModelImageSearch will show the similar images result to GUI. User could download it and relative 3D model.

Image search algorithm: http://phash.org/

##### ModelImageSearch setup
1. install python
2. install VS ( 4GB Space )
3. install python lib
    $ pip install numpy
    $ pip install scipy
    $ pip install image_match
4. startup elasicsearch
5. install Django


##### Django
1. run WebServer.py to startup web application.
2. change port at WebServer.py
3. access http://localhost:8000/

##### Python Log
1. please go to log.conf file to get detail information

##### How to upload image to ES search
1. unzip elasticsearch-2.2.1.zip from tool folder
2. start ES
3. copy images to "images" folder this project
4. startup web application
5. go to admin page
6. click "add image" button


##### How to manage elasticsearch?
1. go to admin page: http://localhost:9200/
2. check db status: http://localhost:9200/_cat/indices?v
3. remove all db data: curl -XDELETE 'localhost:9200/images'

##### QA
Q: 图片搜索后不显示问题
A：Django的static resource路径不对，修改settings.py里面的STATICFILES_DIRS

Q：安装image_match失败
A：安装VS
