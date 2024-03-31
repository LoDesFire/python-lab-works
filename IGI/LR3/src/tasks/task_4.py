from utils import task_decorator

@task_decorator
def task_4():
    """
    This function prints a Shakespearean passage and performs various operations on it
    """
    string = "So she was considering inz her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(string)
    lst = string.split()
    upper_count = 0
    lower_count = 0
    
    for c in string:
        # Counts the number of uppercase and lowercase characters in the input string
        upper_count += c.isupper()
        lower_count += c.islower()
          
    print(f"There are {upper_count} uppercase characters and {lower_count} lowercase characters in the input string.")
    
    for index, w in enumerate(lst): 
        # Searches for the first word in the input string that contains a 'z'
        if w.count('z') > 0:
            print(index + 1)
            break
        
    print(str().join([w + " " for w in lst if w[0] != 'a'])) # print a Shakespearean passage without words beggining on 'a'