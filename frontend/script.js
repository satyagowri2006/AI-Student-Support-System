// Detect module from URL
const params = new URLSearchParams(window.location.search);
const moduleType = params.get("module");

// Chat container
const chat = document.getElementById("messages");


// HOME BUTTON
function goHome(){
window.location.href="../index.html"
}


// QUICK BUTTONS
function quick(text){
const input=document.getElementById("userInput")
input.value=text
sendMessage()
}


// SEND MESSAGE
function sendMessage(){

let input=document.getElementById("userInput")

if(!input) return

let msg=input.value.trim()

if(msg==="") return

addUser(msg)

input.value=""

setTimeout(()=>{
addBot(generateResponse(msg))
},600)

}


// USER MESSAGE
function addUser(text){

if(!chat) return

chat.innerHTML+=`

<div class="flex justify-end">
<div class="bg-blue-600 text-white px-4 py-3 rounded-2xl max-w-md">
${text}
</div>
</div>

`

chat.scrollTop=chat.scrollHeight

}


// BOT MESSAGE
function addBot(text){

if(!chat) return

chat.innerHTML+=`

<div class="flex justify-start">
<div class="bg-gray-100 px-4 py-3 rounded-2xl max-w-md">
${text}
</div>
</div>

`

chat.scrollTop=chat.scrollHeight

}



// AI RESPONSE LOGIC
function generateResponse(msg){

msg=msg.toLowerCase()



// ADMISSION MODULE
if(moduleType==="admission"){

if(msg.includes("eligibility"))
return "Eligibility for B.Tech requires 60% in Physics, Chemistry and Mathematics."

if(msg.includes("apply"))
return "You can apply through the Vignan University admission portal."

if(msg.includes("program"))
return "Programs available include B.Tech, MBA, B.Pharm, M.Tech and Science courses."

return "Ask about eligibility, programs, application process or admission deadlines."

}



// ACADEMIC MODULE
if(moduleType==="academic"){

if(msg.includes("course"))
return "Course registration can be done through the student portal."

if(msg.includes("credit"))
return "Maximum credit load per semester is typically 24 credits."

if(msg.includes("calendar"))
return "The academic calendar includes semester schedules, exams and holidays."

return "Ask about courses, credits, exam schedules or academic calendar."

}



// FINANCIAL MODULE
if(moduleType==="financial"){

if(msg.includes("scholarship"))
return "Vignan University offers merit scholarships, sports scholarships and need-based financial aid."

if(msg.includes("fee"))
return "Fee payment can be done online through the student portal."

if(msg.includes("loan"))
return "Education loan assistance is available through partnered banks."

return "Ask about scholarships, fee payment, loans or financial aid."

}



// CAMPUS MODULE
if(moduleType==="campus"){

if(msg.includes("hostel"))
return "Vignan University has 5 boys hostels and 4 girls hostels with WiFi and security."

if(msg.includes("transport"))
return "University buses operate from major nearby cities."

if(msg.includes("library"))
return "The central library contains 100,000+ books and digital resources."

return "Ask about hostel facilities, transport services or campus facilities."

}



// MENTAL HEALTH MODULE
if(moduleType==="mental"){

if(msg.includes("stress"))
return "The counseling center provides stress management programs."

if(msg.includes("appointment"))
return "You can schedule counseling sessions through the Student Wellness Center."

if(msg.includes("counsel"))
return "Professional counselors are available Monday to Friday."

return "Ask about counseling sessions, stress management or wellness support."

}



// GENERAL CHATBOT (chatbot.html)
if(msg.includes("admission"))
return "Admissions are open for B.Tech, MBA, Pharmacy and Science programs."

if(msg.includes("scholarship"))
return "Vignan University offers merit scholarships, need-based aid and sports scholarships."

if(msg.includes("hostel"))
return "We have 5 boys hostels and 4 girls hostels with WiFi and security."

if(msg.includes("course"))
return "Course registration can be done through the student portal."

if(msg.includes("counsel"))
return "The Student Wellness Center provides counseling services."

return "I can help with admissions, academics, scholarships, hostel facilities or counseling."

}



// MODULE DESCRIPTIONS
const descriptions = {

admission:"Get help with programs, eligibility, and admission applications.",

academic:"Ask about courses, credits, exam schedules and academic calendar.",

financial:"Information about fees, scholarships and education loans.",

campus:"Hostel facilities, transport services and campus navigation.",

mental:"Counseling services and student mental wellness support."

};


// DISPLAY MODULE DESCRIPTION
const descBox=document.getElementById("moduleDescription")

if(descBox){

descBox.innerText=
descriptions[moduleType] || "Ask the AI assistant for help."

}