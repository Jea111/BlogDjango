// Array para guardar los productos del carrito
const carritoFinal = [];

// Seleccionamos todos los botones de "Agregar al carrito"
const btnAddToCart = document.querySelectorAll(".add_to_cart");

// Elemento donde mostraremos el contenido del carrito
const carritoDiv = document.querySelector("#carrito");

// Recorremos todos los botones
btnAddToCart.forEach((btn) => {
  btn.addEventListener("click", (event) => {
    // Encontramos la tarjeta (card) más cercana al botón
    const card = event.target.closest(".card");

    // Obtenemos los datos del producto desde la tarjeta
    const nombreProducto = card.querySelector(".card-title").textContent.trim();
    const precioProducto = card
      .querySelector(".precioProducto")
      .textContent.trim();
    const cantidad = 1;

    // Creamos un objeto producto
    const producto = {
      nombre: nombreProducto,
      precio: precioProducto,
      cantidad: cantidad,
    };

    // Agregamos el producto al carrito
    carritoFinal.push(producto);

    // Mostramos el carrito actualizado
    mostrarCarrito();
  });
});

// Función para mostrar el carrito
function mostrarCarrito() {
  carritoDiv.innerHTML = `
      <h5 class="text-center mt-3 mb-3 g-3">🛒 Carrito de Compras</h5>
      <ul class="list-group">
        ${carritoFinal
          .map(
            (item) => `
          <li class="list-group-item d-flex justify-content-between align-items-center">
            ${item.nombre}
            <span class="badge bg-success rounded-pill">${item.precio}</span>
          </li>`
          )
          .join("")}
      </ul><br>
      <button class='btn btn-success finishBuy'>Finalizar</button>
    `;
}
