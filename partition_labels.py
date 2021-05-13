"""
A string s of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


Note:

s will have length in range [1, 500].
s will consist of lowercase English letters ('a' to 'z') only.
"""

# Step 1: create a dict with each char, last instance of that char
# Step 2: create a temporary partition for first char
# Step 3: repeat step 2 until we have traversed the string to the temporary partition, record position
# Step 4: repeat steps 2-3 until string is fully traversed

alphabet = "abcdefghijklmnopqrstuvwxyz"
input = "ababcbacadefegdehijhklij"

def partition_labels(input, alphabet):
    output = []
    last_instance = {}
    # for letter in alphabet: # O(n)
    #     last_instance[letter] = None

    for i in range(len(input) - 1): # O(n)
        # if last_instance[input[i]] == None:
        #     last_instance[input[i]] - i
        # else:
        #     last_instance[input]
        last_instance[input[i]] = i
    print(last_instance)

    current_partition = 0
    previous_partition = 0
    current_index = 0

    while current_index < len(input) - 1:
        if last_instance[input[current_index]] > current_partition:
            print(f"Previous partion: {current_partition}")
            current_partition = last_instance[input[current_index]]
            print(f"Current partition: {current_partition}")
        if current_index >= current_partition:
            partition_length = current_partition - previous_partition + 1
            output.append(partition_length)
            previous_partition = current_partition + 1
        current_index += 1

    return output


print(partition_labels(input, alphabet))
