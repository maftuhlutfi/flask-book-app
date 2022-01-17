const genreCanvas = document.getElementById('genre-chart');
const genreChart = new Chart(genreCanvas, {
    type: 'pie',
    data: {
        labels: genreData.map(g => g.label),
        datasets: [{
            label: 'Total books',
            data: genreData.map(g => g.value),
            backgroundColor: [
                '#FF0000',
                '#FF4D00',
                '#FF7400',
                '#FF9A00',
                '#FFC100'
            ],
            borderColor: new Array(5).fill('#ffffff'),
            borderWidth: 2
        }]
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom',
                align: 'start',
                labels: {
                    font: {
                        size: 14
                    }
                },
            }
        }
    }
});

const pubYearCanvas = document.getElementById('pub-year-chart');
const pubYearChart = new Chart(pubYearCanvas, {
    type: 'bar',
    data: {
        labels: publishedDateData.map(p => p.label),
        datasets: [{
            label: 'Total books',
            data: publishedDateData.map(p => p.value),
            backgroundColor: [
                '#FF0000',
                '#FF4D00',
                '#FF7400',
                '#FF9A00',
                '#FFC100'
            ],
            borderColor: new Array(5).fill('#ffffff'),
            borderWidth: 2,
            borderRadius: 50,
            barThickness: 30
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false
            }
        }
    }
});

const ratingCanvas = document.getElementById('rating-chart');
const ratingChart = new Chart(ratingCanvas, {
    type: 'bar',
    data: {
        labels: ratingsData.map(r => `${r.label}-${r.label + 1}`),
        datasets: [{
            label: 'Total books',
            data: ratingsData.map(r => r.value),
            backgroundColor: [
                '#FF0000',
                '#FF4D00',
                '#FF7400',
                '#FF9A00',
                '#FFC100'
            ],
            borderColor: new Array(5).fill('#ffffff'),
            borderWidth: 2,
            borderRadius: 50,
            barThickness: 30
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false
            }
        }
    }
});

const languageCanvas = document.getElementById('language-chart');
const languageChart = new Chart(languageCanvas, {
    type: 'pie',
    data: {
        labels: languagesData.map(l => l.label),
        datasets: [{
            label: 'Total books',
            data: languagesData.map(l => l.value),
            backgroundColor: [
                '#FF0000',
                '#FF4D00',
                '#FF7400',
                '#FF9A00',
                '#FFC100'
            ],
            borderColor: new Array(5).fill('#ffffff'),
            borderWidth: 2
        }]
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom',
                align: 'start',
                labels: {
                    font: {
                        size: 14
                    }
                },
            }
        }
    }
});