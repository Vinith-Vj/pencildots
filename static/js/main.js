const menuButton = document.getElementById('menuButton');
const closeButton = document.getElementById('closeButton');
const menu = document.getElementById('menu');
const navLinks = document.querySelectorAll('.navLink');

menuButton.addEventListener('click', () => {
  menu.classList.add('show');
  tlMenu.play()
});

closeButton.addEventListener('click', () => {
  menu.classList.remove('show');
  tlMenu.reverse()
});

navLinks.forEach(link => {
  link.addEventListener('click', () => {
      menu.classList.remove('show');  // Optional if you want to hide menu on link click
      tlMenu.reverse();
      console.log('clicked');
  });
});

var tlHeader = gsap.timeline()

tlHeader.from('.navbar img', {
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

tlMenu.from('.menu-content img', {
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



// window.addEventListener("scroll", function() {
//   const navbar = document.getElementById("navbar");
//   if (window.scrollY > 50) { // Adjust scroll value as needed
//     navbar.style.paddingTop = "30px";
//     navbar.style.backgroundColor = "#ffffff54";
//   } else {
//     navbar.style.paddingTop = "30px";
//     navbar.style.backgroundColor = "transparent"; // Or whatever the original background color is
//   }
// });

window.addEventListener("scroll", function() {
  const navbar = document.getElementById("navbar");
  const screenWidth = window.innerWidth;

  if (screenWidth > 992) { // Only apply the effect for larger screens
    if (window.scrollY > 50) {
      navbar.style.paddingTop = "5px";
      navbar.style.backgroundColor = "#ffffff54";
    } else {
      navbar.style.paddingTop = "30px";
      navbar.style.backgroundColor = "transparent"; // Or your original color
    }
  } else {
    // Reset to default styles for smaller screens if needed
    navbar.style.paddingTop = "30px";
    navbar.style.backgroundColor = "#ffffff54";
  }
});