import React from 'react';

function StringButtons({ strings, handleButtonClick }) {

  return (
    <div className="button-container">
      {strings.map((str, index) => (
        <button
          key={index}
          className="string-button"
          onClick={(event) => handleButtonClick(event)}
        >
          {str}
        </button>
      ))}
    </div>
  );
}

export default StringButtons;
