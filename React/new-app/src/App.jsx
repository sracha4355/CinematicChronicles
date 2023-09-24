import React from 'react';
import './App.css';


function App() {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Cinematic Chronicles</title>
        <link
          rel="icon"
          href="https://cdn-icons-png.flaticon.com/512/5507/5507847.png"
        />
        <link
          href="http://fonts.cdnfonts.com/css/arcade-classic"
          rel="stylesheet"
        />
        <link rel="stylesheet" href="css/style.css" />
      </head>
      <body>
        <div className="container">
          <h3>ENTER A MOVIE PROMPT</h3>
          <form>
            <div className="input-text">
              <input type="text" name="" required="" />
              <label>Enter prompt here...</label>
              <span></span>
            </div>
            <input type="submit" value="Generate" name="" className="btn" />
          </form>
        </div>
      </body>
    </html>
  );
}

export default App;
