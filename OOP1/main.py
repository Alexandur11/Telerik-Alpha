from forum_post import ForumPost


post1 = ForumPost("Steven", "How to find use for every Microsoft product.", 2)
post2 = ForumPost("Todor", "Alfa Romeo for sale. Preowned by Italian grandma", 300)
post1.add_reply("I like Google!")
post1.add_reply("Ugh, Microsoft... :(")
post2.add_reply("Ugh, Romeo... :(")

print(post1.view())
print(post2.view())
