def _sort(List):
    for i, num in enumerate(List):
        try:
            if List[i+1] < num:
                print "Compare Elements"
                print List[i],List[i+1]
                List[i] = List[i+1]
                List[i+1] = num
                _sort(List)
        except IndexError:
            pass
    return List
 
List = [34,88,9,0,2,4,77]
_sort(List)
print List
