class ForumPost:

    def __init__(self, author: str, text: str, upvotes: int, ):
        self.author = author
        self.text = text
        self.upvotes = upvotes
        self.replies = []

    def add_reply(self, text):
        reply_text = "-" + " " + text
        self.replies.append(reply_text)

    def view(self):
        view_str = f'{self.text} / by {self.author}, {self.upvotes} votes.'

        if len(self.replies) > 0:
            for reply in self.replies:
                view_str += f'\n  {reply}'

        return view_str