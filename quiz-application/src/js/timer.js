document.addEventListener("DOMContentLoaded", () => {
    let time = 60;
    const display = document.getElementById("time");

    const countdown = setInterval(() => {
        time--;
        display.textContent = time;

        if (time <= 0) {
            clearInterval(countdown);
            document.getElementById("submit-btn").click();
        }
    }, 1000);
});
