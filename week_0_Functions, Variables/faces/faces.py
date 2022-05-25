def faces(text):
    # Emoji
    smiling_face = "🙂"
    frawing_face = "🙁"

    return text.replace(":)", smiling_face).replace(":(", frawing_face)

text = input()
print(faces(text))
