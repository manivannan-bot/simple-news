function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}


function tmClick() {
   document.getElementById('eng-list').style.display = 'none'
   document.getElementById('tm-list').style.display = 'block'

  document.getElementById('tm-button').style.background = 'white'
  document.getElementById('tm-button').style.color = 'black'

  document.getElementById('en-button').style.background = 'black'
  document.getElementById('en-button').style.color = 'white'


}
function engClick() {
  document.getElementById('tm-list').style.display = 'none'
  document.getElementById('eng-list').style.display = 'block'

  document.getElementById('en-button').style.background = 'white'
  document.getElementById('en-button').style.color = 'black'

  document.getElementById('tm-button').style.background = 'black'
  document.getElementById('tm-button').style.color = 'white'
}

// Get the button
let mybutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

if (window.location.pathname.startsWith('/en/') || window.location.pathname.startsWith('/en')) {

  document.getElementById('eng-list').style.display = 'block'
  document.getElementById('tm-list').style.display = 'none'

  document.getElementById('en-button').style.background = 'white';
  document.getElementById('en-button').style.color = 'black';
}
if (window.location.pathname.startsWith('/tamil/') || window.location.pathname.startsWith('/tamil')) {

  document.getElementById('eng-list').style.display = 'none'
  document.getElementById('tm-list').style.display = 'block'

  document.getElementById('tm-button').style.background = 'white'
  document.getElementById('tm-button').style.color = 'black'
}


// if (window.location.pathname.startsWith('/tamil/politics')) {
//   document.getElementById('tm-button').style.background = 'white'
//   document.getElementById('tm-button').style.color = 'black'
//   var route = '/tamil/politics'
//   var targetLink = document.querySelector('a[href="' + route + '"]');

//   // Change the background color to white and text color to black
//   targetLink.style.backgroundColor = 'white';
//   targetLink.style.color = 'black';
// }



function changeStyles(routes) {
  var links = document.querySelectorAll('a');
  var currentRoute = window.location.pathname;

  links.forEach(function (link) {
    var href = link.getAttribute('href');
    if (link.closest('.lang-list') && routes.some(function (route) { return currentRoute.startsWith(route); }) && currentRoute === href) {
      link.style.backgroundColor = 'white';
      link.style.color = 'black';
    }
  });
}

var routes = ["/tamil",
  "/tamil/top",
  "/tamil/india",
  "/tamil/world",
  "/tamil/politics",
  "/tamil/business",
  "/tamil/tech",
  "/tamil/sports",
  "/tamil/entertainment", "/",
  "/en/top",
  "/en/india",
  "/en/world",
  "/en/politics",
  "/en/business",
  "/en/tech",
  "/en/sports",
  "/en/entertainment"]

changeStyles(routes)



function toggleDropdown(button) {
  var dropdown = button.nextElementSibling;
  dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

// function copyLink() {
//   var linkToCopy = document.getElementById('hidden-source').innerText;
//   navigator.clipboard.writeText(linkToCopy)
//       .then(function () {
//           alert(linkToCopy+' copied!');
//       })
//       .catch(function (error) {
//           console.error("Failed to copy link: ", error);
//       });
// }


function copyLink(url) {
  // Create a temporary input element to copy the URL to clipboard
  var tempInput = document.createElement('input');
  tempInput.setAttribute('value', url);
  document.body.appendChild(tempInput);

  // Copy the URL from the input element
  tempInput.select();
  document.execCommand('copy');

  // Remove the temporary input element
  document.body.removeChild(tempInput);

  // Show a notification or do any other action after copying (optional)
  alert('Link copied : '+url);
}

