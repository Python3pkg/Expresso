# Expresso/PyCAS

## Expresso
A c++11 symbolic expression manipulation library with wrappers for python 2.7. It it based on pattern matching and expression rewriting.

### Installation
Installing the latest realease of Expresso can be done by cloning directly from the repository:

        git clone https://github.com/TheLartians/Expresso.git
        pip2 install .

Please be aware that the core of expresso uses c++11 and therefore needs a relatively new compiler (e.g. gcc-4.9).

## PyCAS
PyCAS is a minimalistic computer algebra system based on expresso (it also serves as an example for writing your own modules with expresso). Since it is developed in parallel it is distributed inside the expresso module as expresso.pycas. In the examples directory you can find an introductory tutorial for PyCAS.

## Citing Expresso/PyCAS
When using Expresso in your work it would be very appriciated to give us a citation. You can use the following BibTeX template:

    @misc{LMExpresso2016,
      author = {Lars Melchior},
      title = {Expresso},
      year = {2016},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/TheLartians/Expresso/}},
      commit = {61e097b9c895b885d69d813b8fde1bb935b03557}
    }
## Outlook
There are still many possible improvements to expresso/pyCAS. Feel free to fork the project and add your own contributions:

### Expresso:
- Match an arbitrary number of patterns at once in even faster time (near constant instead of logarithmic) using a lookup table
- Add support for full commutative patterns (at the moment only the outermost function is matched commutatively)
- Add documentation

### PyCAS:
- Implement algorithms for factoring polynomials
- Add support for integrals using a heuristic risch algorithm 
