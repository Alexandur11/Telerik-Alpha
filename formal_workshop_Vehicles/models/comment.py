class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'


    def __init__(self, content, author):
        self.content = content
        self.author = author

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str) and Comment.CONTENT_LEN_MIN < len(value) < Comment.CONTENT_LEN_MAX:
            self._content = value
        else:
            raise ValueError(Comment.CONTENT_LEN_ERR)


    def __str__(self):
        content = 'hello, mom!'
        author = 'steven'
        expected = '\n'.join([
            '----------',
            'hello, mom!',
            'User: steven',
            '----------',
        ])
        return expected

