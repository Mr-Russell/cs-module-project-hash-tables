def word_count(s):
    # Your code here
    count = {}
    punct = '":;,.-+=/\|[]{}()*^&'
    words = s.lower().split()
    

    for i in words:
        i = i.strip(punct)
        if i == '':
            continue

        if i not in count:
            count[i] = 0
        
        count[i] += 1
    
    return count




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))