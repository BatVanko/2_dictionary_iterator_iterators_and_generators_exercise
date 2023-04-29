# 2_dictionary_iterator_iterators_and_generators_exercise
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

Test Code
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

Output

(1, '1')
(2, '2')

Test Code
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

Output
("name", "Peter")
("age", 24)
