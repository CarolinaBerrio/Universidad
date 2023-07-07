(function () {

    const bntEliminacion = document.querySelectorAll(".bntEliminacion");

    bntEliminacion.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('¿seguro de eliminar el curso?');
            if(!confirmacion) {
                e.preventDefault();
            }
    
        });
    });
})();