/* 
this code make an effect the text appaire char by char
make by cartoone
*/

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
  
document.addEventListener('DOMContentLoaded', function() {
  var text_zone = document.getElementsByClassName("spawn");
  var content = [];

  Array.from(text_zone).forEach((element) => content.push(element.innerHTML));
  Array.from(text_zone).forEach((element) => element.innerHTML = "");

  Array.from(text_zone).forEach((element, index) => {
    let chaine = content[index];
    let tableau = chaine.split("");

    let i = 0;
    function ajouterCaractere() {
      let time = 3000/tableau.length
      if (i < tableau.length) {
        element.textContent += tableau[i];
        i++;
        sleep(time).then(ajouterCaractere);
      }
    }
    ajouterCaractere();
  });
});
  