// Load and display results
document.addEventListener('DOMContentLoaded', function() {
    const resultsData = localStorage.getItem('quizResults');
    
    if (!resultsData) {
        alert('No quiz results found!');
        window.location.href = 'index.php';
        return;
    }
    
    const results = JSON.parse(resultsData);
    
    // Display summary
    document.getElementById('totalQuestions').textContent = results.totalQuestions;
    document.getElementById('correctAnswers').textContent = results.correctAnswers;
    document.getElementById('incorrectAnswers').textContent = results.incorrectAnswers;
    document.getElementById('scorePercentage').textContent = results.scorePercentage + '%';
    
    // Create charts
    createTimeChart(results.timeSpent);
    createPieChart(results.correctAnswers, results.incorrectAnswers);
});

// Create bar chart for time spent per question
function createTimeChart(timeSpent) {
    const ctx = document.getElementById('timeChart').getContext('2d');
    
    const labels = timeSpent.map((time, index) => `Q${index + 1}`);
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Time Spent (seconds)',
                data: timeSpent,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Time (seconds)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Questions'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            }
        }
    });
}

// Create pie chart for correct vs incorrect
function createPieChart(correct, incorrect) {
    const ctx = document.getElementById('pieChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Correct Answers', 'Incorrect Answers'],
            datasets: [{
                data: [correct, incorrect],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(255, 99, 132, 0.6)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

