let inputTerm=document.getElementById("search_term");
let inputSubmit=document.getElementById("submit");
let inputBy=document.getElementById("search_by");
let marks = document.getElementById("marks");
let formdata=new FormData(document.getElementsByTagName("form")[0])
let div=document.getElementById("output");
formdata.append("search_term",inputTerm.value);
formdata.append("search_by",inputBy.value);
var teacherOptions="";
var studentOptions="";
var usernames=document.getElementById("usernames");
window.onload=()=>{
    fetch("http://localhost:8000/oninputstudent")
        .then(res=>res.json())
        .then(data=>{
            for(item of data){
                studentOptions+="<option>"+item["name"]+"</option>";
            }
            usernames.innerHTML=studentOptions;
        })
    fetch("http://localhost:8000/oninputteacher")
        .then(res=>res.json())
        .then(data=>{
            for(item of data){
                teacherOptions+="<option>"+item["name"]+"</option>";
            }
        })
    inputBy.onchange=()=>{
        if(inputBy.value=="st"){
            usernames.innerHTML=studentOptions;
        }
        else{
            usernames.innerHTML=teacherOptions;
        }
    }
}


function table_head(data){
    thead=document.createElement("thead");
    tr=document.createElement("tr");
    thead.appendChild(tr);
    for(let value of Object.keys(data)){
        th=document.createElement("th");
        th.textContent=value;
        tr.appendChild(th);
    }
    return thead;
}

function table_body(data){
    tbody=document.createElement("tbody");
    for(let item of data){
        tr=document.createElement("tr")
        tbody.appendChild(tr);
        for(let value of Object.values(item)){
            td=document.createElement("td");
            td.textContent=value;
            tr.appendChild(td);
        }
    }
    return tbody;
}

function createTable(data,captionValue){
    table=document.createElement("table");
    if(captionValue){
        caption=document.createElement("caption")
        caption.textContent=captionValue;
        table.appendChild(caption);
    }
    table.appendChild(table_head(data[0]));
    table.appendChild(table_body(data));
    return table;
}

inputSubmit.addEventListener("click",(event)=>{
    event.preventDefault();
    let url="http://localhost:8000/";
    if(marks.value != ""){
        url+="searchbymarks/"+marks.value;
    }
    else if(inputBy.value == "st"){
        url+="studentsearch/"+inputTerm.value;
    }
    else{
        url+="teachersearch/"+inputTerm.value;
    }
    fetchres = fetch(url);
    fetchres.then(res=>res.json()).then(data=>{
        div.innerHTML="";
        console.log(data);
        if(data[0]["students"]){
            let i=0;
            while(i<data.length){
                teacherCaption="students of "+data[i]["name"];
                console.log(teacherCaption);
                console.log(data[i]["students"]);
                if(data[i]["students"].length!=0){
                    div.appendChild(createTable(data[i]["students"],teacherCaption));
                }
                else{
                    p=document.createElement("p")
                    p.textContent="Sorry there are no students for "+data[i]["name"];
                    div.appendChild(p);
                }
                i=i+1;
            }
        }
        else{
            div.appendChild(createTable(data));
        }
    }).catch(err=>{
        console.log(err);
        div.textContent="something went wrong";
    })
    inputTerm.value="";
    marks.value="";
})






//inputTerm.addEventListener("input",()=>{
//    let url="http://localhost:8000/"
//    if(search_by.value == "st"){
//        url+="oninputstudent/"+inputTerm.value;
//    }
//    else{
//        url+="oninputteacher/"+inputTerm.value;
//    }
//    fetchres = fetch(url);
//    fetchres.then(res=>res.json()).then(data=>{
//        usernames=document.getElementById("usernames");
//        while(usernames.hasChildNodes()){
//            usernames.removeChild(usernames.firstChild);
//        }
//        for(item of data){
//            option=document.createElement("option");
//            option.text=item['name'];
//            usernames.appendChild(option);
//       }
//    }).catch(err=>console.log("something went wrong"))
//})



