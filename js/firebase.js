import { initializeApp } from 'firebase/app';
import { getDatabase } from 'firebase/database';

const firebaseConfig = {
  apiKey: "AIzaSyBgVuOwBFHuN8lMANKpcmVAJQyKDIi1xzs",
  authDomain: "ganime-77d23.firebaseapp.com",
  databaseURL: "https://ganime-77d23-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "ganime-77d23",
  storageBucket: "ganime-77d23.appspot.com",
  messagingSenderId: "473337506294",
  appId: "1:473337506294:web:9447bbc8474329ce7e3fd7",
  measurementId: "G-KXHZ4GV7CG"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

function registrarUsuario() {
  const db = getDatabase(app);
  set(ref(db, 'Usuario/1'), {
    id: "2",
    user: "Prueba",
    password; "Prueba",
    email: "Prueba",
    description: "Prueba"
  });

  document.getelementbyid("buttonRegistrarUsuario").innerhtml = "Funciona?";
}
