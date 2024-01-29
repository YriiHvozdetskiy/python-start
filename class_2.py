class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        # за замовч вертається tuple
        # return f"{self.text} {other.text}", self.votes_qty + other.votes_qty
        return [f"{self.text} {other.text}", self.votes_qty + other.votes_qty]


first_comment = Comment('First comment')
first_comment.upvote()
second_comment = Comment('Second commnt')
second_comment.upvote()

print(first_comment + second_comment)  # ('First comment Second commnt', 2)
