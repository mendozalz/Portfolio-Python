// Función para formatear la hora
function formatearHora(fecha) {
  var dia = fecha.getDate();
  var mes = fecha.getMonth() + 1; // Sumar 1 ya que los meses comienzan desde 0
  var ano = fecha.getFullYear();
  var horas = fecha.getHours();
  var minutos = fecha.getMinutes();
  var segundos = fecha.getSeconds();

  // Formatear la hora en un formato legible
  return `${dia}/${mes}/${ano} ${horas}:${minutos}:${segundos}`;
}

// Función para actualizar la hora actual
function actualizarHora() {
  // Obtener la fecha y hora actual
  var fechaHoraActual = new Date();

  // Formatear la hora
  var horaFormateada = formatearHora(fechaHoraActual);

  // Obtener el elemento div con la clase "fecha_actual"
  var divFechaActual = document.querySelector(".fecha_actual");

  // Mostrar la hora dentro del div
  divFechaActual.textContent = horaFormateada;
}

// Actualizar la hora cada segundo
setInterval(actualizarHora, 1000);

// Llamar a la función por primera vez para mostrar la hora inicial
actualizarHora();
