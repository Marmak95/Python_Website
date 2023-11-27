function addCategory() {
    // Get the category name from the input field.
    const categoryName = document.getElementById("category-name").value;

    // Make an AJAX request to the server.
    fetch("/admin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            action: "add_category",
            categoryName: categoryName,
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Reload the page to show the successful flash message.
                window.location.reload();
            } else {
                // Reload the page to show the unsuccessful flash message.
                window.location.reload();
                console.error("Error adding category:", data.error);
            }
        })
        .catch(error => console.error("Error:", error));
}

// Call the addCategory function when the DOM is fully loaded.
document.addEventListener("DOMContentLoaded", function () {
    // Get the saveCategoryButton element
    const saveCategoryButton = document.getElementById("saveCategoryButton");

    // Add a click event listener to the saveCategoryButton.
    saveCategoryButton.addEventListener("click", function () {
        // Event handling code.
        addCategory();
    });
});
