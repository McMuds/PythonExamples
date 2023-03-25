from repositories import shopping_list_repository as list_repo
import pdb

# def index():
# pdb.set_trace()
lists = list_repo.select_all()
for row in lists:
    print(f"{row.id} was created on {row.date_created}")
    for item in row.selection:
        print(f"{item.item.name} has or has not been selected {item.selected}")