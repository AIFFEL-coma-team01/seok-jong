def mostCommonWord(paragraph:str,banned:list[str])->str:
    word = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts= collections.Counter(word)
    return counts.most_common(1)[0][0]



str="Bob hit a ball, the hit BALL flew far after it was hit."
mostCommonWord(str)