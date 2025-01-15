// Delete listing

const deleteBtn = document.getElementById("deleteBtn")
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

deleteBtn.addEventListener("click", () => {
    deleteModal.show()
})

deleteConfirm.addEventListener("click", () => {
    deleteConfirm.href = "delete"
})
