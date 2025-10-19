// Espera a que todo el contenido HTML de la página cargue antes de ejecutar el código
document.addEventListener("DOMContentLoaded", () => {
  // Recupera el carrito guardado en el navegador (localStorage)
  // Si no hay nada guardado, devuelve un arreglo vacío []
  const carrito = JSON.parse(localStorage.getItem("carritoFinal")) || [];
  console.log("Carrito recibido:", carrito); // verificamos en consola que si devuelva el array

  // Selecciona el formulario que hay en la página
  const form = document.querySelector("form");

  // Escucha el evento "submit" (cuando el usuario envía el formulario)
  form.addEventListener("submit", (e) => {
    e.preventDefault(); // Evita que la página se recargue automáticamente al enviar el form

    // Crea un objeto con todos los datos del formulario (nombre, dirección, etc.)
    const formData = new FormData(form);

    // Agrega al formulario los productos del carrito en formato JSON (texto)
    formData.append("carrito", JSON.stringify(carrito));

    // Envía los datos al servidor (a la misma URL actual)
    fetch("", {
      method: "POST",
      body: formData, // Se envía el formulario con los datos del usuario y el carrito
    })
      // Cuando el servidor responde, convertimos la respuesta en texto
      .then((res) => res.text())
      // Cuando llega la respuesta, mostramos mensaje y limpiamos el carrito
      .then((data) => {
        Toastify({
          text: "pedido confirmado con exito",
          duration: 8000,
          close: true,
          gravity: "top",
          position: "right",
          backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
        }).showToast();
        localStorage.removeItem("carritoFinal"); // Borra el carrito del navegador
        window.location.href = "/"; // Redirige al inicio de la tienda
      });
  });
});
