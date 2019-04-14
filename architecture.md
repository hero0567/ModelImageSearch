### Architecture

ModelImageSearch provide the feature to load disk image to database and provide Web GUI to user to query and management.

it accept a image input and search similar images from database by [phash](http://www.phash.org/). 

it also provide a admin GUI to add new images or delete images from database.

```mermaid
graph BT;
   Disk--load-->ElasticSearch
　　PythonLib(Python lib)-->Django 
　　PHash-->PythonLib(Python lib)
　　ElasticSearch-->PythonLib(Python lib)
　　WatchDog(Watch Dog)--cron job-->ElasticSearch
　　WatchDog(Watch Dog)--cron job-->Django
　　Django-->GUI(GUI admin,query,display)
　　GUI(GUI admin,query,display)-->Input[Input image]
　　

```

