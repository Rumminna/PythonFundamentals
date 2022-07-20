class SlidoComment:
    def __init__(self, author_name, content, date="now", likes=0, dislikes=0, author_picture="https://www.photocase.de/verwendung-von-fotos"):
        self.author_name = author_name
        self.content = content
        self.date = date
        self.likes = likes
        self.dislikes = dislikes
        self.author_picture = author_picture

    def present_comment(self):
        return f"{self.author_name}\n Likes: {self.likes} Dislikes: {self.dislikes} {self.author_picture}"

comment = SlidoComment("No name", content="Ne sum siguren")
for _ in range(100):
    comment.likes += 1
print(comment.present_comment())
