# TITLE: Analysis of CPU performance for various architectures and cores
## Team Members: Thomas Wright
## Date: 10/22/2020

# Project Description
## Problem Statement and Motivation
This project is aimed to look at how well modern day CPU's are scaling with multithreaded processes with multiple cores. This can help us see if adding additional cores to the CPU is giving the end users a tangible benefit. We can break down the differences between CPU's by architecture, generation, manufacturing size and logical cores. All this information will help us see exactly what attributes most greatly help CPU performance in a multithreaded application.
.

## Introduction and Description of Data
Visualizing and relating the data to itself can emphasize trends which could show which CPU design features are more impactful for CPU performance. The issue with this methods is it is hard to isolate cpu features so working with a large dataset of CPU's could help keeping some variables reasonably similar. This data could be used to see what features you are looking for in a CPU or to gauge when the best time to purchase a cpu is.


# Plan
The end plan is to be able to automate graphs of performance vs CPU features and have this hosted on a website. Linear regressions of some of the data should also be available. The first step would be to store data in a MySQL database, possibly with a webui like phpmyadmin to look at the database with ease. Then I will set up a web application(flask or django) to be able to look at a simple graph of the data and make sure all components of the project interface with each other. Lastly would be to create the python functions to sanitize and graph the data properly with user input. The computing and storage requirements should be relatively small considering I am only including modern cpus and there should be very little user traffic. 


# References:
For CPU specifications and information the website www.techpowerup.com has a vast database of this information which can be scraped.
For CPU performance results www.cpubenchmark.net has CPU's listed with their respective performance metrics in single and multithreaded core tests. While this website uses an arbitrary score for it's test the values should be consistent throughout the website.


