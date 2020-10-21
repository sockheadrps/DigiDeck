let btns = document.getElementsByClassName("button");

for (var i=0; i < btns.length; i++){
    let btn = btns[i]
    let func = () => {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", `http://192.168.1.154:8000/${btn.id}`);
        xhr.onload = () => {
            if(xhr.status == 200)
                console.log(xhr.responseText);
            else
                console.log(xhr.statusText);
        }
        xhr.send();
    }
    btns[i].addEventListener('click', func);
}
