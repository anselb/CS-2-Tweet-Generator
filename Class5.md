## Class 5: Application Architecture

### Activities
- Review code with partners and use [code review rubric] to assess quality
- Compare code quality of functions based on length and responsibility
- Discuss issues with ripple effects caused by tight [coupling] and ways to avoid it
- Discuss advantages of classes and object-oriented programming (OOP)

### Objectives
After completing this class session and the associated tutorial challenges, students will be able to ...
- Assess aspects of code quality including organization and modularity
- Refactor functions that use structures as class instance methods
- Plan application architecture to prepare for future expansion

### Challenges
These challenges are the baseline required to complete the project and course.
Be sure to complete these before next class session and before starting on the stretch challenges below.
- [Page 6: Application Architecture]
    - Improve code organization and quality based on peer feedback on code review rubric
    - Write down your answers to questions about application architecture to plan improvements
        1. The key features include various histograms and their unique methods such as counting the types
        and frequency of each type. The application should also sample words based on frequency and arrange
        the words into sentences. Each feature is separated into their own files and split into functions.
        Only the histograms were made into classes.
        1. Yes, given that the project has to do with handling large bodies of text, I think that most, if
        not all of the names are okay.
        1. All variables are kept within their functions or classes. No global variables are present because
        they are not needed.
        1. All of the functions complete one action (or a few micro-actions that make up an action). All of the functions have no or minimal side effects as they do not modify variables out of their scope and
        it is rare that a function will print output instead of returning a value.
        1. The histograms are better in classes because each method shares types and tokens.
        1. Files do have their own modules that can be run as modules and as scripts.
        1. Most of the modules are able to be run independently. A couple of the histogram modules expect a
        dictogram to be inputted rather than any histogram.
    - Implement `Dictogram` class (histogram as a subclass of `dict` type) using [dictogram starter code]:
        - Implement `add_count(word, count)` - increase the frequency count of `word` in the histogram by `count`
        - Implement `frequency(word)` - return the frequency count of `word` in the histogram, or `0` if not found
        - Add `types` and `tokens` properties that track the number of word types and tokens in the histogram
        - Run `python dictogram.py` to test `Dictogram` class instance methods on a few small examples
        - Run `pytest dictogram_test.py` to run the [dictogram unit tests] and fix any failures
    - Implement `Listogram` class (histogram as a subclass of `list` type) using [listogram starter code]:
        - Implement `add_count(word, count)` - increase the frequency count of `word` in the histogram by `count`
        - Implement `frequency(word)` - return the frequency count of `word` in the histogram, or `0` if not found
        - Implement `__contains__(word)` - return a boolean indicating whether `word` is in the histogram
        - Implement `_index(word)` - return the index of the entry containing `word` if found in the histogram, or `None` if not found
        - Add `types` and `tokens` properties that track the number of word types and tokens in the histogram
        - Run `python listogram.py` to test `Listogram` class instance methods on a few small examples
        - Run `pytest listogram_test.py` to run the [listogram unit tests] and fix any failures
    - Restructure code files and functions to be more modular and flexible

### Stretch Challenges
These challenges are more difficult and help you push your skills and understanding to the next level.
- [Page 6: Application Architecture]
    - Organize other app functions and classes based on your answers to app architecture questions
- Bonus challenges
    - Improve the speed of accessing word frequencies in the `Listogram` class by storing entries in sorted order and searching for them in a clever way
        - An elegant way to do this is to make a `SortedListogram` class that inherits from the `Listogram` class and overrides some instance methods to specialize their behavior to handle entries in sorted order
    - Want to make the `Listogram` class more convenient to use? Add methods so that it can be used as an [iterable container], such as in a `for` loop like this:
        ```
        fish_text = 'one fish two fish red fish blue fish'
        histogram = Listogram(fish_text.split())
        for word in histogram:
            freq = histogram.frequency(word)
            print('{} occurs {} times'.format(word, freq))
        ```


[code review rubric]: http://make.sc/code-review-rubric
[Page 6: Application Architecture]: https://www.makeschool.com/academy/tutorial/tweet-generator-data-structures-probability-with-python/application-architecture
[coupling]: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
[iterable container]: https://docs.python.org/3/library/stdtypes.html#typeiter

[dictogram starter code]: source/dictogram.py
[dictogram unit tests]: source/dictogram_test.py
[listogram starter code]: source/listogram.py
[listogram unit tests]: source/listogram_test.py
