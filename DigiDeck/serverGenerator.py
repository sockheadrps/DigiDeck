import os

file = open('server.py', 'w+')
file.write('from playsound import playsound')
file.write('\nimport hug')
file.write('\n')
file.write("\n@hug.static('/static')")
file.write('\ndef my_static_dirs():')
file.write('\n\treturn "."')
file.write('\n')
file.write('\n')


file.write("\n@hug.static('/endpoints')")
file.write('\ndef sound_endpoints():')
file.write('\n\treturn "/Sounds"')
file.write('\n')
file.write('\n')




os.chdir('Sounds')
def get_sound_file_names():
    btn_ids = []
    for filename in os.listdir():
        if filename.endswith(".mp3"):
            btn_ids.append(filename[:-4])
    return btn_ids

for bid in get_sound_file_names():
    file.write("\n@hug.get" + "('/" + bid + "')")
    file.write('\n@hug.local()')
    file.write('\ndef '+ bid + '():')
    file.write("\n\tplaysound(" + "'./Sounds/" + bid + ".mp3')")
    file.write('\n\treturn {"played"}')
    file.write('\n')
    file.write('\n')


file.write('\n')

file.close()
