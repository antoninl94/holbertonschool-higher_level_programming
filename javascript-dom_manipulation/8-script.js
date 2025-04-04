document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
      document.querySelector('#hello').textContent = data.hello;
  })
  .catch(error => {
    document.querySelector('#hello').textContent = "Hello can't be fetched";
    console.error('Fetch Error', error);
  });
});
