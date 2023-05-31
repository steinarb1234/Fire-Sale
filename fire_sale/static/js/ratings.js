


var stars = document.getElementById('stars');

for (var i = 0; i < 5; i++) {
var star = document.createElement('span');
star.className = 'star';
star.textContent = (i < Math.round(rating)) ? '\u2605' : '\u2606'; // Unicode character for filled star and unfilled star
stars.appendChild(star);
}