---
layout: single
title: "Sensor Fleet"
permalink: /temp-sensor-00/
header:
  overlay_image: "/assets/images/tempsensor_pic_th.jpg"
excerpt: "Environment Sensing, Visualizing"
tags: [arduino, temp sensor, mqtt]
categories: [data science]
---
## What's my motivation?
Texas is HOT. ACs work overtime and electricity bills soar. In a nutshell, this was the motivation for wanting to see how cheaply and easily I could build a small temperature sensor to collect heating and cooling data from different rooms in the house. This has been a really fun project and taught me **a lot**, including how to use to program an Arduino, design a lightweight data pipeline, and build a visualization dashboard to see my data.

This project is a fun thing to do as a useful DIY project, for those interested in building "something that works" fairly quickly and easily. See Parts 1-2.

Aspiring data scientists are another potential audience for this project, because it's great practice in thinking through the steps of a problem while generating your own (useful!) dataset. See Parts 1-5.

## Here's the goal
In this series, we'll be building a fleet of temperature sensors that you can deploy and place around the house. The constraints will be clarified later but the most important requirements were:
* **Cost**. I wanted each sensor to cost less than the cheapest commercially available sensor (roughly $25 at the time of writing).
* **Accessible**. I wanted to be able to access sensor readings remotely, i.e. outside of local Wifi network.
* **Lightweight**. Not the most precise of specifications, but basically I wanted the whole project to use the smallest tools necessary for the job and as few lines of code as necessary. *(Disclaimer: I'm still circling this target, as I learn more efficient ways and tools for accomplishing the task)*

## Description
Here's a summary of what each post in the series will comprise:

### Part 1: Build a sensor, Publish the data
After this post, you'll be able to:
* Publish temperature sensor measurements powered by an Arduino
* Read the sensor readings using the MQTT protocol
* Create a mysql database to store the measurements
* Write incoming measurements to the database

### Part 2: Grow the fleet, View the data
After this post, you'll be able to:
* Add additional sensors to your fleet
* Monitor and detect your fleet is working as expected
* Create a Heroku web app to visualize the data
* Create an interactive graph to visualize the smoothened data measurements.

### Part 3: Data Pipeline, automated
After this post, you'll be able to:
- Automate data ingestion (hello, crontab)
- Deploy the project on AWS instance (optional but nice)

### Part 4: Insight Generation with Local Weather
After this post, you'll be able to:
- Query a NOAA based weather station to pull local weather data
- Add outdoor temp as a feature to optionally display on your dashboard

### Part 5: Address Security Concerns
After this post, you'll be able to:
- Create your own MQTT broker
- Add a password to your webapp

### Part 6: Streaming with Kafka
So far, the realtime part of this has been klugy. Let's do this for real with Apache Kafka.
[In development]

Link to [next post](/temp-sensor-01/) in the series.
