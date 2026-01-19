let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: 'centered', targets: [0,1,2,3,4,5,6] },
        { orderable: false, targets: [5,6]},
        { searchable: false, targets: [0,5,6] },
    ],
    pageLength: 4,
    destroy: true,
    language: {
        decimal: "",
        emptyTable: "No hay registros",
        info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
        infoFiltered: "(Filtrado de _MAX_ total entradas)",
        infoPostFix: "",
        thousands: ",",
        lengthMenu: "Mostrar _MENU_ Entradas",
        loadingRecords: "Cargando...",
        processing: "Procesando...",
        search: "Buscar:",
        zeroRecords: "Sin resultados encontrados",
        paginate: {
            first: "Primero",
            last: "Ultimo",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};

const initDataTable = async() => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $('#datatable-programmers').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};


const listProgrammers = async() => {
    try {
        const response = await fetch('http://localhost:8000/app/list_programmers');
        const data = await response.json();
        console.log(data);

        let content = ``
        data.programmers.forEach((programmer, index) => {
            content+= `
                <tr>
                    <td>${index}</td>
                    <td>${programmer.name}</td>
                    <td>${programmer.country}</td>
                    <td>${programmer.birthday}</td>
                    <td>${programmer.score}</td>
                    <td>${programmer.score >= 8 
                        ? "<i class='fa-solid fa-check' style='color: green;'></>" 
                        : "<i class='fa-solid fa-xmark' style='color: red;'></>" }</td>
                    <td>
                    <a href="http://localhost:8000/app/edit_programmers/${programmer.id}">
                        <button class="btn btn-sm btn-primary"><i class="fa-solid fa-pencil"></i></button>
                    </a>
                    <a onclick="deleteProgrammer('http://localhost:8000/app/delete_programmers/${programmer.id}')">
                        <button class="btn btn-sm btn-danger"><i class="fa-solid fa-trash-can"></i></button>
                    </a>
                    </td>
                </tr>
            `
        });
        tableBody_programmers.innerHTML = content;
    } catch(ex) {
        alert(ex)
    }
}


window.addEventListener('load', async() => {
    await initDataTable();
});


/* function deleteProgrammer(url) {
    Swal.fire({
        title: "Esta seguro de borrar?",
        text: "Este contenido no se puede recuperar!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Si, borrar!",
        closeOnConfirm: true
    }).then(() => {
            $.ajax({
                type: 'DELETE',
                url: url,
                success: function (data) {
                    if (data.success) {
                        toastr.success(data.message);
                        dataTable.ajax.reload();
                    }
                    else {
                        toastr.error(data.message);
                    }
                }
            });
        });
} */

async function deleteProgrammer(url) {
    const result = await Swal.fire({
        title: "¿Está seguro de borrar?",
        text: "Este contenido no se puede recuperar!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Sí, borrar!",
    });

    if (result.isConfirmed) {
        try {
            const response = await fetch(url, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Si usas CSRF
                    'Content-Type': 'application/json',
                },
            });

            const data = await response.json();
            console.log(data);
            if (response.ok && data.success) {
                Swal.fire("¡Eliminado!", data.message, "success");
                dataTable.ajax.reload(); // Recarga la tabla
            } else {
                Swal.fire("Error", data.message || "No se pudo eliminar", "error");
            }
        } catch (error) {
            Swal.fire("Error", "No se pudo conectar al servidor", "error");
            console.error(error);
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue);
    return cookieValue;
}