const navButton = document.querySelector(".navbar button");

function toggleNav({ target }) {
  const expanded = target.getAttribute("aria-expanded") === "true" || false;
  navButton.setAttribute("aria-expanded", !expanded);
}

navButton.addEventListener("click", toggleNav);

const comButton = document.querySelector(".commentTitle button");
const comForm = document.querySelector(".commentsForm");

function toggleNav2({ target }) {
  const expanded = target.getAttribute("aria-expanded") === "true" || false;
  comButton.setAttribute("aria-expanded", !expanded);
  comForm.classList.toggle("hidden");
}

comButton.addEventListener("click", toggleNav2);