document.addEventListener("DOMContentLoaded", function() {
    const mobileMenuToggle = document.getElementById("mobile-menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

  
    mobileMenuToggle.addEventListener("click", function(event) {
        event.stopPropagation(); 
        mobileMenu.classList.toggle("hidden");
    });

   
    document.body.addEventListener("click", function(event) {
        
        if (!mobileMenu.contains(event.target) && !mobileMenuToggle.contains(event.target)) {
            mobileMenu.classList.add("hidden");
        }
    });
});
