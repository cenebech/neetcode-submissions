class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        [Hello, World, cat]
        5#hello5#world#cat

        # look through chatGPT solutions
        """
        encode_str = ""
        for word in strs:
            length_word = str(len(word))
            encode_str += length_word
            encode_str += "#"
            encode_str += word
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str = []

        current_index = 0

        #while we have values keep moving
        while current_index < len(s):
            #create our seperator index
            seperator_index = current_index

            #while we have do not have # keep moving
            while s[seperator_index] != "#":
                #increment the position of seperator_index
                seperator_index += 1

            #word_length
            word_length = int(s[current_index:seperator_index])

            #word_start
            word_start = seperator_index + 1

            #word_end
            word_end = word_start +word_length

            #word
            word = s[word_start:word_end]


            #update the decode
            decode_str.append(word)


            #update current index
            current_index = word_end


        return decode_str


   