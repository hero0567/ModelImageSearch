from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

es = Elasticsearch()
ses = SignatureES(es)

#ses.add_image('images2/001.jpg', metadata='001')
ses.add_image('C:\\Users\\lin.xia\\Documents\\My Received Files\\215EABAA.PNG')
# ses.add_image('images/001.jpg')
# ses.add_image('images/002.jpg')
# ses.add_image('images/003.jpg')
#ses.add_image('images/004.jpg')
#ses.add_image('images/001.jpg', metadata={'catagory': 'desk'})

# result = ses.search_image('images/002.jpg')
# print(result)