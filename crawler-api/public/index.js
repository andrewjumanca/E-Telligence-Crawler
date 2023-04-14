let index = 0,
    interval = 1000;

const rand = (min, max) => 
  Math.floor(Math.random() * (max - min + 1)) + min;

const animate = star => {
  star.style.setProperty("--star-left", `${rand(-10, 100)}%`);
  star.style.setProperty("--star-top", `${rand(-40, 80)}%`);

  star.style.animation = "none";
  star.offsetHeight;
  star.style.animation = "";
}

for (const star of document.getElementsByClassName("magic-star")) {
  setTimeout(() => {
    animate(star);
    
    setInterval(() => animate(star), 1000);
  }, index++ * (interval / 3))
}

// JSON visualizer
// const jsonContainer = document.getElementById('json-container');
// const jsonData = { "name": "John Doe", "age": 30, "city": "New York" };
// jsonContainer.textContent = JSON.stringify(jsonData, null, 2);
// Prism.highlightAll();

// Event Listener
const input = document.getElementById("searchQuery");
const button = document.getElementById("sendQueryButton");
const responseContainer = document.getElementById("response-container");
const loader = document.getElementById('loader-container');
const jsonBox = document.querySelector('.json-box');


button.addEventListener('click', async () => {
    const query = input.value
    jsonBox.style.display ='none'
    loader.style.display = 'block';


    // set input to api endpoint
    const response = await fetch('http://localhost:8000/api/v1?productName=' + query, {
      method: 'GET'
    });

    const data = await response.json();
    const jsonData = JSON.stringify(data, null, 2); // prettify JSON string with indentation
    // Hide the loader and show the json-box
    loader.style.display = 'none';
    jsonBox.style.display = 'block';

    responseContainer.textContent = jsonData
    Prism.highlightAll();
})