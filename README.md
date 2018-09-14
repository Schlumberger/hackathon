# Schlumberger Hackathon Challenge

## Challenge

Ask an engineer how to improve an application, and they will likely say, "give me a way to see MORE DATA". Surveillance engineers may analyze output from a dozen or more sensors in the same visualization.​

Line charts are the default choice for this workflow, but they are cumbersome, especially if the data streams have different scaling and units.  And as IIoT becomes pervasive at the wellsite, this problem will only grow.​

Show us how to do it better!

Deliver a web application to display/query/analyze time-series data from downhole equipment in innovative ways.​​

## Requirements
 * [Python](https://www.python.org/)
 * [Flask](http://flask.pocoo.org/)
 * [Node.js](https://nodejs.org/en/download/)
 * [Angular CLI](https://cli.angular.io/)

## Launch Application
 - Go to directory **backend**
 - run  `python server.py`
 - Go to directory **frontend**
 - run  `npm install`
 - run `npm start`
 - Browse to  [http:\\\localhost:4200](http:localhost:4200)

 ## Use the APIs
 - API 1:
	- GET: /devices
		- Description: list all different devices in the dataset
		- Sample Response:
			- [
				"IC01",
				"ESP03",
				"ESP01",
				"ESP02",
				"IC02"	
			  ]
	- GET: /sensors?deviceid=IC01
		- Description: get all sensors/measurements available for a particular device
		- Required query parameter: deviceid
		- Sample Response:
			- [
				"CHOKE_POSITION",
				"PRESSURE1",
				"PRESSURE2",
				"TEMPERATURE1",
				"TEMPERATURE2",
				"WATER_CUT",
				"LIQUID_RATE",
				"WATER_RATE",
				"OIL_RATE"
			  ]
	- GET: /timeseries?deviceid=IC01&sensor=OIL_RATE
		- Description: get time series data (time/value pairs) for device/sensor combo
		- Required query parameters: deviceid, sensor
		- Sample Response:
			- {"equipment": "IC01", "sensor": "OIL_RATE", "unit": "bbl/d", "datapoints": [{"timestamp": 1370044800, "value": 0.0},..]}