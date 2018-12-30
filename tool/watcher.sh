ps -fe|grep WebServer.py |grep -v grep
if [ $? -ne 0 ]
then
	image=`grep -rn 'AddImage - INFO - Add image' /root/ModelImageSearch/app.log| tail -1 | awk -F "Add image " '{print $2}'`
	if [[ $image != "" ]]
	then
	  echo $image > /root/ModelImageSearch/last
	fi
    echo "`date` restart python....." >> ~/watcher.log
	cd /root/ModelImageSearch
	python3 WebServer.py &
else
    echo "`date` python runing....." >> ~/watcher.log
fi

ps -fe|grep org.elasticsearch.bootstrap.Elasticsearch |grep -v grep
if [ $? -ne 0 ]
then
    echo "`date` restart elasticsearch....." >> ~/watcher.log
	sh /root/ModelImageSearch/tool/elasticsearch-2.2.1/bin/elasticsearch  &
else
    echo "`date` elasticsearch runing....." >> ~/watcher.log
fi


