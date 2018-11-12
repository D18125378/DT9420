par = "Pair your seaside escape with the reds and whites of northern California's wine country in Jenner. This small coastal city in Sonoma County sits near the mouth of the Russian River, where, all summer long, harbor seals and barking California sea lions heave themselves onto the sand spit, sunning themselves for hours. You can swim and hike at Fort Ross State Historic Park and learn about early Russian hunters who were drawn to the area's herds of seal for their fur pelts. The fort's vineyard, with vines dating back to 1817, was one of the first places in California where grapes were planted."

# split paragraph into sentences
sentences = par.split(". ")

# split each sentence into words
tokenized_sentences = [sentence.split(" ") for sentence in sentences]

# get longest sentence and its length
longest_sen = max(tokenized_sentences, key=len)
longest_sen_len = len(longest_sen)

# get shortest word and its length
shortest_sen = min(tokenized_sentences, key=len)
shortest_sen_len = len(shortest_sen)

print (longest_sen_len)
print (shortest_sen_len)
