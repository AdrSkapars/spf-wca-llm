# spf-wca-llm
SEE INFORMATION ABOUT PROJECT IN POSTER.PDF

----

Description of dataset's worst cases (find formal definitions under 'Dataset/z3_annotations'):

**SameHundred** - All elements except ss0 are ≥ 100\
**SameLowercase** - All characters are lowercase\
**SameString** - All characters are ‘x’\
**SameOnlyThird** - Exactly the third element is 0 and no constraints elsewhere

**SimpleAscendingLast** - Ascending order except that the last element is always the smallest\
**SimpleUnique** - All characters are unique from one another other\
**SimpleTrueFalse** - Alternating pattern of True then False then True …\
**SimpleSymmetric** - Matrix inputs must be symmetric \
**SimpleEveryThird** - Every third element is 0, no constraints elsewhere\
**SimpleSignFlip** - Ascending but every other inequality is an ‘=’ instead of ‘<’

**ComplexFlipPos1** - Flip odd and even ids positions in ascending (s01 < s00 < s03 < s02 < s05 < s04), without ending being variable left out because odd amount\
**ComplexFlipPos2** - Flip odd and even ids positions in ascending (s01 < s00 < s03 < s02 < s05 < s04 < s), with ending being variable left out because odd amount\
**ComplexHalfEqual** - Elements up to ceil(N/2) id equal each other (was meant to be floor but implementation wrong somehow)\
**ComplexMidPeak** - Ascending order to ceil(N/2) element, then descending order afterwards \
**ComplexPalindrome** - First smaller than last, second smaller than second last and so on\
**ComplexOddsEvens** - Ascending order of odd element ids then ascending order of even element ids (’<’ inbetween)

**WeirdTimes** - Elements are the times table of the first element (s01 = 2\*s00, s02 = 3\*s00, ...)\
~~**WeirdHundred** - Either s01=1 and all elements less than 100, or s01=2 and all elements greater than 100~~ too similar?\
!Doesnt fit context! **WeirdLoopMean** - Loop for as many times as average value of inputs rounded up\
~~**WeirdNotFactor**- Directly previous element cannot be a factor of the current element~~ doesnt work\
**WeirdFibonacci** - Elements follow fibonacci sequence rule\
**WeirdConstDiff** - There is constant difference between each element in list

!Doesnt fit context! **WiseDijsktra** - Usually WC when graph dense and weights similar so have to explore\
!Doesnt fit context! **WiseSalesman** - Usually WC when every node connected to every other\
!Doesnt fit context! **WiseBinaryTree** - Usually WC when elements are in sorted order

**BadgerUsername** - Checks if satisfies username conditions, (between 3 and 15 characters and they’re all character 45 for some reason is worst case)\
**BadgerPassword** - Checks if satisfies password conditions, (between 3 and 10 characters and they’re all character 37 for some reason is worst case)\
**BadgerHash** - Hashes N symbolic char arrays of length 2 and then retrieves one symbolic char array of length 2, WC should involve collisions
