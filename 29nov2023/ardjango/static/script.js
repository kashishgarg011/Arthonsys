function validateForm() {
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  var message = document.getElementById('message').value;

  if (name && email && message) {
    alert('Form submitted successfully!\nName: ' + name + '\nEmail: ' + email + '\nMessage: ' + message);
  } else {
    alert('Please fill in all fields.');
  }
}
