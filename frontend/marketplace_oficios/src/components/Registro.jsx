import { useState } from "react";

function Registro() {
    // Estado para almacenar los datos del formulario
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    //funcion se ejecuta al apretar "Registrarme"
    const manejarRegistro = async (e) => {
        e.preventDefault(); // evita que la pagina se recargue sola

        // preparar los datos para enviar a la API
        const paqueteDatos = {
            name: name,
            email: email,
            password: password
        };

        try {
            // usamos fetch para ennviar los datos a la API
            const respuesta = await fetch("http://localhost:8000/users/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json" // decimos que es JSON
                },
                body: JSON.stringify(paqueteDatos) // convertimos el paquete a JSON
            });

            // revisamos que contesto el backend
            if (respuesta.ok) {
                const datosCreados = await respuesta.json();
                alert("Usuario creado correctamente: " + datosCreados.id);

                //vaciamos el formulario
                setName("");
                setEmail("");
                setPassword("");
            }
            else {
                    // si hubo un error, lo mostramos
                    const error = await respuesta.json();
                    alert("Error al crear usuario: " + error.detail);

                }

            }
            catch (error) {
                alert("Error de conexion: No se pudo conectar con el servidor ");

            }
                
            
        }

    
    
    // lo que se dibuja en pantalla
    return (
        <div style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
         <h2>Crear una Cuenta</h2>
      
         <form onSubmit={manejarRegistro}>
           {<><div style={{ marginBottom: "10px" }}>
                    <label>Nombre: </label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required />
                </div><div style={{ marginBottom: "10px" }}>
                        <label>Email: </label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required />
                    </div><div style={{ marginBottom: "10px" }}>
                        <label>Contraseña: </label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required />
                    </div></>}
        
          <button type="submit">Registrarme</button>
         </form>
        </div>
    );

}
export default Registro;