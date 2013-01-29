The Verhoeff Checksum Algorithm
===============================

For a detailed discussion, see: http://www.cs.utsa.edu/~wagner/laws/verhoeff.html

Jacobus Verhoeff studied human transcription errors and determined that very few categories of errors make up the vast majority of mistakes. Single errors ('1' becomes '2'), adjacent transcription ('12' becomes '21'), and ommiting or adding a digit can account for all but a small percent in many circumstances.

Jacobus figured out that he could use the operation of what's known as the 'dihedral group D5', which derives from the symmetries of a pentagon, and can be represented as the digits 0 through 9, to generate a checksum of the digits. The properties of this operation, in particular the fact that multiplication in the group is defined such that it is non-commutative, resulted in the creation of an algorithm that could detect all single errors and adjacent transcriptions along with the vast majority (>90%) of cases of several other common categories listed by Verhoeff.

It is really quite powerful and not that hard to implement, given the correct tables provided by Verhoeff's efforts.

Usage
-----

> $ ./verhoeff.py -h
> usage: verhoeff.py [-h] [-v] N [N ...]
> 
> By default, calculate a Verhoeff checksum for a number. With the '-d'
> argument, instead validate a Verhoeff checksummed value.
> 
> positional arguments:
>   N               integer to calculate or validate the Verhoeff checksum of
> 
> optional arguments:
>   -h, --help      show this help message and exit
>   -v, --validate  validate the integer's Verhoeff checksum (default: calculate
                  the Verhoeff checksum)

TODO
----

* Include tests that cover basic checksumming and checking, all single errors, and all adjacent transcriptions
* Implement the error correcting code that's based on Verhoeff's algorithm

Why Write This?
---------------

In late 2011 I heard about the Verhoeff Checksum Algorithm from a colleague. Further, he mentioned that others had built his algorithm up to an error correcting code (the algorithm for this modification, apparently stuck behind a paywall, is not something I've yet looked into).

We were in the middle of trying to solve a problem about how to reliably instruct clients to provide a key account number with their wire deposits. Clients had to provide the number to a bank representative who would manually transcribe it into the wire deposit instructions.

The possibility of two manual transcriptions (first by the client from our site, then by the bank rep) and the strange realities of the bank wire system meant that the numbers we received with the wires were often incorrect. We thought that if we provided a Verhoeff-checksummed version of the account number, we could improve reliability. For a proof of concept, I stayed late in the office a couple of weeks later and figured out enough about the algorithm to build this python implementation.

There are a number of existing implementations in python, but this one is mine. While we haven't yet scheduled inclusion of Verhoeff checksummed data in our product, it was fun to build this up from a description of the algorithm.
