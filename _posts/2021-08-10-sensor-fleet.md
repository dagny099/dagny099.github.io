---
layout: post
classes: wide
title: "Sensor Fleet"
subtitle: "Building an Arduino-powered IoT fleet to track temperature and optimize home cooling costs"
date: 2021-08-10
last_modified_at: 2026-11-09
permalink: /blog/sensor-fleet-intro/
redirect_from:
  - /temp-sensor-00/
  - /data science/sensor-fleet/
  - /series/sensor-fleet/
  - /blog/sensor-fleet-part-1/
  - /blog/sensor-fleet-part-2/
  - /blog/sensor-fleet-part-3/
  - /blog/sensor-fleet-part-4/
  - /blog/sensor-fleet-part-5/
  - /blog/sensor-fleet-part-6/
  - /temp-sensor-01/
  - /temp-sensor-02/
  - /temp-sensor-03/
  - /temp-sensor-04/
  - /temp-sensor-05/
  - /temp-sensor-06/
header:
  overlay_image: "/assets/images/tempsensor_pic_th.jpg"
excerpt: "A 2021 build: Arduino-powered temperature sensors that collect heating and cooling data from different rooms for under $25 each, with MQTT messaging, a MySQL database, and a dashboard."
tags: [arduino, temp-sensor, mqtt, iot]
stack: [Arduino, MQTT, MySQL, Python]
categories: [data science]
---
# Story
## What's my motivation?
Texas is HOT. ACs work overtime and electricity bills soar. In a nutshell, this was the motivation for wanting to see how cheaply and easily I could build a small temperature sensor to collect heating and cooling data from different rooms in the house. This has been a really fun project and taught me **a lot**, including how to program an Arduino, design a lightweight data pipeline, and build a visualization dashboard to see my data.

This project is a fun thing to do as a useful DIY project, for those interested in building "something that works" fairly quickly and easily.

Aspiring data scientists are another potential audience for this project, because it's great practice in thinking through the steps of a problem while generating your own (useful!) dataset.

## Here's the goal
The goal was a fleet of temperature sensors I could place around the house. The most important requirements were:
* **Cost**. I wanted each sensor to cost less than the cheapest commercially available sensor (roughly $25 at the time of writing).
* **Accessible**. I wanted to be able to access sensor readings remotely, i.e. outside of local Wifi network.
* **Lightweight**. Not the most precise of specifications, but basically I wanted the whole project to use the smallest tools necessary for the job and as few lines of code as necessary. *(Disclaimer: I'm still circling this target, as I learn more efficient ways and tools for accomplishing the task)*

## How the build was laid out
The plan had five stages:

1. **Build a sensor, publish the data:** an Arduino publishes temperature readings over MQTT, and a subscriber writes them to a MySQL database.
2. **Grow the fleet, view the data:** add sensors, check that each one keeps reporting, and chart the readings in a small web app.
3. **Automate the pipeline:** schedule ingestion with crontab and move the project onto an AWS instance.
4. **Add local weather:** pull outdoor temperature from a NOAA weather station to compare with the indoor readings.
5. **Address security:** run my own MQTT broker and put a password on the web app.
