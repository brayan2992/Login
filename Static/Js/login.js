document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");

    form.addEventListener("submit", (e) => {
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (email === "" || password === "") {
            e.preventDefault();
            alert("Por favor, completa todos los campos.");
            return;
        }

        if (!validateEmail(email)) {
            e.preventDefault();
            alert("El correo electrónico no es válido.");
            return;
        }

        // ✅ Si pasa las validaciones, NO usamos e.preventDefault()
        // El formulario se enviará normalmente a Flask
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
