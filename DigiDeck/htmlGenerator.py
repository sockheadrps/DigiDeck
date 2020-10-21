from yattag import Doc, indent
import os


doc, tag, text, line = Doc().ttl()
os.chdir('Sounds')


def get_sound_file_names():
    btn_ids = []
    for filename in os.listdir():
        if filename.endswith(".mp3"):
            btn_ids.append(filename[:-4])
    return btn_ids



btn_ids = get_sound_file_names()
doc.asis('<!DOCTYPE html>')
with tag('html', lang='en'):
    with tag('head'):
        doc.asis('<link rel="stylesheet" href="/static/app.css">')
        doc.asis('<meta charset="UTF-8">')
        doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        doc.asis('<meta http-equiv="X-UA-Compatible" content="ie=edge">')
        doc.asis('<script src="/static/xhr.js" defer></script>')

    with tag('body'):
        with tag('section', id='control-center'):
            for bid in btn_ids:
                line('button', bid, klass="button", id=bid)

os.chdir('..')
file = open('index.html', 'w+')
file.write(indent(doc.getvalue(), indent_text=True))
file.close()


