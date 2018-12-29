# Magic8Ball


### Python powered, smart magic 8 ball for answering yes or no questions.


This program is cooler than your typical random magic 8ball. First the user is asked to enter a simple yes or no question. Than  it determines the answer by first calculating the md5sum of the question and then converting the hash into binary. Next, each numeral in the binary is added together to form the final sum. If the sum %2 == 0 , then return an affirmative answer, otherwise return a negative. There is both a yes and no list dictionary of verbose answers. After calculating whether or not to answer in the affirmative, return a random yes or no answer string from the corresponding dictionary.
