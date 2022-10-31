from asyncio.windows_events import _WindowsSelectorEventLoop
from cgitb import text
import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
month_course_average_b = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    
    title: {
        floating: true,
        align: 'left',
        text: 'Winter Olympic Medal Wins'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Cancelled<br>during<br>World War II'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Soviet Union fell,<br>Germany united'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""
def app(): # Name of our choice
    wp = jp.QuasarPage() 
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options = chart_def)
    hc.options.xAxis.categories = list(month_course_average_b.index)

    hc.options.series = [{"name": course, "data": list(month_course_average_b[course])} for course in month_course_average_b.columns]
        
    return wp


jp.justpy(app)