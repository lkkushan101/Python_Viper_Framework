from ReusableRequest import Request_Post
from Utility.ReadExcel import readExcel
import unittest
import json
class Post_Test(unittest.TestCase):

        post_req = Request_Post
        response = post_req.send_post_request(readExcel('../Data/data_webservices.xlsx','Sheet1','B3'), json.loads(readExcel('../Data/data_webservices.xlsx','Sheet1','C3')))
        print(response.status_code)
        assert response.status_code == 200
