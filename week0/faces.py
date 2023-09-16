def main():
    msg = input()
    text = convert(msg)
    print(text)

# implement a function called convert
def convert(emoji):
    emoji = emoji.replace(":)","🙂")
    emoji = emoji.replace(":(","🙁")
    return emoji
# call the main function
main()