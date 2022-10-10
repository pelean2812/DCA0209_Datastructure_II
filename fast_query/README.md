# Building Fast Queries

This is an adaptation of this [original solution](https://github.com/dataquestio/solutions/blob/master/Mission481Solution.ipynb). But now, we're analysing [this](https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset) dataset, that have 4GB of size!

The things that we're done in this project are:

- 1) Given an id of a message on Reddit, return all information about the message

- 2) Given a lower and upper bound of the "sentiment" column, return all messages with sentiment values ​​between the lower and upper bounds

- 3) Given a parameter value, return two messages whose sum of the value of the "score" column is equal to the parameter. Return -1 if it doesn't exist

- 4) Implement tests with pytest for validation purposes.

At the end of this projects, we can see how powerfull is use python dictionaries for the third item. Without dictionaries, it takes near two minutes to verify 100 random sum target values, but using dictionaries, it is almost instantaneous!!!

You can see my solution [here](https://github.com/pelean2812/DCA0209_Datastructure_II/blob/main/fast_query/fast_query.ipynb).

## Group
- Pedro Leandro Batista Marques
- Efrain Marcelo Pulgar Pantaleon
