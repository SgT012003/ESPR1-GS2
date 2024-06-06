import { } from 'react';
import '../css/style.scss';
import '../css/roots.scss';



function Footer() {

// Get the button:
let mybutton = document.querySelector("#scrlBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTo({ top: 0, behavior: 'smooth' });
  document.documentElement.scrollTo({ top: 0, behavior: 'smooth' })
  
}
  return (
    <>
    <button onClick={topFunction} id="scrlBtn" title="Go to top">A</button>
    <section className='content display-center'>
      <h5 className='white'>@2024-todos os direitos reservados.</h5>
      </section>
    </>
  );
}
export default Footer;
