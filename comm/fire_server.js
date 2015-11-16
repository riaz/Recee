var Firebase = require("firebase");
var myFirebaseRef = new Firebase("https://recce.firebaseio.com/");
myFirebaseRef.child("/").on("value", function(snapshot) {
  console.log(snapshot.val()); 
});
