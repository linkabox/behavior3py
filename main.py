
import b3
import json
from b3.actions.log import Log


with open("tree.json",'r') as load_f:
    data = json.load(load_f)
    print(data)

tree = b3.BehaviorTree()
tree.load(data,{
    "Log":Log
})

print("load tree:",tree.id)

board = b3.Blackboard()

for i in range(0,5):
    print("tree tick==========:",i)
    tree.tick(i, board)