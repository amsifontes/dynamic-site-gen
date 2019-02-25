import sys
import utils


def main():

    try:
        argument = sys.argv[1]

        if argument == 'build':
            pages = utils.discover_pages()
            utils.render_pages(pages)

            print('All done...Enjoy!!!')
        elif argument == 'new':
            print('add new page functionality here.')
            try:
                utils.new_page(filename= sys.argv[2])
            except:
                utils.new_page()
        elif argument == 'help':
            print("""
            Example commands:
                Rebuild site:    python manage.py build
                Create new page: python manage.py new
                """)
        else:
            print("Hmm... I don't recognize that argument. Please specify 'build' or 'new'")

    except:
        print("""
        Usage:
            Rebuild site:    python manage.py build
            Create new page: python manage.py new
            """)

if __name__ == '__main__':
    main()
