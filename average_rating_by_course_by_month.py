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
        type: 'spline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2021'
    },
    subtitle: {
        align: 'center',
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        plotBands: [{ // Highlight the two last years
            from: 20,
            to: 25,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: []
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