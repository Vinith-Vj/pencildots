const menuButton = document.getElementById('menuButton');
const closeButton = document.getElementById('closeButton');
const menu = document.getElementById('menu');

menuButton.addEventListener('click', () => {
  menu.classList.add('show');
  tlMenu.play()
});

closeButton.addEventListener('click', () => {
  menu.classList.remove('show');
  tlMenu.reverse()
});


var tlHeader = gsap.timeline()

tlHeader.from('.navbar span', {
  opacity: 0,
  y: -30,
  duration: 1
})

tlHeader.from('.navbar button', {
  opacity: 0,
  y: -30,
  duration: 1
})


var tlMenu = gsap.timeline()

tlMenu.from('.menu-content h2', {
  opacity: 0,
  x: 150,
  duration: 1
})

tlMenu.from('.menu-content a', {
  duration: 0.6,
  stagger: 0.2,
  opacity: 0
})

tlMenu.from('.menu-content button', {
  opacity: 0,
  duration: 1
})

tlMenu.pause()

// var h1 = document.querySelector('.catchphrase h1')

// var catchphrase = h1.textContent

// var splittedText = catchphrase.split(" ")

// var create = ""

// splittedText.forEach(function(e) {
//     create += `<span>${e}</span>`
// })

// h1.innerHTML = create

tlHeader.from('.catchphrase h1', {
    y: 100,
    opacity: 0,
    stagger: 0.15,
    duration: 1
})