
document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const button = form.querySelector("button");

            if (button) {
                button.disabled = true;
                button.textContent = "Submitting...";
            }
        });
    });
});
