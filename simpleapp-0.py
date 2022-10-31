from asyncio.windows_events import _WindowsSelectorEventLoop
from cgitb import text
import justpy as jp

def app(): # Name of our choice
    wp = jp.QuasarPage() 
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    return wp


jp.justpy(app)