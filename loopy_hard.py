import re


def market_revenue(transactions):
    total = 0
    if not transactions:
        return 0
    else:
        for trans in transactions:
            if isinstance(trans,tuple):
                total += int(trans[1])*int(trans[2])
        
    

    # TODO: calculate total revenue

    return total
print(market_revenue([("apple",4,5),("banana",10,2)]))


# def longest_unique_word(sentence):
#     word = {}
    # if not sentence:
    #     return ''
    # elif isinstance(sentence,list):
    #     for s in sentence:
    #         se = s.split()
    #         print(se)
    #         for words in se:
    #             word.setdefault(words, se.count(words))
    #     print(word)
    #     for key, val in word.items():
    #         if val == 1:
    #             word[key] = len(key)
    #     for key,val in word.items():
    #         if val == max(word.values()):
    #             return key
    # else:
    #     sentence = sentence.split()
    #     print(sentence)
    #     for s in sentence:
    #         word.setdefault(s, sentence.count(s))
    #     print(word)
    #     for key, val in word.items():
    #         if val == 1:
    #             word[key] = len(key)
    #     for key,val in word.items():
    #         if val == max(word.values()):
    #             return key
    
    # for words in sentence:
    #     wording = words.split(' ')
    #     for w in wording:
    #         word[w] = word.get(w,0)+1
    #     word_frq_sorted = sorted(word, key=word.get)
    # return word_frq_sorted[-1]
def longest_unique_word(sentences):
    word_counts = {}
    all_words = []
    
    # 1. Collect all words from every sentence
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            all_words.append(word)
            word_counts[word] = word_counts.get(word, 0) + 1
            
    # 2. Find the longest word that has a count of exactly 1
    longest_unique = ""
    for word in all_words:
        if word_counts[word] == 1:
            if len(word) > len(longest_unique):
                longest_unique = word
                
    return longest_unique

print(longest_unique_word([
            "one two three four five",
            "data data science fun",
            "red blue green blue red yellow"
        ]))
            
# print(longest_unique_word([
#             "one two three four five",
#             "data data science wellnes fun",
#             "red blue green blue red yellow"
#         ]))

def two_sum(nums, target):

    # for i in range(0,len(nums)):
    #     if nums[i]+nums[i+1] == target:
    #         return i,i+1
    #     else:
    #         return
    seen = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return (seen[diff] , i)
        seen[n] = i
print(two_sum([2,7,11,15],9))


def peak_temperatures(temps):

    peaks = []
    if len(temps)<2:
        return peaks
    else:
        for i,temp in enumerate(temps):
            if i > 0 and i <len(temps):
                if temp > temps[i-1] and temp > temps[i+1]:
                    peaks.append(temp)
    # TODO

    return peaks
print(peak_temperatures([30,32,31,35,33,36,34,33]))


def email_filter(emails):

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    valid = []
    invalid = []
    if isinstance(emails,list):
        for email in emails:
            if re.findall(pattern,email):
                valid.append(email)
            else:
                invalid.append(email)
    else:
        if re.findall(pattern,emails):
            valid.append(emails)
        else:
            invalid.append(emails)
        
    return {
        "valid": valid,
        "invalid": invalid
    }
print(email_filter(["user@mail.com",
            "bad@domain",
            "hello@gmail.com"]))

def stock_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # 1. Update the lowest price seen so far
        if price < min_price:
            min_price = price
        
        # 2. Check if selling at current price gives a better profit
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
            
    return max_profit
print(stock_profit([7,1,5,3,6,4]))


def inventory_projection(stock, daily_sales):
    current_stock = stock
    
    for day, inventory in enumerate(daily_sales):
        current_stock -= inventory
        if current_stock<= 0:
            return f"The stock will run out on day {day+1}"
        
    return f"Inventory lasts entire period. Remaining stock: {inventory}"