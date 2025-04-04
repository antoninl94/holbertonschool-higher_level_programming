fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json())
.then(data => {
  const characterElement = document.querySelector('#character');
  characterElement.textContent = data.name;
})
.catch(error => {
  document.querySelector('#character').textContent = 'No character found';
  console.error('Fetch error', error);
});
