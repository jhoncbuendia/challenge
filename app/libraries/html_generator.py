#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from service import Service
from data_model import DataModel
import json
import sys, os

class HtmlGenerator:
    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(BASE_DIR)

        self.data_model = DataModel()


    def render_all_categories(self):

        tree = []
        for c in self.data_model.get_categories():
            element = {}
            element['text'] = c['CategoryName']
            tree.append(element)

        self.render_template(json.dumps(tree), 'all_categories')


    def render_single_categorie(self, parent_id):
        data = self.data_model.get_categories_by_parent(parent_id)
        tree = []
        element = {}
        element['text'] = data['parent']['CategoryName']

        element['nodes'] = []
        for i in data['childs']:
            n_element = {}
            n_element['text'] = i['CategoryName']
            element['nodes'].append(n_element)
        tree.append(element)

        self.render_template(json.dumps(tree), str(parent_id))

    def render_template(self, tree, file_name):


        js_script = "$('.tree-container').treeview({data:" + tree + "});"

        template = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="utf-8">
              <meta http-equiv="X-UA-Compatible" content="IE=edge">
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
              <title>Ebay Categories</title>

              <!-- Latest compiled and minified CSS -->
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
              <link rel="stylesheet" href="./css/bootstrap-treeview.min.css" media="screen" title="no title">
            </head>

            <body>
              <nav class="navbar navbar-static-top navbar-dark bg-inverse">
                <a class="navbar-brand" href="#">Ebay Cateogries Render</a>
              </nav>

              <!-- Main jumbotron for a primary marketing message or call to action -->
              <div class="jumbotron">
                <div class="container">
                  <h1 class="display-3">Render Ebay Categories Project</h1>
                  <p>With this project you will be able to  download and render all ebay categories on bottom side of this page.</p>
                  <p><a class="btn btn-primary btn-lg" href="#" role="button">Go to github repositorie »</a></p>
                </div>
              </div>

              <div class="container">
                <!-- Example row of columns -->
                <div class="row">
                  <div class="col-md-12">
                    <div class="tree-container">

                    </div>
                  </div>
                </div>

                <hr>

                <footer>
                  <p>© Company 2016</p>
                </footer>
              </div> <!-- /container -->

              <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
              <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
              <!-- Include all compiled plugins (below), or include individual files as needed -->
              <!-- Latest compiled and minified JavaScript -->
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
              <script src="./js/bootstrap-treeview.min.js" charset="utf-8"></script>
              <script type="text/javascript">
                {js_script}
              </script>
            </body>
            </html>
        '''.format(js_script = js_script)

        file = open("html_generated/"+ file_name + ".html", "w")
        file.write(template)

        file.close()

        return template
