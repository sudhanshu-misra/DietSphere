function toggleDarkMode() {
    document.body.classList.toggle("dark");
    localStorage.setItem("darkmode", document.body.classList.contains("dark"));
}

window.onload = () => {
    if (localStorage.getItem("darkmode") === "true") {
        document.body.classList.add("dark");
    }
}