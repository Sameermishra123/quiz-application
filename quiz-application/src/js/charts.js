document.addEventListener("DOMContentLoaded", () => {
    const score = Number(localStorage.getItem("score"));
    const correct = Number(localStorage.getItem("correct"));
    const incorrect = Number(localStorage.getItem("incorrect"));

    document.getElementById("score").textContent = score;
    document.getElementById("correct-answers").textContent = correct;
    document.getElementById("incorrect-answers").textContent = incorrect;

    new Chart(document.getElementById("resultsChart"), {
        type: "bar",
        data: {
            labels: ["Correct", "Incorrect"],
            datasets: [
                {
                    label: "Results",
                    data: [correct, incorrect],
                    backgroundColor: ["green", "red"]
                }
            ]
        }
    });
});
