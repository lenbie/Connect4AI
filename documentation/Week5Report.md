

- changed move ordering as instructed on moodle, makes alpha beta pruning more efficient as center cols better
- added constants on recommendation of peer reviewer
- made eval function player neutral



- move count needs to be for whole game - cant just do in minimax, so if we dont wanna use existing move count then we have to make a function but that iterates over board so not really more efficient than just checking if there are available moves