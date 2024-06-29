# Summary of findings.

## Statistic 1
**Accuracy achieved:**
100% accuracy achieved

**Description of model weights:**
it weighs heavily where the 1 is in the permutation. Specifically, if 1 is the fifth element in the permutation

**How to compute statistic:**
if index 5 of the permutation is a 1, then the permutation is valid, else it is invalid.


## Statistic 2
**Accuracy achieved:**
100% accuracy achieved

**Description of model weights:**
it heavily weighs the last two elements in the permutation. Specifically, having a large number in index 4 and small number in index 5. 

**How to compute statistic:**
If index 4 > index 5, then the permutation is valid. 


## Statistic 3
**Accuracy achieved:**
83%

**Description of model weights:**
it heavily weighs 3 at the third index and 4 at the fourth index. 

**How to compute statistic:**
I can't figure this one out.

## Statistic 4
**Accuracy achieved:**
100% accuracy

**Description of model weights:**
it heavily weighs each number at its corresponding index. i.e. 1 at 1, 2 at 2, three at 3, etc....

**How to compute statistic:**
A permutation is valid if for every index i, permutation[i] != i. example:
54213 is valid since every number isn't at its index
54312 is not valid since 3 is the third digit

## Statistic 5
**Accuracy achieved:**
I wasn't able to get accuracy on this one

**Description of model weights:**
Seems like it weighs numbers in reverse order

**How to compute statistic:**

## Statistic 6
**Accuracy achieved:**
26% accuracy

**Description of model weights:**
it heavily weighs not having a 4 in one of the last two integers when working with permutations of 6. doesn't want a 5,6 in early spots in the permutation aswell. 

**How to compute statistic:**
not sure
## Statistic 7
**Accuracy achieved:**
Accuracy for class 1 = 57.142857142857146%
Accuracy for class 2 = 37.93103448275862%
Accuracy for class 3 = 32.142857142857146%
Accuracy for class 4 = 60.0%

**Description of model weights:**
weights heavily having low numbers as the first element and large numebrs as the last element. 
**How to compute statistic:**

## Statistic 8
**Accuracy achieved:**
83%

**Description of model weights:**
The weights seem pretty feint. It seems like it weights 4 as the third element in permutations of 5 heavily, as well as having the first and last digits in their respective spots. 

**How to compute statistic:**
idk

## Statistic 9
**Accuracy achieved:**
80% accuracy

**Description of model weights:**
it weights having the first element at the start of the permutation, and heavily weighs not having it at the last two indexes of the permutation. seems to be in ascending order. 
**How to compute statistic:**
idk