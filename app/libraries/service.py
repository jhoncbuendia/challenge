import requests
import untangle
from ebay_enviroment_values import EbayEnviromentValues

class Service:

    '''
    setting default values
    @param {}
    #@return {}
    '''

    def __init__(self):
        self.ebay_enviroment_values = EbayEnviromentValues()
    #end init


    '''
    Get categories list from ebay
    @param {}
    #@return {Categories} List
    '''

    def get_categories(self):

        req = requests.post(self.ebay_enviroment_values.url, data = self.ebay_enviroment_values.data, headers = self.ebay_enviroment_values.headers)
        categories__xml = untangle.parse(req.text)
        categories_dic = []

        for c in categories__xml.GetCategoriesResponse.CategoryArray.Category:
            category = {}
            category['CategoryID'] = c.CategoryID.cdata
            category['CategoryLevel'] = c.CategoryLevel.cdata
            category['CategoryName'] = c.CategoryName.cdata
            category['CategoryParentID'] = c.CategoryParentID.cdata
            categories_dic.append(category)
        return categories_dic
        #end get_categories
