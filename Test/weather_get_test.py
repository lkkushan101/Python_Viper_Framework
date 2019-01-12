from ReusableRequest import Request_Get
from Utility.ReadExcel import readExcel

import unittest

class Get_Test(unittest.TestCase):
    get_req = Request_Get
    response = get_req.send_get_request(readExcel('../Data/data_webservices.xlsx','Sheet1','B2'))

    assert response['City'] == readExcel('../Data/data_webservices.xlsx','Sheet1','D2')
    assert response['Humidity'] == readExcel('../Data/data_webservices.xlsx','Sheet1','E2')

