from bs4 import BeautifulSoup
import os
from pyfzf.pyfzf import FzfPrompt

nameserv = ['3D Printing', 'Academia', 'Amateur Radio', 'Android Enthusiasts', 'Anime & Manga', 'Arduino', 'Area51', 'Arqade', 'Artifical Intelligence', 'Arts & Crafts', 'Ask Different', 'Ask Patents', 'Ask Ubuntu', 'Astronomy', 'Aviation', 'Beer, Wine & Spirits', 'Biblical Hermeneutics', 'Bicycles', 'Bioinformatics', 'Biology', 'Bitcoin', 'Blender', 'Board & Card Games', 'Bricks', 'Buddhism', 'Cardano', 'Chemistry', 'Chess', 'Chinese Language', 'Christianity', 'CiviCRM', 'Code Golf', 'Code Review', 'Coffee', 'Community Building', 'Computational Science', 'Computer Graphics', 'Computer Science Educators', 'Computer Science', 'Constructed Languages', 'Craft CMS', 'Cross Validated', 'Crypthography', 'Data Science', 'Database Administrators', 'DevOps', 'Drones and Models Aircraft', 'Drupal Answers', 'Earth Science', 'Ebooks', 'Economics', 'Electrical Engineering', 'elementary OS', 'emacs', 'Engineering', 'English Language & Usage', 'English Language Learners'

stacklink = "https://ru.stackoverflow.com"

fzf = FzfPrompt()
global num
global lnk

quesd = []
linkd = []

os.system("curl {stacklink} > .tmp/stack.html")
html_main = open('stack.html', 'r')
bs = BeautifulSoup(html_main, features='lxml')
names = bs.find_all('div', class_='summary')
for name in names:
    for a in bs.find_all('a', class_="question-hyperlink"):
        link = a['href']
        if link not in linkd:
            linkd.append(link)
        text = a.find(text=True)
        if text not in quesd:
            quesd.append(text)

selt = fzf.prompt(quesd)
nselt = selt[0]
num = sel.index(nselt)
gorun = linkd[num]
print(f"\n\nGo to: {stacklink}{gorun}")
