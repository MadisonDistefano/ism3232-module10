
# Exercise 1: Understanding Classes and Objects

1. **What are the two classes in the original chatbot project?**  
   OrderLookup and SupportChatbot.

2. **What are the objects created in main.py?**  
   order_tool and bot.

3. **What are the attributes of SupportChatbot?**  
   name, instructions, order_tool, stock_tool, and history.

4. **What are the methods of OrderLookup?**  
   __init__, find_order_id, and find_status.

5. **What line demonstrates composition?**  
   self.order_tool = order_tool. The chatbot receives and stores an OrderLookup object.

6. **In bot.respond("hello"), what does self refer to?**  
   self refers to the bot object.
