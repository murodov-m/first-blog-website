const likeButtons = document.getElementsByClassName('like');

for (let i = 0; i < likeButtons.length; i++) {
  likeButtons[i].addEventListener('click', function() {
    alert('Liked!');
  });
}
