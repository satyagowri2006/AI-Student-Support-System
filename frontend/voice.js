function startVoice(){

const recognition = new webkitSpeechRecognition();

recognition.lang="en-US";

recognition.onresult=function(event){

let text=event.results[0][0].transcript;

document.getElementById("userInput").value=text;

sendMessage();

}

recognition.start();
}