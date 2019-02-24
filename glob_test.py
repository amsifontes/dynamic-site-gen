import glob
import os

all_html_files = glob.glob("content/*.html")
print(all_html_files)
print("all_html_files type: ", type(all_html_files)) # list type

# file_path = "content/blog.html"
for file in all_html_files:
    file_name = os.path.basename(file)
    print(file_name)
    name_only, extension = os.path.splitext(file_name)
    print("name only:",name_only,"extension",extension)
