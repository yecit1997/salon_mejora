// Filtrar en tiempo real
document.getElementById('searchInput').addEventListener('keyup', function () {
    var input, filter, table, tr, td, i, j, txtValue
    input = document.getElementById('searchInput')
    filter = input.value.toLowerCase()
    table = document.getElementById('estilistaTable')
    tr = table.getElementsByTagName('tr')
  
    for (i = 0; i < tr.length; i++) {
      tr[i].style.display = 'none' // Ocultar todas las filas por defecto
      td = tr[i].getElementsByTagName('td')
      for (j = 0; j < td.length; j++) {
        if (td[j]) {
          txtValue = td[j].textContent || td[j].innerText
          if (txtValue.toLowerCase().indexOf(filter) > -1) {
            tr[i].style.display = ''
            break
          }
        }
      }
    }
  })