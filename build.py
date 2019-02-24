def ingest_base(base_file_path):
    base_file = open(base_file_path).read()
    return base_file

def content_insert(template, content, insert_marker="{{ content }}"):
    output = template.replace(insert_marker, content)
    return output

def main():
    pages = [
        {
            'input': 'content/index.html',
            'output': 'docs/index.html',
            'title': 'Homepage',
        },
        {
            'input': 'content/bio.html',
            'output': 'docs/bio.html',
            'title': 'Bio',
        },
        {
            'input': 'content/blog.html',
            'output': 'docs/blog.html',
            'title': 'Blog',
        },
        {
            'input': 'content/projects.html',
            'output': 'docs/projects.html',
            'title': 'Projects',
        },
        ]

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
