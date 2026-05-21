import { useState, useEffect} from "react";
import Registro from "./components/Registro";

function App(){
  //crear variable con memoria
  const [mensaje, setMensaje] = useState("Buscando a Python...")

  //useEffect recibe una funcion y un arreglo 
  //fetch sirve para hacer las peticiones a la API
  //cuando la respuesta llegue, la convertimos a JSON
   //cuando el JSON esté listo, lo usamos para actualizar nuestro mensaje
  useEffect(() => {
    fetch("http://localhost:8000/")
     .then(respuesta => respuesta.json())
     .then(datos => {
      console.log("Python mandó esto:", datos);
      setMensaje(datos.Mensaje);
    }, [])

    //si hay un error, lo mostramos en la consola
    .catch(error => {
      console.error("Error al conectar:", error);
      setMensaje("Error: FastAPI no responde");
   });
  }, [])

  //lo que se dibuja en la pantalla
  return(
    <div style={{textAlign: "center", marginTop: "50px"}}>
      <h1>Marketplace de Oficios</h1>
      {/* Usamos las llaves {} para meter nuestra variable de JavaScript adentro del HTML */}
      <p>Estado: {mensaje}</p>

      <hr />
      {/*dibujamos el formulario de registro*/}
      <Registro />
    </div>
  )
}

//exportamos la funcion para que vite pueda usarla
export default App;
