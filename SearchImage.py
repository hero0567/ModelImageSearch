from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

es = Elasticsearch()
ses = SignatureES(es)

result = ses.search_image('C:\\Users\\lin.xia\\Documents\\My Received Files\\215EABAA.PNG')
#metaresult = ses.es.search("215EABAA.PNG")

print(result)
#print(metaresult)