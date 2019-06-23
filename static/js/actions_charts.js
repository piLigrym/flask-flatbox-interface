$( document ).ready(function() {
    // init events
    $('#formShow').on("submit", show);
});


function show() {
    let dtEnd = $('#dtEnd').val();
    let dtStart = $('#dtStart').val();
    let sensor = $('#sensor option:selected').val();

    $.ajax({
        type: "GET",
        url: "/climate/temperature",
        data: {'dtEnd': dtEnd, 'dtStart': dtStart, 'sensor': sensor},
        success: function (data) {
            try {
                let divChart = $('#divChart');
                divChart.empty();
                let canvas =  $('<canvas></canvas>');
                new Chart(canvas, {
                    type: 'line',
                    data: {
                        labels: data['date'],
                        datasets: [{
                            label: 'Temperature, C',
                            yAxisID: 'A',
                            data: data['temperature'],
                            borderColor: "#FF8033",
                            fill: false


                        }, {
                            label: 'Humidity',
                            yAxisID: 'B',
                            data: data['humidity'],
                            borderColor: "#4d74ff",
                            fill: false


                        }]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'Temperature, C, sensor - ' + sensor
                        },
                        scales: {
                            yAxes: [
                                {
                                    id: 'A',
                                    type: 'linear',
                                    position: 'left',
                                },
                                {
                                    id: 'B',
                                    type: 'linear',
                                    position: 'right',
                                }
                            ],
                            xAxes: [{
                                ticks: {
                                    autoSkip: true,
                                    maxTicksLimit: 5,
                                    display: false
                                }
                            }]
                        }
                    }
                });

                divChart.append(canvas);
            }
            catch (e) {
                alert('Влзникла ошибка при обработке данных!');
                console.log(e)
            }

        },
        error: function (error) {
            alert('Возникла ошибка, попробуйте позже!');
            console.log(error);
        }
    });
    return false;
}