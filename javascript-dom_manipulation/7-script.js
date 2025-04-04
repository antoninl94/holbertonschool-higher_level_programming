fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
  const ul = document.querySelector('#list_movies');
  data.results.forEach(movies => {
    const li = document.createElement('li');
    li.textContent = movies.title;
    ul.appendChild(li);
  });
})
.catch(error => {
  document.querySelector('#list_movies').textContent = 'No movies found';
  console.error('Fetch error', error);
});
