

# TITLE: Analysis of CPU performance for various architectures and cores
## Team Members:Thomas Wright
## Date: 12/10/20

# Probelm Statement and Motivation
This project is aimed to look at how well modern day CPU's are scaling with multithreaded processes with multiple cores. This can help us see if adding additional cores to the CPU is giving the end users a tangible benefit. We can break down the differences between CPU's by architecture, generation, manufacturing size and logical cores. All this information will help us see exactly what attributes most greatly help CPU performance in a multithreaded application and at what price points cpus have the most performance.

# Introduction and Description of Data
Visualizing and relating the data to itself can emphasize trends which could show which CPU design features are more impactful for CPU performance. The issue with this methods is it is hard to isolate cpu features so working with a large dataset of CPU's could help keeping some variables reasonably similar. This data could be used to see what features you are looking for in a CPU or to gauge when the best time to purchase a cpu is or which brand of cpu would be the best to purchase.

# Literature Review/Related Work 
A good source of information on how linear regression works in python - https://realpython.com/linear-regression-in-python/

# Modeling Approach
The first iterations of models that were used for RandomForestClassifer, I choose this model for its ability to determine the importance of attributes. This was helpful for future model building as it allowed me to exclude those properties to make the future models simpler.
I ended up with a linear regression model as it had the seemingly best accuracy compared to all the other models that I tested.

# Project Trajectory, Results, and Interpretation 
The projects definitely changed scope over time. When I created the dataset there was a lot of categorical data that would have a hard time translating into numerical data that a model could really work with. I had to prune some features that I wanted like being able to compare different generations of CPUs together. I also found building a large dataset structure takes a lot of work so in the end the dataset ended up under 1000 entries which wasn't ideal for a real experiment but it allowed for the project to progress faster with less time spent training models or downloading data. For a school project I think this is fine but ideally you would work with a premade dataset or create a larger one yourself.

My results were pretty much expected if you know much about how CPUs work. Basically adding more cores and threads to a cpu improves it multithreading capabilities. This can be seen by messing with the cpu configurator on the website.

This information doesn't really mean much in the long term as the field of cpu performance is heavily studied already and engineers at amd and intel have vastly more knowledge about these topics. I think this project can help some people who are less familiar with tech either find a good CPU or be able to understand how some of the features affect performance.

# Conclusions and Future Work
If I were to attempt this project again I would spend much more time on training the models and building up a clean dataset as these bases are very important as you build off these when making graphs and conclusions.

# References:
The scikit-learn website was invalubale when workin with the models. https://scikit-learn.org/stable/index.html

# Support Materials
All of the data from this project was sourced from www.cpubenchmark.net.

# Declaration of academic integrity and responsibility

In your report, you should include a declaration of academic integrity as follows:

```
With my signature, I certify on my honor that:

The submitted work is my and my teammates' original work and not copied from the work of someone else.
Each use of existing work of others in the submitted is cited with proper reference.
Signature: __Thomas_Wright____ Date: ____12/10/20_____
```

# Credit
The above project template is based on a template developed by Harvard IACS CS109 staff (see https://github.com/Harvard-IACS/2019-CS109A/tree/master/content/projects).
