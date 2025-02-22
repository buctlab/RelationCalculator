# Installation Guide

## Dependencies

Before installing and running the RelationCalculator package, you need to ensure the following dependencies are installed:

- Python 3.8 or higher version
- NumPy 1.18 or higher version
- Matplotlib 3.2 or higher version

## Installing Dependencies

If you have not installed these dependencies yet, you can use the following pip command to install them.

If you are managing your system with pip, please use the following command:

```bash
pip install numpy matplotlib
```

Please note, if you have multiple versions of Python in your system, you may need to use `pip3` instead of `pip`.

or if you are managing your system with Conda, please use the following command:

```
conda install numpy matplotlib
```

## Use the following command to install RelationCalculator

If you are managing your system with pip, please use the following command:

```
pip install RelationCalculator
```

or if you are managing your system with Conda, please use the following command:

```
conda install -c ioea_lab relationcalculator
```



# Relationship Counting Software Package

## Module 1 : RelationsClass

### Class Name ：Relation

The `Relation` class is used to define a relation between elements. It takes two parameters in its constructor: `elements` and `relations`.

### Parameters

- `elements` (list, optional): A list of elements. If not provided, an empty list is created.
- `relations` (list of tuples, optional): A list of pairs of elements representing the relations between them. If not provided, an empty list is created.

### Description

The `elements` parameter is converted to a list if it is present; otherwise, an empty list is created. The `relations` parameter is a list containing pairs of elements representing the relations between them. When traversing the `relations` list, if an element in a pair does not exist in the `elements` list, it is added to the `elements` list. Then, the `add_relation` method is called to add the relation of the pair of elements, and this pair is added to the `relations_list` list. Finally, the `set_relation_matrix` method is called to set the relation matrix.

| Function Name       | Functionality                                                | Function Output            |
| :------------------ | ------------------------------------------------------------ | -------------------------- |
| add_relation        | Add an ordered pair to the current binary relation.          | None                       |
| set_relation_matrix | Calculate the matrix representation of the current binary relation. | Relation matrix (np.array) |
| count_relations     | Calculate the number of ordered pairs in the current binary relation. | Decimal number             |
| get_all_elements    | Get all elements in the current set.                         | list                       |
| get_all_relations   | Get all ordered pairs in the current binary relation.        | list                       |
| get_relation_matrix | Calculate the matrix representation of the current binary relation. | list                       |
| is_related          | Determine whether two elements are related.                  | true/false                 |
| isReflexive         | Determine whether the binary relation is reflexive.          | true/false                 |
| isIrreflexive       | Determine whether the binary relation is irreflexive.        | true/false                 |
| isSymmetric         | Determine whether the binary relation is symmetric.          | true/false                 |
| isAntisymmetric     | Determine whether the binary relation is antisymmetric.      | true/false                 |
| isTransitive        | Determine whether the binary relation is transitive.         | true/false                 |

### Class Name ：RelationDefineByMatrix

##### Primary member variables : Matrix m

| Function Name   | Functionality                                                | Function Output                    |
| :-------------- | ------------------------------------------------------------ | ---------------------------------- |
| matrix2num      | Convert the relational boolean matrix to a binary number representation. | Binary number (output as a string) |
| isReflexive     | Determine whether the binary relation represented by the relation matrix is reflexive. | true/false                         |
| isIrreflexitive | Determine whether the binary relation represented by the relation matrix is irreflexive. | true/false                         |
| isSymmetric     | Determine whether the binary relation represented by the relation matrix is symmetric. | true/false                         |
| isAntiSymmetric | Determine whether the binary relation represented by the relation matrix is antisymmetric. | true/false                         |
| isTransitive    | Determine whether the binary relation represented by the relation matrix is transitive. | true/false                         |

### Class Name ：RelationDefineByInt

#####  Variables: Decimal number n; number of set elements size

The `RelationDefineByInt` class is a subclass of the `Relation` class, designed for handling specific situations where relations are defined through integers. It takes two parameters in its constructor: `n` and `size`.

### Parameters

- `n` (int): An integer representing the binary representation of the relationship.
- `size` (int): Represents the size of the relationship matrix.

### Description

In the constructor, the integer `n` is first converted to a binary string, which is then padded to the square of `size` length with '0'. This binary string is then converted into a list of integers, which is reshaped into a `size` by `size` matrix. Finally, the constructor of the superclass is called to initialize the relationship with this matrix.

For example, if we have an integer 13 (binary representation is 1101), and we want to represent this relationship in a 2x2 matrix, we can do this:

```python
relation = RelationDefineByInt(13, 2)
```

This will create a relationship matrix as follows:

```python
[[1 1]
 [0 1]]
```

| Function Name   | Functionality                                                | Function Output            |
| :-------------- | ------------------------------------------------------------ | -------------------------- |
| num2matrix      | Convert the decimal number representation of a binary relation to a boolean matrix representation (relation matrix). | Relation matrix (np.array) |
| isReflexive     | Determine whether the binary relation represented by this positive integer is reflexive. | true/false                 |
| isIrreflexitive | Determine whether the binary relation represented by this positive integer is irreflexive. | true/false                 |
| isSymmetric     | Determine whether the binary relation represented by this positive integer is symmetric. | true/false                 |
| isAntiSymmetric | Determine whether the binary relation represented by this positive integer is antisymmetric. | true/false                 |
| isTransitive    | Determine whether the binary relation represented by this positive integer is transitive. | true/false                 |

### Some special features

| Function Name | Functionality                                           | Function Output            |
| :------------ | ------------------------------------------------------- | -------------------------- |
| logicMulti    | Perform logical multiplication on two boolean matrices. | Relation matrix (np.array) |

### Usage example

```python
from RelationCalculator import Relation,RelationDefineByInt

relation = Relation({'A','B','C'},[('C',6)])

relation.add_relation('A','B')
relation.add_relation('A','C')
relation.add_relation('B','C')

print(relation.count_relations()) #4

print(relation.is_related('A','C')) #True
print(relation.is_related('B','A'))  #False
print(relation.is_related('C',6))  #True

print(relation.get_all_elements()) #['A', 'B', 'C', 6]
print(relation.get_all_relations()) #[('C', 6), ('A', 'B'), ('A', 'C'), ('B', 'C')]

print(relation.isReflexive()) #False
print(relation.isIrreflexive()) #True
print(relation.isTransitive()) #False

print(relation.get_relation_matrix())
#[[0 1 1 0]
# [0 0 1 0]
# [0 0 0 1]
# [0 0 0 0]]

relation = RelationDefineByInt(511,3)

print(relation.get_all_elements()) #[1, 2, 3]
```





## Module 2 : CaculatorClass

### Class Name ：Calculator

#####  Variables: number of set elements

| Function Name                                                | Functionality                                                | Function Output                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- |
| count_all_relations                                          | Calculate the total number of relations on a set with size elements. | Decimal number                          |
| generate_all_relations                                       | Calculate the binary representation of all relations on a set with size elements. | Binary number (output as a string) list |
| generate_all_relations_as_matrices                           | Calculate the boolean matrix representation of all relations on a set with size elements. | Relation matrix list                    |
| count_reflexive_relations                                    | Calculate the total number of reflexive relations on a set with size elements. | Decimal number                          |
| generate_reflexive_relations                                 | Calculate the binary representation of reflexive relations on a set with size elements. | Binary number (output as a string) list |
| generate_reflexive_relations_as_matrices                     | Calculate the boolean matrix representation of reflexive relations on a set with size elements. | Relation matrix list                    |
| count_irreflexive_relations                                  | Calculate the total number of irreflexive relations on a set with size elements. | Decimal number                          |
| generate_all_irreflexive_relations                           | Calculate the binary representation of irreflexive relations on a set with size elements. | Binary number (output as a string) list |
| generate_irreflexive_relations_as_matrices                   | Calculate the boolean matrix representation of irreflexive relations on a set with size elements. | Relation matrix list                    |
| count_symmetric_relations                                    | Calculate the total number of symmetric relations on a set with size elements. | Decimal number                          |
| generate_all_symmetric_relations                             | Calculate the binary representation of symmetric relations on a set with size elements. | Binary number (output as a string) list |
| generate_symmetric_relations_as_matrices                     | Calculate the boolean matrix representation of symmetric relations on a set with size elements. | Relation matrix list                    |
| count_antisymmetric_relations                                | Calculate the total number of antisymmetric relations on a set with size elements. | Decimal number                          |
| generate_all_antisymmetric_relations                         | Calculate the binary representation of antisymmetric relations on a set with size elements. | Binary number (output as a string) list |
| generate_antisymmetric_relations_as_matrices                 | Calculate the boolean matrix representation of antisymmetric relations on a set with size elements. | Relation matrix list                    |
| count_reflexive_symmetric_relations                          | Calculate the total number of relations that are both reflexive and symmetric on a set with size elements. | Decimal number                          |
| generate_all_reflexive_symmetric_relations                   | Calculate the binary representation of relations that are both reflexive and symmetric on a set with size elements. | Binary number (output as a string) list |
| generate_reflexive_symmetric_relations_as_matrices           | Calculate the boolean matrix representation of relations that are both reflexive and symmetric on a set with size elements. | Relation matrix list                    |
| count_irreflexive_symmetric_relations                        | Calculate the total number of relations that are both irreflexive and symmetric on a set with size elements. | Decimal number                          |
| generate_all_irreflexive_symmetric_relations                 | Calculate the binary representation of relations that are both irreflexive and symmetric on a set with size elements. | Binary number (output as a string) list |
| generate_irreflexive_symmetric_relations_as_matrices         | Calculate the boolean matrix representation of relations that are both irreflexive and symmetric on a set with size elements. | Relation matrix list                    |
| count_nonreflexive_nonirreflexive_relations                  | Calculate the total number of relations that are neither reflexive nor irreflexive on a set with size elements. | Decimal number                          |
| generate_all_nonreflexive_nonirreflexive_relations           | Calculate the binary representation of relations that are neither reflexive nor irreflexive on a set with size elements. | Binary number (output as a string) list |
| generate_nonreflexive_nonirreflexive_relations_as_matrices   | Calculate the boolean matrix representation of relations that are neither reflexive nor irreflexive on a set with size elements. | Relation matrix list                    |
| count_nonreflexive_nonirreflexive_symmetric_relations        | Calculate the total number of symmetric relations that are neither reflexive nor irreflexive on a set with size elements. | Decimal number                          |
| generate_all_nonreflexive_nonirreflexive_symmetric_relations | Calculate the binary representation of symmetric relations that are neither reflexive nor irreflexive on a set with size elements. | Binary number (output as a string) list |
| generate_nonreflexive_nonirreflexive_symmetric_relations_as_matrices | Calculate the boolean matrix representation of symmetric relations that are neither reflexive nor irreflexive on a set with size elements. | Relation matrix list                    |
| count_transitive_relations                                   | Calculate the total number of transitive relations on a set with size elements. | Decimal number                          |
| generate_all_transitive_relations                            | Calculate the binary representation of transitive relations on a set with size elements. | Binary number (output as a string) list |
| generate_transitive_relations_as_matrices                    | Calculate the boolean matrix representation of transitive relations on a set with size elements. | Relation matrix list                    |
| count_partialOrder_relations                                 | Calculate the total number of partial order relations on a set with size elements. | Decimal number                          |
| generate_all_partialOrder_relations                          | Calculate the binary representation of partial order relations on a set with size elements. | Binary number (output as a string) list |
| generate_partialOrder_relations_as_matrices                  | Calculate the boolean matrix representation of partial order relations on a set with size elements. | Relation matrix list                    |
| count_quasiOrder_relations                                   | Calculate the total number of quasi-order relations on a set with size elements. | Decimal number                          |
| generate_all_quasiOder_relations                             | Calculate the binary representation of quasi-order relations on a set with size elements. | Binary number (output as a string) list |
| generate_quasiOder_relations_as_matrices                     | Calculate the boolean matrix representation of quasi-order relations on a set with size elements. | Relation matrix list                    |

### Some special features

| Function Name | Functionality                                                | Function Output |
| :------------ | ------------------------------------------------------------ | --------------- |
| plot_matrices | Convert the boolean matrix to a grayscale image for representation. | Image           |

### Usage example

```python
from RelationCalculator import Calculator,plot_matrices

c = Calculator(3)

print(c.count_all_relations()) #512

print(c.count_transitive_relations()) #171

plot_matrices(c.generate_transitive_relations_as_matrices(),9,19,"output.png")
```

