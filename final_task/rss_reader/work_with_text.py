import html
import decorators


def get_img(input_string: str) -> [str, str]:
    """from string type '<img src="link" alt="something">text' returns ['link', 'something']"""
    input_string = input_string[input_string.find('<img'):]
    link = input_string[input_string.find('src="') + 5:]
    str_img = input_string[input_string.find('alt="') + 5:]
    return [link[:link.find('"')], str_img[:str_img.find('"')]]


def text_processing(string: str, array_links=None):
    """processes a string for output"""
    if array_links is None:
        array_links = []
    image = ''
    if '<' not in string:
        array_links.append('')
        return html.unescape(string)
    string += '<'
    if 'img' in string:
        image_link_and_alt_text = get_img(string)
        array_links.append(image_link_and_alt_text[0])
        image = '[image: ' + image_link_and_alt_text[1] + '] '
    string = string[string.find('<') + 1:]
    while string.find('<') - string.find('>') == 1:
        string = string[string.find('<') + 2:]
    string = string[string.find('>') + 1:string.find('<')]
    return html.unescape(image + string)


@decorators.functions_log
def get_string_with_result(data: dict, limit=-1) -> str:
    """Converts json to string for print"""
    result = '\n'
    result += data['title'] + '\n\n'
    for index_news, dict_news in enumerate(data['items']):
        result += 'Title: ' + dict_news['title'] + '\n'
        result += 'Date: ' + dict_news['published'] + '\n'
        result += 'Link: ' + dict_news['link'] + '\n'
        result += 'Description: ' + dict_news['summary'] + '\n'
        if dict_news['contain_image']:
            result += 'Link on image: ' + dict_news['link_on_image'] + '\n'
        result += '\n'
    return result


def edit_key(input_key: str) -> str:
    """Converts a string to a beautiful for print view ('string' -> 'String: ')"""
    if input_key == 'published':
        input_key = 'Date'
    elif input_key == 'summary':
        input_key = 'Description'
    return input_key[0].upper() + input_key[1:] + ': '
