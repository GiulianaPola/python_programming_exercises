class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        num_papers=-1
        num_citations=-1
        h=0
        while num_papers>=num_citations:
            num_papers=0
            num_citations=num_citations+1
            for i in range(n):
                if citations[i]>=num_citations:
                    num_papers=num_papers+1
            #print(num_papers,num_citations,h)
        h=num_citations-1
        return h