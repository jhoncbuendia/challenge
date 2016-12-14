import sqlite3
from service import Service
import sys, os

class DataModel:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(BASE_DIR)

        self.conn = sqlite3.connect('db/ebay_data.db')
        self.cursor = self.conn.cursor()




    def drop_categories_table(self):
        try:
            # Drop table
            self.cursor.execute('DROP TABLE categories;')

        except:
            pass
    #end drop_cateogires_table

    def create_categories_table(self):
        # Create table
        self.cursor.execute('''CREATE TABLE categories
             (category_name text, category_parent_id integer, category_id integer, category_level integer)''')
    #end create_catgories_table


    def insert_cateogories(self, categories):
        for c in categories:
            # Insert a row of data
            query = "INSERT INTO categories VALUES ('{CategoryName}', {CategoryParentID} , {CategoryID}, {CategoryLevel})".format(CategoryName = c['CategoryName'], CategoryParentID = c['CategoryParentID'] , CategoryID = c['CategoryID'], CategoryLevel = c['CategoryLevel'])
            self.cursor.execute(query)

        # Save (commit) the changes
        self.conn.commit()

    def get_categories(self):
        categories_dic = []
        for row in self.cursor.execute('SELECT category_name, category_parent_id, category_id, category_level   FROM categories'):
            category = {}
            category['CategoryName'] = row[0]
            category['CategoryParentID'] = row[1]
            category['CategoryID'] = row[2]
            category['CategoryLevel'] = row[3]
            categories_dic.append(category)

        return categories_dic

    def get_categories_by_parent(self, parent_id):
        response = {}

        for row in self.cursor.execute("SELECT category_name, category_parent_id, category_id, category_level   FROM categories where category_id =" + str(parent_id)):
            parent = {}
            parent['CategoryName'] = row[0]
            parent['CategoryParentID'] = row[1]
            parent['CategoryID'] = row[2]
            parent['CategoryLevel'] = row[3]

        response['parent'] = parent

        categories_dic = []
        for row in self.cursor.execute("SELECT category_name, category_parent_id, category_id, category_level   FROM categories where category_parent_id =" + str(parent_id)):
            category = {}
            category['CategoryName'] = row[0]
            category['CategoryParentID'] = row[1]
            category['CategoryID'] = row[2]
            category['CategoryLevel'] = row[3]
            categories_dic.append(category)

        response['childs'] = categories_dic

        return response
