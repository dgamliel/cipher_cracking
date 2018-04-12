c_text = 'LRCXFTOGEVMPTESKXBGFCDNKJYCGJSRBXZGQGOWYXOOCZBGYJAAJNNPHVVBWVOXFVIWFVSDKVXGHBQKXKEGVGMQEGILVOFSUZBSRBTSHMVIRHBERGNIFCHPRLRCXFTOGEVMPTESKXBGFCDNKJYCGJSRBXZGQGOWYXOOCZBGYJAAJNNPHVVBWVOXFVIWFVSDKVXGHBQKXKEGVGMQEGILVOFSUZBSRBTSHMVIRHBERGNIFCHPRLRCXFTOGEVMPTESKXBGFCDNKJYCGJSRBXZGQGOWYXOOCZBGYJAAJNNPHVVBWVOXFVIWFVSDKVXGHBQKXKEGVGMQEGILVOFSUZBSRBTSHMVIRHBERGNIV'


'''
Finds all possible block sizes of our c_text
which is [1,2,4,89,178]
We can assume that the block size is not 1, 89, 178 due to the shortness of the message
'''

def find_sizes(c_text):
    arr_len = []
    for i in range(1,len(c_text)):
        if len(c_text) % i == 0:
            arr_len.append(i)
    return arr_len


def make_two_chunks(c_text):
    two_chunks = []
    for i in range(0,len(c_text), 2):
        chunk = c_text[i:i+2]
        two_chunks.append(chunk)

    return two_chunks

def make_four_chunks(c_text):

    two_chunks = []
    for i in range(0,len(c_text), 4):
        chunk = c_text[i:i+4]
        two_chunks.append(chunk)

    return two_chunks

print(find_sizes(c_text))
print(make_two_chunks(c_text))
print ("\n\n\nNOW ATTEMPTING CHUNKS OF 4\n\n")
print(make_four_chunks(c_text))
