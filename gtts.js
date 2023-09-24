const tts = require('gtts');

// Get the text to be converted to speech
const text = 'This is some text to be converted to speech.';

// Convert the text to speech
const speech = tts.synthesize(text, {
  lang: 'en-US',
  rate: 1.0,
  pitch: 1.0,
  volume: 1.0
});

// Play the speech
speech.play();
