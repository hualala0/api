var mychart = echarts.init(document.getElementById('mychart'));
$(".btn").bind("click",function () {
    $.ajax({
        type: "post",
        data: {uname: $(this).parent().prev().prev().text(), pname: $(this).parent().prev().text()},
        success: function (data) {
            var pdata = JSON.parse(data);
            var year = 2019;
            var date = +echarts.number.parseDate(year + '-01-01');
            var end = +echarts.number.parseDate((year + 1) + '-01-01');
            var dayTime = 3600 * 24 * 1000;
            var data1 = [];
            //console.log(pdata);
            for (var time = date; time < end; time += dayTime) {
                data1.push([
                    echarts.format.formatTime('yyyy/MM/dd', time),
                    0
                ]);
                for (var i = 0; i < pdata.length; i++) {
                    if (echarts.format.formatTime('yyyy/MM/dd', time) === pdata[i][0]) {
                        data1.pop();
                        data1.push(pdata[i]);
                        break;
                    }
                }
            }
            option = {
                title: {
                    top: 30,
                    text: 'api访问次数',
                    left: 'center',
                },
                tooltip : {
                    trigger: 'item'
                },
                legend: {
                    top: '30',
                    left: '100',
                    data:['访问次数'],
                },
                calendar: [{
                    top: 100,
                    left: 'center',
                    range: ['2019-01-01', '2019-6-30'],
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#000',
                            width: 4,
                            type: 'solid'
                        }
                    },
                    yearLabel: {
                        formatter: '{start} 1nd',
                    },
                    itemStyle: {
                        normal: {
                            color: '#323c48',
                            borderWidth: 1,
                            borderColor: '#111'
                        }
                    }
                },
                {
                    top: 280,
                    left: 'center',
                    range: ['2019-07-01', '2019-12-31'],
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#000',
                            width: 4,
                            type: 'solid'
                        }
                    },
                    yearLabel: {
                        formatter: '{start} 2nd',

                    },
                    itemStyle: {
                        normal: {
                            color: '#323c48',
                            borderWidth: 1,
                            borderColor: '#111'
                        }
                    }
                }],
                series : [
                    {
                        name: '访问次数',
                        type: 'scatter',
                        coordinateSystem: 'calendar',
                        data: data1,
                        symbolSize: function (val) {
                            return val[1] / 5;
                        },
                        itemStyle: {
                            normal: {
                                color: '#ddb926'
                            }
                        }
                    },
                    {
                        name: '访问次数',
                        type: 'scatter',
                        coordinateSystem: 'calendar',
                        data: data1,
                        calendarIndex: 1,
                        symbolSize: function (val) {
                            return val[1] / 5;
                        },
                        itemStyle: {
                            normal: {
                                color: '#ddb926'
                            }
                        }
                    }
                ]
            };
            mychart.setOption(option);

        }
    })
});

