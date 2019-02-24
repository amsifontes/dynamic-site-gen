def ingest_base(base_file_path):
    base_file = open(base_file_path).read()
    return base_file

def content_insert(template, content, insert_marker="{{ content }}"):
    output = template.replace(insert_marker, content)
    return output

def main():
    import glob
    import os

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
            'title': 'Homepage' if name_only == 'index' else name_only.capitalize(), # ex. 'index'
        }

        pages.append(page)

    print('pages: ', pages)



    print("website fragments... assemble!!!")

    # ingest base template
    template = ingest_base('templates/base.html')

    # ingest dictionary for each page and assemble using metadata,
    # inserting/replacing title and content
    for page in pages:
        content = open(page['input']).read()
        full_page = content_insert(template, content)
        titled_full_page = content_insert(full_page, page['title'], insert_marker="{{ title }}")
        open(page['output'], 'w+').write(titled_full_page)


    print("fragments assembled successfully! :)")


if __name__ == '__main__':
    main()
