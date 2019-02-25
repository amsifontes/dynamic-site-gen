import glob
import os
from jinja2 import Template


def discover_pages():
    print('compiling pages list...')
    pages = []
    all_content_docs = glob.glob("content/*.html") # returns list of filepaths
    for doc in all_content_docs:
        # create dictionary with input filepath, output filepath, and title

        # define output directory path and filename to be appended for each doc
        output_directory_path = 'docs/'
        file_name = os.path.basename(doc)

        # remove extension to use filename as page title
        name_only, extension = os.path.splitext(file_name)
        print("name only:",name_only,"extension",extension)

        page = {
            'input': doc, # ex. 'content/index.html'
            'output': output_directory_path + file_name , # ex. 'docs/index.html'
            'file_name': file_name, # ex. index.html
            'title': 'Homepage' if name_only == 'index' else name_only.capitalize(), # ex. 'Index'
        }

        pages.append(page)

    print('pages list complete.')
    print('pages: ', pages)

    print('moving index to front of list...')

    # find index of dict object in list for Homepage and assign to var idx
    for page in pages:
        if page['file_name'] == 'index.html':
            idx = pages.index(page)

    # pop Homepage dict object from list by index and insert at front of list
    pages.insert(0,pages.pop(idx))
    print('Homepage at index 0')
    print('Returning pages list of dicts')
    return pages


def render_pages(pages):
    print('ingesting base template...')

    # ingest base template
    template_html = open('templates/base.html').read()
    template = Template(template_html)

    # iterate through dictionary for each page and assemble using Jinja,
    # inserting/replacing title and content
    print('rendering templates with context...')

    for page in pages:
        html_output = template.render(
            title=page['title'],
            content=open(page['input']).read(),
            pages=pages
        )
        open(page['output'],'w+').write(html_output)


    print("fragments assembled successfully! :)")


def new_page(filename='helloworld.html'):
    f = open(filename,'w+')

    message = """
        <!DOCTYPE html><html lang="en">
        <head><title>Page Title</title></head>
        <body>
        <h1>Content Title</h1>
        <hr />
        <p>Some sweet, sweet new content...</p>
        </html>
        """



    f.write(message)
    f.close()
