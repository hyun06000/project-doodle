var timerLine = document.getElementById("Timer");
var canvas = document.getElementById("mouseDraw");
var ctx = canvas.getContext("2d");

var X = 0;
var Y = 0;
var drag = false;

var inGame = true;
var timeout = 60;
var timeIntervalMs = 100;
var sec = "";


function mOn(mEvent) {
    X = mEvent.offsetX;
    Y = mEvent.offsetY;
    drag = true;    
}

function mMove(mEvent) {
    if (!inGame) {
        return;
    }
    if(!drag) {
        return;
    }

    var nowX = mEvent.offsetX;
    var nowY = mEvent.offsetY;

    canvasDraw(nowX, nowY);

    X = nowX;
    Y = nowY;
}

function canvasDraw(nowX, nowY) {
    ctx.beginPath();
    ctx.moveTo(X, Y);
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}

function mOff(mEvent) {
    drag = false;
}

function mOut(mEvent) {
    drag = false
}

canvas.addEventListener("mousedown",   mOn);
canvas.addEventListener("mousemove", mMove);
canvas.addEventListener("mouseup",  mOff);
canvas.addEventListener("mouseout",  mOut);

// setInterval(함수, ms주기) : 주기적인 실행
function timer() {
    sec = timeout%60;
    timerLine.innerHTML = sec+"초 남았어";
    timeout--;
    if (timeout < 10) {
        timerLine.innerHTML += " 서둘러라"
    }

    if (timeout < 0) {
        inGame = false;
        timerLine.innerHTML = "끝!";
        uploadFile()
        clearInterval(interval);
    }
}
var interval = setInterval(timer, timeIntervalMs);


function uploadFile(){
    var filename = "image_draw.png"
    var filedata = canvas.toDataURL().split("base64,")[1];
    if(filedata){
        var xhr = new XMLHttpRequest();
        var url = "/upload64";
        xhr.open("POST", url, true);
        xhr.responseType = "json";
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var result = document.getElementById("result");
                result.innerHTML = "이거 분명히 " + xhr.response.inference + "임 ㅇㅈ?"
            }
        };
        var dict = {filename:filename, filedata:filedata};
        var formdata = JSON.stringify(dict);
        xhr.send(formdata);
        }
}
