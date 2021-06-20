var firebaseConfig = {
    apiKey: "AIzaSyDEItAUc5mdQbONUJkUIwG_PFJcNUIX0wY",
    authDomain: "bitly-54078.firebaseapp.com",
    projectId: "bitly-54078",
    storageBucket: "bitly-54078.appspot.com",
    messagingSenderId: "503665618541",
    appId: "1:503665618541:web:bfb3e7d1b5559596391964",
    measurementId: "G-ECW3ZH72EY"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig)
  firebase.analytics();
  onAppInit();
 
  
function loginWithPopup(provider){
  firebase.auth()
  .signInWithPopup(provider)
  .then((result) => {
    // getIdToken(result.user)
    var credential = result.credential;
    var token = credential.accessToken;
    var user = result.user;
  }).catch((error) => {
      console.log(error)
    var errorCode = error.code;
    var errorMessage = error.message;
    var email = error.email;
    var credential = error.credential;
  });
}

  function loginWithGoogle(){
    const googleAuthProvider= new firebase.auth.GoogleAuthProvider();
    loginWithPopup(googleAuthProvider)
  }

  function loginWithFacebook(){
    const facebookAuthProvider = new firebase.auth.FacebookAuthProvider();
    loginWithPopup(facebookAuthProvider)
  }
  //  createAccoutWithEmail("sanjay32rawat@gmail.com","test@123")

  function loginWithEmail(email,password){
    firebase.auth().sendSignInLinkToEmail(email, password)
  .then((userCredential) => {
    var user = userCredential.user;
    console.log(userCredential);
  })
  .catch((error) => {
    console.log(error);
    var errorCode = error.code;
    var errorMessage = error.message;
  });
  }

function createAccoutWithEmail(email,password){
  firebase.auth().createUserWithEmailAndPassword(email, password)
  .then((userCredential) => {
    console.log(userCredential)
    // ...
  })
  .catch((error) => {
    console.log(error);
    var errorCode = error.code;
    var errorMessage = error.message;
    // ..
  });
}
  function onAppInit(){
    firebase.auth().onAuthStateChanged((user)=> {
      user.sendEmailVerification()
      console.log(user);
        firebase.auth().onIdTokenChanged(function(user) {
          user && getIdToken(user);
        });
  })
}

  function getIdToken(user,forceRefresh=false){
    user.getIdToken(forceRefresh).then(idToken=>{
      localStorage.setItem('idToken',idToken)
      console.log(idToken);
    }).catch(error=>{
     console.log(error)
    })
  }