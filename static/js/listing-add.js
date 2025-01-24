// Add listing
const addBtn = document.getElementById("addBtn");
const addModal = new bootstrap.Modal(document.getElementById("addModal"));
addBtn.addEventListener("click", () => {
    addModal.show();
});
