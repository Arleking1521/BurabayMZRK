 const swiper = new Swiper('.sw', {
    // Optional parameters
    loop: true,
    autoplay:{
        delay: 3000,
    },
  
    // If we need pagination
    pagination: {
      el: '.pag',
      clickable: true,
      type: 'bullets',
    },
});

const swiper1 = new Swiper('.sw1', {
  // Optional parameters
  loop: true,
  autoplay:{
      delay: 3000,
  },

  // If we need pagination
  pagination: {
    el: '.pag1',
    clickable: true,
    type: 'bullets',
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

function show_hide_password(target){
  var input = document.getElementById('password-input')
  var input1 = document.getElementById('password-input1')
  if(target.getAttribute('id') == 'pi'){
    if (input.getAttribute('type') == 'password') {
      target.classList.add('view');
      input.setAttribute('type', 'text');
    } else {
      target.classList.remove('view');
      input.setAttribute('type', 'password');
    }
  }
  if(target.getAttribute('id') == 'pi1'){
    if (input1.getAttribute('type') == 'password') {
      target.classList.add('view');
      input1.setAttribute('type', 'text');
    } else {
      target.classList.remove('view');
      input1.setAttribute('type', 'password');
    }
  }
  return false;
}






function show_files_name(target) {
  const selectedFilesDiv = document.getElementById('selected-files');

  const files = target.files;
  selectedFilesDiv.innerHTML = '';

  for (const file of files) {
      const fileName = file.name;
      const fileItem = document.createElement('p');
      fileItem.textContent = fileName;
      selectedFilesDiv.appendChild(fileItem);
  }
}