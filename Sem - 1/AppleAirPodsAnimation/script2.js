var images = [];
var loadedImages = 0;
var totalImages = 64; //med are only
var currentFrameIndex = 0;

var imgElement = document.getElementById("myImage");

window.onload = () => {
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

window.addEventListener('scroll', function () {
    var scrollTop = document.documentElement.scrollTop; 
    var maxScrollTop = document.documentElement.scrollHeight - window.innerHeight; 
    if (maxScrollTop > 0) { 
        var scrollFraction = scrollTop / maxScrollTop; 
        var frameCount = totalImages;
        var frameIndex = Math.min(frameCount - 1, Math.floor(scrollFraction * frameCount));

        currentFrameIndex = frameIndex;

        renderImages();
    }
});

function renderImages() {
    imgElement.src = images[currentFrameIndex].src;
}

window.onresize = function() {
    
}