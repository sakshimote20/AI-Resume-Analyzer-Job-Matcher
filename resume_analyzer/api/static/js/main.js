// Load jobs

fetch("/api/jobs/")
.then(response => response.json())
.then(data => {

const list = document.getElementById("jobList")

data.forEach(job => {

const li = document.createElement("li")

li.innerHTML = `
<strong>${job.title}</strong> - ${job.company}<br>
Description: ${job.description}
`

list.appendChild(li)

})

// update jobs count card
document.getElementById("jobCount").innerText = data.length

})



// Upload resume

function uploadResume(){

const fileInput = document.getElementById("resumeFile")

if(fileInput.files.length === 0){
alert("Please select a resume")
return
}

const formData = new FormData()

formData.append("resume", fileInput.files[0])

const csrfToken = document.getElementById("csrfToken").value

fetch("/api/upload-resume/",{

method:"POST",

headers:{
"X-CSRFToken": csrfToken
},

body:formData

})

.then(res => res.json())

.then(data => {

let output = "<b>Name:</b> " + data.name + "<br><br>"

output += "<h3>Job Matches</h3>"

// update dashboard cards
document.getElementById("totalResumes").innerText = 1

document.getElementById("bestScore").innerText =
data.matches[0].score + "%"


data.matches.forEach(job => {

output += job.title + " - " + job.company +
" (Match Score: " + job.score + "%)<br>"

})

document.getElementById("result").innerHTML = output

})

}