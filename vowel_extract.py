name = input('Enter a name: ')
vow = ['a', 'e', 'i', 'o', 'u']
extracted_vowels = [i for i in name if i in vow]
if extracted_vowels:
    print(extracted_vowels)
else:
    print('It seems no vowels in the name')