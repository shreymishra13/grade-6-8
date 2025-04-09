function validate(e) {
    e.preventDefault();


    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
  
   
















 

    if (email === "") {
        document.getElementById("message").innerHTML="Please enter the email";
        document.getElementById("message").style.color="red";
       
    }
    
    else if (pass === "") {
        document.getElementById("message").innerHTML="Please enter the password";
        document.getElementById("message").style.color="red";
    } 
    else {
        document.getElementById("message").innerHTML="Login Successfull";
        document.getElementById("message").style.color="green";
    }

  
}
function palindrome(myString){
	
	var input = myString.replace(/[^A-Z0-9]/ig, "").toLowerCase();


	var reversedInput = input.split('').reverse().join('');
	
	
	if (input === reversedInput){
		document.write("<div>" + myString + " is a palindrome <div>")
	}
	else{
		document.write("<div>" + myString + " is not a palindrome <div>")
	}
}


palindrome("madam")

