1️⃣ Hold-Out Cross Validation
What it is

The dataset is split only once into two parts:

Training set

Testing set

Steps

Take the full dataset.

Split it into training data (e.g., 70% or 80%).

Use the remaining data (30% or 20%) as test data.

Train the model on the training set.

Evaluate the model on the test set.

Example

Total data = 100 samples

Training = 80 samples

Testing = 20 samples

Advantages

✔ Very simple
✔ Fast computation

Disadvantages

❌ Performance depends on one single split
❌ Unreliable for small datasets

2️⃣ K-Fold Cross Validation
What it is

The dataset is divided into K equal parts (folds).
The model is trained K times.

Steps

Split the dataset into K folds (e.g., K = 5).

Choose one fold as the test set.

Use the remaining K−1 folds as the training set.

Train the model and evaluate it.

Repeat steps 2–4 until every fold is used once as test data.

Take the average performance of all K runs.

Example (5-Fold)

Fold 1 → test, Fold 2–5 → train

Fold 2 → test, Fold 1,3,4,5 → train

… continue till Fold 5

Advantages

✔ Better performance estimation
✔ Uses all data for training and testing

Disadvantages

❌ More computation than hold-out

3️⃣ Leave One-Out Cross Validation (LOOCV)
What it is

A special case of K-Fold where

K = number of data points

Steps

Take one data point as test data.

Use all remaining data points as training data.

Train the model and test it.

Repeat this process for every data point.

Average all results.

Example

If dataset has 100 samples:

1 sample → test

99 samples → train

Total models trained = 100

Advantages

✔ Uses maximum training data
✔ Very low bias

Disadvantages

❌ Extremely slow for large datasets
❌ High computational cost

4️⃣ Stratified K-Fold Cross Validation
What it is

An improved version of K-Fold that maintains class proportion in every fold.

Why needed?

Used when the dataset is imbalanced (one class appears much more than others).

Steps

Divide the dataset into K folds.

Ensure each fold has the same class ratio as the full dataset.

Select one fold as test data.

Use the remaining folds as training data.

Repeat until all folds are used as test data.

Average the results.

Example

Original dataset:

Class A = 90%

Class B = 10%

Each fold will also contain:

~90% Class A

~10% Class B

Advantages

✔ Reliable for imbalanced datasets
✔ Better evaluation metrics

Disadvantages

❌ Not suitable for time-series data

5️⃣ Monte Carlo Cross Validation (Random Sampling)
What it is

The dataset is randomly split multiple times into training and testing sets.

Steps

Randomly split the dataset into training and test sets.

Train the model and evaluate it.

Repeat the random split many times.

Calculate the average performance.

Example

Train = 80%, Test = 20%

Repeat this random split 20–50 times

Run 1 → random 20% test
Run 2 → another random 20% test
Run 3 → again random 20% test
...
...
...

Advantages

✔ Flexible train-test sizes
✔ More robust than single hold-out

Disadvantages

❌ Some samples may never be tested
❌ Results vary if random seed not fixed

🔑 Summary Table
Method	Main Idea	Best Use Case
Hold-Out	One split	Large datasets
K-Fold	K equal splits	General ML problems
LOOCV	One sample test	Very small datasets
Stratified K-Fold	Balanced folds	Imbalanced datasets
Monte Carlo	Random splits	Flexible evaluation