class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        di=collections.defaultdict(list)
        for path in paths:
            data=path.split()
            root=data[0]
            for file in data[1:]:
                name,_,content=file.partition('(')
                di[content[:-1]].append(root+'/'+name)    
        answer=[]
        for  value in di.values():
            if len(value)>1:
                answer.append(value)
        return answer


        