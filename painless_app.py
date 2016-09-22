from bokeh.embed import components
from bokeh.plotting import figure
from flask import Flask, render_template
painless_app = Flask(__name__)
#import requests
	
@painless_app.route("/")
def init_app():
	plot = figure(title = 'Data from Quandle WIKI set',
					x_axis_label='date',
					x_axis_type='datetime')
	plot.scatter(x=[1,2,3],y=[1,2,3],size=12,color='red')

					
	script, div = components(plot)
	greeting = "Hey there, sexy"
	return render_template('graph2.html', 
							script=script, 
							div=div, greeting=greeting)
									
if __name__ == '__main__':
	painless_app.run()