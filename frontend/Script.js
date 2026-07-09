const apiUrl = "https://peyt9tymbh.execute-api.us-east-1.amazonaws.com/production-prod/Customer";

async function addCustomer() {

const customer={

Customer_id:document.getElementById("customerId").value,

CustomerName:document.getElementById("customerName").value,

Email:document.getElementById("email").value,

Phone:document.getElementById("phone").value,

City:document.getElementById("city").value

};

const response=await fetch(apiUrl,{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(customer)

});

const data=await response.json();

document.getElementById("addMessage").innerHTML=data.message;

}

async function searchCustomer(){

const id=document.getElementById("searchId").value;

const response=await fetch(apiUrl+"?Customer_id="+id);

const data=await response.json();

if(data.Customer_id){

document.getElementById("result").innerHTML=

"<b>Customer ID:</b> "+data.Customer_id+"<br>"+

"<b>Name:</b> "+data.CustomerName+"<br>"+

"<b>Email:</b> "+data.Email+"<br>"+

"<b>Phone:</b> "+data.Phone+"<br>"+

"<b>City:</b> "+data.City;

}

else{

document.getElementById("result").innerHTML=data.message;

}

}