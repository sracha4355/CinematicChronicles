import sys
sys.path.append('..')

from query import *

queryBuilder = QueryBuilder(4)
prompts = [
    "100. idea1",
    "1. idea2",
    "1000. idea3",
    "45. idea6"
]
print('extracted choices', queryBuilder.extractChoices('\n'.join(prompts)))
