def get_num_words(contents):
    num_words = len(contents.split())
    return num_words

def count_character_instances(contents):
    contents = contents.lower().split()
    count = {}
    for word in contents:
        for char in word:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    
    return count