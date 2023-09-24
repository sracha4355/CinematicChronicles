import './App.css';
import React, { useState } from 'react';
import axios from 'axios'; // Import Axios
import StringButtons from './stringButtons.jsx';
import {allChoices, choiceInStringFormat, setChoiceInStringFormat} from './global';

 function App() {
    const [showChoices, setShowChoices] = useState(true);
    const [global_choices, setGlobalChoices] = useState([])
    const ROOT = "http://127.0.0.1:5000"
    const [imageURL, setImageURL]  = useState("/")
    const [notdone, setNotDone] = useState(true)
    const [allChoicesInStr, setAllChoicesInStr] = useState("")


    const handleChange = async (e) => {
      setShowChoices(false)

      e.preventDefault(); // Prevent the default form submission behavior

      // Get the value of the input field
      const prompt = e.target.prompt.value;

      // Make an API call using Axios (you can replace the URL with your actual API endpoint)
      try {
        await axios.get('http://127.0.0.1:5000/setup/choices/3/topic/' + prompt + '/depth/6');
        let choices = await axios.get('http://127.0.0.1:5000/generate');
        choices = choices.data
        let tmp = []
        for(let i = 0; i < choices.length; i++){   
          tmp.push(choices[i])
        }
        setGlobalChoices(tmp)

        let dalleURL = await axios.get(ROOT + "/dalle/img/" + prompt)
        dalleURL = dalleURL.data
        setImageURL(dalleURL)
        
        
      } catch (error) {
        console.error('API call failed:', error);
      } 
    };

    const choseAChoice = async (e) => {
      let text = e.target.textContent
      allChoices.push(text)
      
      let res = await axios.get(ROOT + "/selected/choice/" + text)

      let  choices = await axios.get('http://127.0.0.1:5000/generate');
      choices = choices.data
      let tmp = []
        for(let i = 0; i < choices.length; i++){   
          tmp.push(choices[i])
        }
      setGlobalChoices(tmp)
      console.log(global_choices)
      
      let dalleURL = await axios.get(ROOT + "/dalle/img/" + text)
      dalleURL = dalleURL.data
      setImageURL(dalleURL)

      console.log("All choices chosen so far")
      console.log(allChoices)
    };

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
        
        { showChoices ? 
          <div className="container">
            <h3>ENTER A MOVIE PROMPT</h3>
            <form onSubmit={handleChange}>
              <div className="input-text">
                <input type="text" name="prompt" required="" />
                <label>Enter prompt here...</label>
                <span></span>
              </div>
              <input type="submit" value="Generate" name="" className="btn" />
            </form>
          </div>
          : 
            notdone ?
            <div className="buttonsLayout">
              <h3>YOUR CHOICE</h3>
              <img src={imageURL}  className="dalle-image"></img>
              <StringButtons strings={global_choices} handleButtonClick={choseAChoice}/>
              <button className="btn" onClick={() => {
                setNotDone(false)
                setAllChoicesInStr(allChoices.join(' '))
                console.log("chsk: "+allChoicesInStr)
    
              }}>End</button>
            </div> : 
            <div className="end-of-story">
              <h3 className="endOfStoryHeader ">YOUR  STORY !!</h3>
              <p className="endOfStoryParagraph">{allChoicesInStr}</p>
              
            </div>
          
        }
        



      </body>
    </html>
  );
}

export default App;
