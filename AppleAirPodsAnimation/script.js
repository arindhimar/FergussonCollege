var images = [];
var loadedImages = 0;
var totalImages = 64; //med are only
var currentFrameIndex = 0;

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");


window.onload = () => {
    resizeCanvas();
    canvas.style.background = 'transparent';//glass painting 

    for (let i = 0; i < totalImages; i++) {
        var img = new Image();
        img.src = `https://www.apple.com/105/media/us/airpods-pro/2022/d2deeb8e-83eb-48ea-9721-f567cf0fffa8/anim/hero/medium/${String(i).padStart(4,  '0')}.png`;

        img.onload = () => {
            loadedImages++;
            if (loadedImages === totalImages) {
                renderImages();
            }
        };

        images.push(img);
    }
}

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    // renderImages();
}


window.addEventListener('scroll', function () {
    var scrollTop = document.documentElement.scrollTop; // to keep track of how far we've scrolled 
    // console.log(scrollTop);
    var maxScrollTop = document.documentElement.scrollHeight - window.innerHeight;// all the say from 0 to the absolute end , scoll heigt = total height of the page , innerHeight is the visible part
    // console.log(maxScrollTop);
    
    if (maxScrollTop > 0) { // Check to prevent invalid scrollFraction
        var scrollFraction = scrollTop / maxScrollTop; //(1-0)
        //console.log(scrollFraction)
        var frameCount = totalImages;
        
        var frameIndex = Math.min(frameCount - 1, Math.floor(scrollFraction * frameCount));

        currentFrameIndex = frameIndex;

        // console.log(currentFrameIndex);
        renderImages();
    }
});

function renderImages() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(images[currentFrameIndex], 0, 0, canvas.width, canvas.height);
}

window.onresize = resizeCanvas;
