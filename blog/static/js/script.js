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
    const precioProducto = parseFloat(
      card.querySelector(".precioProducto").textContent.trim()
    );
    const cantidad = 1;

    const total = cantidad * precioProducto;

    // Creamos un objeto producto
    const producto = {
      nombre: nombreProducto,
      precio: precioProducto,
      cantidad: cantidad,
      total: total,
    };

    carritoFinal.push(producto);

    mostrarCarrito();
  });
});

function mostrarCarrito() {
  // Calculamos el total general de todos los productos
  const totalGeneral = carritoFinal.reduce((acc, item) => acc + item.total, 0);

  carritoDiv.innerHTML = `
    <h5 class="text-center mt-3 mb-3 g-3">🛒 Carrito de Compras</h5>
    <ul class="list-group">
      ${carritoFinal
        .map(
          (item) => `
        <li class="list-group-item d-flex justify-content-between align-items-center">
          ${item.nombre} (x${item.cantidad})
          <span class="badge bg-success rounded-pill">$${item.total.toFixed(
            2
          )}</span>
        </li>
      `
        )
        .join("")}
    </ul>
    <div class="mt-3 text-center">
      <h6 class="text-success"> Total: $${totalGeneral.toFixed(2)}</h6>
    </div>
    <br>
    <button class='btn btn-success finishBuy'>Finalizar</button>
  `;
}

// Evento al hacer clic en "Finalizar compra"
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("finishBuy")) {
    // Guardamos los productos del carrito en localStorage
    localStorage.setItem("carritoFinal", JSON.stringify(carritoFinal));

    // Redirigimos al formulario Django
    window.location.href = "/pedidos/";
  }
});

//alerta cada que se agrega un producto
document.addEventListener("DOMContentLoaded", () => {
  const alertButtons = document.querySelectorAll(".alertBtn");

  alertButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const nombreProducto = btn.dataset.producto || "Producto";

      Toastify({
        text: `${nombreProducto} agregado exitosamente`,
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
      }).showToast();
    });
  });
});
