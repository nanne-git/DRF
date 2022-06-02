inputTerm=document.getElementById("search_term");
inputSubmit=document.getElementById("submit");
inputTerm.addEventListener("input",()=>{
    inputBy=document.getElementById("search_by");
    formdata=new FormData(document.getElementsByTagName("form")[0])
    formdata.append("search_term",inputTerm.value);
    formdata.append("search_by",inputBy.value);
    let url="http://localhost:8000/";
    if(search_by.value == "st"){
        url+="oninputstudent/"+inputTerm.value;
    }
    else{
        url+="oninputteacher/"+inputTerm.value;
    }
    fetchres = fetch(url);
    fetchres.then(res=>res.json()).then(data=>{
        usernames=document.getElementById("usernames");
        while(usernames.hasChildNodes()){
            usernames.removeChild(usernames.firstChild);
        }
        for(item of data){
            option=document.createElement("option");
            option.text=item['name'];
            usernames.appendChild(option);
       }
    })
})
inputSubmit.addEventListener("click",(event)=>{
    event.preventDefault();
    marks=document.getElementById("marks");
    inputBy=document.getElementById("search_by");
    formdata=new FormData(document.getElementsByTagName("form")[0])
    formdata.append("search_term",inputTerm.value);
    formdata.append("search_by",inputBy.value);
    let url="http://localhost:8000/";
    if(search_by.value == "st"){
        url+="studentsearch/"+inputTerm.value+"/"+marks;
    }
    else{
        url+="teachersearch/"+inputTerm.value;
    }
    fetchres = fetch(url);
    fetchres.then(res=>res.json()).then(data=>{
        div=document.getElementById("output");
        div.innerHTML="";
        table=document.createElement("table");
        thead=document.createElement("thead");
        table.appendChild(thead);
        tbody=document.createElement("tbody");
        table.appendChild(tbody);
        th=document.createElement("tr");
        thead.appendChild(th);
        for(let value of Object.keys(data[0])){
            console.log(value);
            td=document.createElement("td");
            td.textContent=value;
            th.appendChild(td);
        }
        for(let item of data){
            tr=document.createElement("tr")
            tbody.appendChild(tr);
            for(let value of Object.values(item)){
                td=document.createElement("td");
                td.textContent=value;
                tr.appendChild(td);
            }
        }
        div.appendChild(table);
        inputTerm.value="";
    });
})

