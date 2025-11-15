const ctx = document.getElementById('resultsChart').getContext('2d');

function renderChart(labels, data) {
    const resultsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Quiz Results',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Your Quiz Performance'
                }
            }
        }
    });
}

function fetchResults() {
    fetch('/quiz-application/src/php/api/get_results.php')
        .then(response => response.json())
        .then(data => {
            const labels = data.labels;
            const scores = data.scores;
            renderChart(labels, scores);
        })
        .catch(error => console.error('Error fetching results:', error));
}

document.addEventListener('DOMContentLoaded', fetchResults);