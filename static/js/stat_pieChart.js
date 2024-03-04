const ctx2 = document.getElementById('doughnutChart').getContext('2d');
const pieChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Orange'], // Corrected labels
        datasets: [{
            label: 'My First Dataset',
            data: [65, 59],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Set background color of the chart canvas
document.getElementById('doughnutChart').style.backgroundColor = 'black';