const ctx = document.getElementById('barChart').getContext('2d');
const barChart = new Chart(ctx, {
    type: 'bar',
    data: { // Added colon here
        labels: ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'ash'],
        datasets: [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40, 28],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'gbr(201, 203, 207)',
                'gbr(201, 203, 207)'
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
document.getElementById('barChart').style.backgroundColor = 'black';