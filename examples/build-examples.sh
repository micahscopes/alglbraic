!#/usr/bin/env bash
algl --out . complex-numbers
algl --out . dual-numbers
algl --out . quaternions
algl --out . clifford-algebra GA2 '1 1'
algl --out . clifford-algebra GA3 '1 1 1'
algl --out . clifford-algebra PGA2 '1 1 0'
algl --out . clifford-algebra PGA3 '1 1 1 0'
algl --out . clifford-algebra CGA2 '1 1 1 -1'
algl --out . clifford-algebra CGA3 '1 1 1 1 -1'

