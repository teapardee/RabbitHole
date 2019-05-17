function preview(clicked_id) {
  console.log('test');
  document.getElementById(clicked_id).addEventListener('click', function() {
    document.querySelector('.modal').style.display = 'flex';
  });

  document.querySelector('.close').addEventListener('click', function() {
    document.querySelector('.modal').style.display = 'none';
  });
}
