function renderChart(data) {
    const ctx = document.getElementById('adherenceChart');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            backgroundColor: "rgba(54, 162, 235, 0.6)",
            borderColor: "rgba(54, 162, 235, 1)",

            datasets: [{
                label: 'Adherence %',
                data: data.values
            }]
        }
    });
}