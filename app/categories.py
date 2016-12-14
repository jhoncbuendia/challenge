#!/usr/bin/python
from libraries.data_model import DataModel
from libraries.html_generator import HtmlGenerator
from libraries.service import Service
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "rebuild", "render_all", "render="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            sys.exit()

        elif o in ("-rb", "--rebuild"):
            service = Service()
            categories = service.get_categories()
            data_model = DataModel()
            data_model.drop_categories_table()
            data_model.create_categories_table()
            data_model.insert_cateogories(categories)
            print 'rebuild completed'

        elif o in ("-rea", "--render_all"):
            generator = HtmlGenerator()
            generator.render_all_categories()
            print 'all categories rendered in html_generated/all_categories.html file'

        elif o in ("-re", "--render"):
            #category id 1281
            output = a
            generator = HtmlGenerator()
            generator.render_single_categorie(str(output))
            print 'all categories rendered in html_generated/'+ str(output) +'.html file'
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()
