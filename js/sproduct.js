let BigImg = document.getElementById("BigImg");
let SmallImg = document.getElementsByClassName("small-img");

SmallImg[0].onclick = function () {
    BigImg.src = SmallImg[0].src;
}

SmallImg[1].onclick = function () {
    BigImg.src = SmallImg[1].src;
}
SmallImg[2].onclick = function () {
    BigImg.src = SmallImg[2].src;
}

SmallImg[3].onclick = function () {
    BigImg.src = SmallImg[3].src;
}