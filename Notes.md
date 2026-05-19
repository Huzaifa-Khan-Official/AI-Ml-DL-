### we can calculate following from "confusion matrix"
1) Accuracy:
    Percentage of correct prediction
2) Precision:
    Out of all predicted positives, how many are actually positives
3) Recall:
    Out of all actual positives, how many did we correctly predicted
4) F1 score:
    Harmonic mean of precision and eracall

---


# Structure/Working of Decision Tree:
* Start with the data
* Choose the best feature
* make branches
* repeat the process for each branch
* Stop when:
    * All data is pure
    * Max depth is reaches

### Entropy Formula for output variable
    Entropy (s) = -P(+) log<sub>2</sub>P(+) - P(-) log<sub>2</sub>P(-)

### Information Gain Formula for output variable with respect to the feature
    Information Gain (IG) = Entropy(parent) - ∑(Weighted Entropy(children))

---

# Support Vector Machine (SVM)

### Kernel:
    When we use support vector machines, and the data is very difficult to separate linear labeling, we can use density and multidimentional, and in multidimentional we can use Hyperplane, and that is used with kernel.

### Hyperplane:
    A Line that separate two categories

### Margin:
    The space between the line and nearest point

### Support Vector:
    The closest ball to the margin that support the line
