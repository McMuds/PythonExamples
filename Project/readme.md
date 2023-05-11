
# Shopping List Project

## Brief
Shopping lists are too manual. I want to be able to quickly add items I need during the week and then see a properly ordered list when I go shopping.  

Would be most useful mobile first, though some of the activities you might wish to do as a desktop browser app (i.e. this means my desktop css will be an after-thought.)

## MVP
- Be able to add items I need to buy
- Be able to add categories for items
- Be able to show all items on the list in a particular category
- Be able to look through previously bought items and mark that I need them
- Be able to look through previously added items by category
- Be able to create a shopping list and check things off as they’re bought
- Be able to sort the shopping list in various ways: category, alphabetical, ticked/not

## Possible Extensions
- Add a layout to the shop so that the shopping list is presented in the order you’d see it in the store
- Be able to change that layout if the shop is rejigged
- Add different shops and be able to add layouts to each shop, so you can see where things are based on that shop, and therefore a Tesco list would be different from an Asda list
- Be able to suggest common items based on previous shopping lists
--- frequency of appearance on a list
--- consistency - you've bought once every 4 weeks, and it's been a while since you last bought it. (yeah - this is stupidly hard)
- Be able to have shop specific goods (ie you like a brand of yoghurt that you can only get in Tesco. If you’re going to Tesco, prompt it as a suggestion)
- Be able to add a quantity to items - I need 600ml of cream because I’m making Keith, Mar and Sky a bribe cake

## How to run
- open a terminal session
- Clone the repo
- Requires:
--- flask (`pip3 flask` if you have pip3 installed. Which you most likely do.)
--- psychopg2 (`pip3 psychopg2`)
--- postgres
- dbcreate shopping_list
- if you want to set up some test data, `run psql -d shopping_list -f shopping_list.sql`
- navigate to the main directory, and type `flask run`
- in Chrome, use the url localhost:4999 (this is the default - check your terminal session - it will tell you which localhost port it's using)
