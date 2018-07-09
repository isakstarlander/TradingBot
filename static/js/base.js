function toggleMenu() {
    const menuIcon = document.getElementById("navbar__toggle");
    const menu = document.getElementById("navbar__menu");
    menu.style.display = (menu.style.display === "" || menu.style.display === "none") 
        ? "flex" 
        : "none";
    if (menuIcon.classList.contains("fa-bars")) {
        menuIcon.classList.remove("fa-bars")
            menuIcon.classList.add("fa-times")
    } else {
        menuIcon.classList.remove("fa-times")
        menuIcon.classList.add("fa-bars")
    }
}