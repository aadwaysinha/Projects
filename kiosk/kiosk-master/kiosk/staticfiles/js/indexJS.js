console.log('connected');

try {
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
} catch (e) {
  console.error(e);
  $('.no-browser-support').show();
  $('.app').hide();
}


var custom = $('#transcriptForm')
// custom.hide();
var noteTextarea = $('#note-textarea');


var noteContent = '';


/*-----------------------------
      Voice Recognition
------------------------------*/

// If false, the recording will stop after a few seconds of silence.
// When true, the silence period is longer (about 15 seconds),
// allowing us to keep recording even when the user pauses.
recognition.continuous = true;

// This block is called every time the Speech APi captures a line.
recognition.onresult = function (event) {

  // event is a SpeechRecognitionEvent object.
  // It holds all the lines we have captured so far.
  // We only need the current one.
  var current = event.resultIndex;

  // Get a transcript of what was said.
  var transcript = event.results[current][0].transcript;

  // Add the current transcript to the contents of our Note.
  // There is a weird bug on mobile, where everything is repeated twice.
  // There is no official solution so far so we have to handle an edge case.
  var mobileRepeatBug = (current == 1 && transcript == event.results[0][0].transcript);

  // OUTPUT FROM SPEECH API --- AARON
  if (!mobileRepeatBug) {
    noteContent += transcript;
    noteTextarea.val(noteContent);
    console.log(noteContent)
    custom.value = noteContent
    custom.html(noteContent)
  }
};

recognition.onstart = function () {
  console.log('Voice recognition activated. Try speaking into the microphone.');
}

recognition.onspeechend = function () {
  console.log('You were quiet for a while so voice recognition turned itself off.');
}

recognition.onerror = function (event) {
  if (event.error == 'no-speech') {
    console.log('No speech was detected. Try again.');
  };
}



/*-----------------------------
      App buttons and input
------------------------------*/

$('#micIconID').on('click', function (e) {
  if (noteContent.length) {
    noteContent += ' ';
  }
  recognition.start();
});


$('#pauseBTN').on('click', function (e) {
  recognition.stop();
  console.log('Voice recognition paused.');
});

$('#clearBTN').on('click', function(e){
    noteContent = '';
    custom.value = '';
    custom.html('');
    recognition.stop();
})

// Sync the text inside the text area with the noteContent variable.
noteTextarea.on('input', function () {
  noteContent = $(this).val();
})
