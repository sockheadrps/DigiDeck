import socket
import os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

file = open('xhr.js', 'w+')
file.write('let btns = document.getElementsByClassName("button");')
file.write('\n')
file.write('\nfor (var i=0; i < btns.length; i++){')
file.write('\n\tlet btn = btns[i]')
file.write("\n\tlet func = () => {")
file.write('\n\t\tlet xhr = new XMLHttpRequest();')
file.write('\n\t\txhr.open("GET", ' + f"`http://{IPAddr}:8000" + "/${btn.id}`)")
file.write('\n\t\txhr.onload = () => {')
file.write('\n\t\t\tif(xhr.status == 200)')
file.write('\n\t\t\t\tconsole.log(xhr.responseText);')
file.write('\n\t\t\telse')
file.write('\n\t\t\t\tconsole.log(xhr.statusText);')
file.write('\n\t\t}')
file.write('\n\t\txhr.send();')
file.write("\n\t}")
file.write("\n\tbtns[i].addEventListener('click', func);")
file.write('\n}')


print("#############")
print("#############")
print("#############")
print("#############")
print("Connect to wifi on your device and enter: http://" + IPAddr + ":8000/static")
print("When you have copied the address, press any key while in this window to continue and run the server. Navigate "
      "to the provided address on your device AFTER the server has loaded. Terminate the server by closing "
      "command prompt or pressing ctrl+c")
print("#############")
print("#############")
print("#############")
print("#############")

