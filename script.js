document.addEventListener("DOMContentLoaded", () => {
    const validValues = ["запис1", "запис2", "запис3"];

    function checkInput() {
        const input = document.getElementById("userInput").value.trim();
        const messageElement = document.getElementById("message");

        if (!input) {
            messageElement.textContent = "Ви нічого не ввели!";
            messageElement.style.color = "red";
        } else if (!validValues.includes(input.toLowerCase())) {
            messageElement.textContent = "Такого запису не існує!";
            messageElement.style.color = "red";
        } else {
            
            const index = validValues.indexOf(input.toLowerCase());
            if (index !== -1) {
                validValues.splice(index, 1);
                messageElement.textContent = `Запис "${input}" успішно видалено!`;
                messageElement.style.color = "green";
            }
            console.log("Оновлений список записів:", validValues);
        }
    }

    document.querySelector("button").addEventListener("click", checkInput);
});