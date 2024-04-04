document.addEventListener("DOMContentLoaded", function() {
    const mobileMenuToggle = document.getElementById("mobile-menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    mobileMenuToggle.addEventListener("click", function() {
        mobileMenu.classList.toggle("hidden");
    });
});