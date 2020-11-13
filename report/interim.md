# TITLE: Analysis of CPU performance for various architectures and cores
## Team Members: Thomas Wright
## Date: 11/12/2020

# Project Description
## Probelm Statement and Motivation
This project is aimed to look at how well modern day CPU's are scaling with multithreaded processes with multiple cores. This can help us see if adding additional cores to the CPU is giving the end users a tangible benefit. We can break down the differences between CPU's by architecture, generation, manufacturing size and logical cores. All this information will help us see exactly what attributes most greatly help CPU performance in a multithreaded application and at what price points cpus have the most performance.

## Introduction and Description of Data
Visualizing and relating the data to itself can emphasize trends which could show which CPU design features are more impactful for CPU performance. The issue with this methods is it is hard to isolate cpu features so working with a large dataset of CPU's could help keeping some variables reasonably similar. This data could be used to see what features you are looking for in a CPU or to gauge when the best time to purchase a cpu is or which brand of cpu would be the best to purchase.

## Literature Review/Related Work 
A good source of information on how linear regression works in python - https://realpython.com/linear-regression-in-python/

## Interim Results
If you have some interim results or new findings, you can include them here.

# Project Progress
The development server for this project is hosted on a freebsd machine as it what I had on hand and I wanted to have a local development environment. It was a process learning how to build some of the tools to work on this OS but luckily I was able to build jupyter and all my dependieces fine. The first step was to store data in a MySQL database but as I have been mostly testing with csv files and they seem to work well with the size of my datasets so I will be switching to using those instead of using a mySQL server. The data has all been gathered and has the ability to be redownloaded although this took considerably more work then I had anticipated due to the website www.cpubenchmark.net obfuscation of their data. I will soon be starting to build models and put them into a web application using flask. Finally The computing and storage requirements should still be relatively small as my dataset is not massive and there should be little traffic


# References:
For CPU specifications and information the website www.techpowerup.com has a vast database of this information which can be scraped.
For CPU performance results www.cpubenchmark.net has CPU's listed with their respective performance metrics in single and multithreaded core tests. While this website uses an arbitrary score for it's test the values should be consistent throughout the website.
