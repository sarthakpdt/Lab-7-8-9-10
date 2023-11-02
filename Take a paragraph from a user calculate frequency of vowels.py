paragraph=input("Enter a paragraph: ").lower()
vowel={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in paragraph:
    if i in 'aeiou':
        vowel[i]+=1
sort=dict(sorted(vowel.items()))
print("Vowel Frequency Counts:")
for vowel, count in sort.items():
    print(vowel,":",count)
