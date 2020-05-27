# -*- coding: UTF-8 -*-

import os, re, codecs

template = '''# Links

{LINKS}
---

[MarkdownPlayer](https://github.com/Supegg/MarkdownPlayer)
'''

links = str()

for root, dirs, files in os.walk("."):
    for name in files:
        if re.match(r".*\.md", name):
            link = os.path.join(root, name)[2:].replace('\\', '/')
            links += f"* [{link}](markdown.html?md={link})\n"
            #print(os.path.join(root, name)[2:])

#print(links)
print(template.replace("{LINKS}", links))

# write 2 index.md
#f = open("index.md", 'w', 'utf8')
f = codecs.open("index.md", 'w', 'utf8')
f.write(template.replace("{LINKS}", links))
f.flush()
f.close()
