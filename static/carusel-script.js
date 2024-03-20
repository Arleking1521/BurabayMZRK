let slideIndex = 0;
const slides = document.querySelectorAll('.mySlides');
const totalSlides = slides.length;
let autoSlideInterval;

function showSlide(index) {
  slides.forEach(slide => {
    slide.style.display = 'none';
  });
  slides[index].style.display = 'block';
}

function currentSlide(n) {
  showSlide(slideIndex = n);
}


function nextSlide() {

  slides[slideIndex].style.animation = 'slideOutLeft 0.5s ease';
  setTimeout(() => {
    slides[slideIndex].style.display = 'none';
    slides[slideIndex].style.animation = '';
    slideIndex = (slideIndex + 1) %totalSlides;
    showSlide(slideIndex);
    slides[slideIndex].style.animation = 'slideInRight 0.5s ease';
  }, 500);
}

function prevSlide() {
  

  slides[slideIndex].style.animation = 'slideOutRight 0.5s ease';
  setTimeout(() => {
    slides[slideIndex].style.display = 'none';
    slides[slideIndex].style.animation = '';
    slideIndex = (slideIndex - 1 + totalSlides) % totalSlides ;
    showSlide(slideIndex);
    slides[slideIndex].style.animation = 'slideInLeft 0.5s ease';
  }, 500);
}

function startAutoSlide() {
  autoSlideInterval = setInterval(nextSlide, 10000);
}

function stopAutoSlide() {
  clearInterval(autoSlideInterval);
}

showSlide(slideIndex);
startAutoSlide();

const sliderContainer = document.querySelector('.slideshow-container');
sliderContainer.addEventListener('mouseenter', stopAutoSlide);
sliderContainer.addEventListener('mouseleave', startAutoSlide);

// Добавляем анимации для автоматического переключения слайдов
function autoNextSlide() {
  nextSlide();
}

function autoPrevSlide() {
  prevSlide();
}

autoSlideInterval = setInterval(autoNextSlide, 5000);
