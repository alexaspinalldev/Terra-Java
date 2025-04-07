const loaders = document.querySelectorAll('[data-load]');
const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));


window.addEventListener('pageshow', function (event) {
    if (event.persisted || performance.getEntriesByType("navigation")[0].type === 'back_forward') {
        loadingModal.hide();
    }
});

loaders.forEach(loader => {
    loader.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey) {
            return;
        }

        loadingModal.show();
    });
});