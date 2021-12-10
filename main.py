def corresponding_parenthesis(text):
    count_opening_parenthesis = text.count('(')
    count_closing_parenthesis = text.count(')')
    if count_closing_parenthesis == count_opening_parenthesis:
        return ''
    elif count_opening_parenthesis > count_closing_parenthesis:
        result = count_opening_parenthesis - count_closing_parenthesis
        return '('* result
    elif count_closing_parenthesis > count_opening_parenthesis:
        result = count_closing_parenthesis - count_opening_parenthesis
        return ')'* result

def remove_more_than_two_repetitions(text):
    new_text = ''
    for letter in text:
        if new_text[-2:] != letter + letter:
            new_text += letter
    return new_text