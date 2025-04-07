function hoverGear() {
  let el = document.getElementById("page_text");
  el.style.transition = '0.3s';
  el.style.color = '#087bf3';
}
function unhoverGear() {
  let el = document.getElementById("page_text");
  el.style.color = '#000000';
}

function toggleImage() {
  var img = document.getElementById("toggleImage");
  if (img.style.display === "none" || img.style.display === "") {
        img.style.display = "block";
  } else {
    img.style.display = "none";
  }
}
