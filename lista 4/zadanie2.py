import requests
from bs4 import BeautifulSoup
from collections import Counter

def find_most_common_words_in_tag(html_content, target_tag):
    soup = BeautifulSoup(html_content, "html.parser")

    valid_tags = ["h1", "h2", "p", "ol"]
    if target_tag not in valid_tags:
        return "Nieprawidłowy znacznik"

    tag_elements = soup.find_all(target_tag)

    if not tag_elements:
        return f"Brak znalezionych elementów dla tagu {target_tag}"

    text_inside_tag = " ".join([element.get_text() for element in tag_elements])

    words = text_inside_tag.split()
    
   
    words = [word for word in words if len(word) > 4]

    if not words:
        return f"Brak słów wewnątrz tagu {target_tag}"

    word_counts = Counter(words)

    most_common_words = word_counts.most_common(1)
    least_common_words = word_counts.most_common()[:-4:-1]

    most_common_output = "\n".join([f"'{word}' (występuje {count} razy)" for word, count in most_common_words])
    least_common_output = "\n".join([f"'{word}' (występuje {count} razy)" for word, count in least_common_words])

    return f"Najczęściej występujące słowo wewnątrz tagu {target_tag}:\n{most_common_output}\n\nTrzy rzadziej występujące słowa wewnątrz tagu {target_tag}:\n{least_common_output}"


def main():
    website_url = input("Podaj adres strony internetowej: ")
    selected_tag = input("Wybierz znacznik (h1, h2, p, ol): ")

    valid_tags = ["h1", "h2", "p", "ol"]
    if selected_tag not in valid_tags:
        print("Nieprawidłowy znacznik. Zakończono program.")
        return

    try:
        response = requests.get(website_url)
        response.raise_for_status()
        result = find_most_common_words_in_tag(response.text, selected_tag)
        print(result)
    except requests.exceptions.RequestException as error:
        print(f"Błąd podczas pobierania strony: {error}")


if __name__ == "__main__":
    main()
