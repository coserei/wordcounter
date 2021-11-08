# Coserei 08/11/2021 (European date)
import time

TextInput = input('insert text:')
wordcount = len(TextInput.split(' '))
print('The total amount of words is: ' + wordcount)
time.sleep(2)
intent = 'https://twitter.com/intent/tweet?via=coserei&text=' + wordcount + '%20fucking%20words%21%20Tweeted%20via%20the%20wordcounter,'
print('Tweet your results here: ' + intent)
