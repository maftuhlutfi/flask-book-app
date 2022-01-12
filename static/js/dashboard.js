const genreCanvas = document.getElementById('genre-chart');
const genreChart = new Chart(genreCanvas, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2],
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
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2],
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
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2],
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
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2],
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