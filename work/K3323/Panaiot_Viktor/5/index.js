function triggerFadeIn(el) {
  // Пример: можно вставить анимацию, перед тем как перейти
  // Но часто проще сделать обычный переход по href
  // Здесь — просто демонстрация
  setTimeout(() => {
    window.location = el.href;
  }, 300);
}

function hoverGear() {
  let el = document.getElementById("page_text");
  el.style.transition = '0.3s';
  el.style.color = '#087bf3';
  // Дополнительно можно поменять иконку, если у вас есть
}
function unhoverGear() {
  let el = document.getElementById("page_text");
  el.style.color = '#000000';
}

function blinkArea(el) {
  el.style.transition = 'none';
  el.style.backgroundColor = '#e0e0e0';
  setTimeout(() => {
    el.style.backgroundColor = 'transparent';
    // Переход на страницу
    window.location = el.href;
  }, 300);
}
