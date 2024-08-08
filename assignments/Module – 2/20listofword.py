"""Write a Python function that takes a list of words and returns the length
of the longest one."""

word=["keval","meet","deep","rushi","sandeep"]
count=0

for i in word:
    lenth=len(i)
    print(lenth)
    if lenth>count:
        count=lenth

print(f"longest one:",{count})


