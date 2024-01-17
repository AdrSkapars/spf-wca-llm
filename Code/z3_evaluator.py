import json
import subprocess


target_programs = [
	"own.SameHundred",
	"own.SameLowercase",
	"own.SameOnlyThird",
	"own.SameString",
	"own.SimpleAscendingLast",
	"own.SimpleEveryThird",
	"own.SimpleSignFlip",
	"own.SimpleSymmetric",
	"own.SimpleTrueFalse",
	"own.SimpleUnique",
	"own.WeirdConstDiff",
	"own.WeirdFibonacci",
	"own.WeirdTimes",
	"own.BadgerHash",
	"own.BadgerPassword",
	"own.BadgerUsername",
	"own.ComplexFlipPos_1",
	"own.ComplexFlipPos_2",
	"own.ComplexHalfEqual",
	"own.ComplexMidPeak",
	"own.ComplexPalindrome",
	"own.ComplexOddsEvens",
]

for tprogram in target_programs:
	