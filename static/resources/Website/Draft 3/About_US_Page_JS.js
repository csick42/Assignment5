// JavaScript Document
// Contributors: Christian Sickmeier //

// Contact Form //

var form = document.getElementById("ContactForm");
console.log("Found form:", form);
	
	if (!form) {
		console.error("ContactForm no found!");
	} else {
		form.addEventListener("submit", function(event) {
		console.log("Submit handler fired");
		event.preventDefault();
		
		var name = document.getElementById("ContactName").value;
		var email = document.getElementById("ContactEmail").value;
		var message = document.getElementById("ContactMessage").value;
		console.log("Form values:", { name, email, message });
		
		var subject = "Website Contact from " + name;
		var body = "Name: " + name + "\n" + "Email: " + email + "\n\n" + message;
		var mailtoLink = "mailto:csickmei@iu.edu" + "?subject=" +encodeURIComponent(subject) + "&body=" +encodeURIComponent(body);
		console.log("mailto link:", mailtoLink);
	
		window.location.href = mailtoLink;
	});
	}

