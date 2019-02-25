pages = [
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
            'input': 'content/index.html',
            'output': 'docs/index.html',
            'title': 'Homepage',
        },
        {
            'input': 'content/projects.html',
            'output': 'docs/projects.html',
            'title': 'Projects',
        },
        ]

print(pages)

# mylist.insert(0, mylist.pop(mylist.index(targetvalue)))
# [i for i, d in enumerate(listofpeople) if "Jack" in d.keys()]

for page in pages:
    if page['input'] == 'content/index.html':
        idx = pages.index(page)


print('homepage index: ',idx)
pages.insert(0,pages.pop(idx))
print(pages)
