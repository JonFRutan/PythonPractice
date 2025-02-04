# I found that all of the tags are kept in a structure called "InitAppTagModal"
# Originally the plan was to cut the div out (using DivCut.py), however this way may be faster.
# FIXME: THERE IS AN ISSUE GRABBING TAGS USING JUST AN ID AS THE ARGUMENT
import re, sys, HtmlGrab

if len(sys.argv) > 1:
    input_div = sys.argv[1]
else:
    input_type = input("Using URL or App ID? : (u/a) ")
    if input_type == 'u':
        url = input("Paste a URL")
    elif input_type == 'a':
        app_id = input("Enter the steam app id: ")


tag_start_pattern = r"InitAppTagModal"

with open(input_div, "r") as file:
    div_contents = file.read().split("\n")

line_count = 0
for line in div_contents:
    line_count += 1
    if re.search(tag_start_pattern, line):
        # Interestingly, all tags are kept on a single line.
        tags = div_contents[line_count].split("},{")
        #print(f"Tags found at line {line_count+1}")    

tag_count = len(tags)
# Clean up the first tag...
tags[0] = tags[0].strip()
tags[0] = tags[0][2:]
# Clean up the last tag...
tags[tag_count-1] = tags[tag_count-1][:len(tags[tag_count-1])-3]

print(f"{tag_count} tags found on line {line_count+1}")
for line in tags:
    print(line)
