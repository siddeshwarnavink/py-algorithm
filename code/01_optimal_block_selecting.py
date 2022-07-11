"""
Problem:
Imagine this as a street in a city and you need to choose a 'block' to by an appartement in this street. Each 'block' has 
various 'facilities' like e.g, gym, school, store. We need to write an algorithm to choose the optimal block 
where all our required facilities are all easily accessible

(Source: https://www.youtube.com/watch?v=rw4s4M3hFfs)
"""

input_blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    },
]

input_req = ["gym", "school", "store"]

def getOptimalBlock(blocks, req):
    blockScores = []
    
    for currentBlockIndex, block in enumerate(blocks):
        facilityScore = 0
        
        for facility in req:
            if(block[facility]):
                facilityScore += 1
            else:
                step = 1
                while True:
                    if currentBlockIndex + step < len(blocks) and (blocks[currentBlockIndex + step][facility]):
                        facilityScore += step
                        break
                    if currentBlockIndex - step > 0 and (blocks[currentBlockIndex - step][facility]):
                        facilityScore += step
                        break
                    step += 1
                step += 1
                
        blockScores.append(facilityScore)
        
    return blockScores.index(min(blockScores))

optimal_block = getOptimalBlock(input_blocks, input_req)

print('The optimal block to live in is block #{}'.format(optimal_block))