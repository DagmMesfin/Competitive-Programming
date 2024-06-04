class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        commonstringind = defaultdict(list)
        minindexsum = float('inf')
        for stro in list1:
            indexsum = 0
            if stro in list2:
                indexsum = list1.index(stro) + list2.index(stro)
                minindexsum = min(minindexsum, indexsum)
                commonstringind[indexsum].append(stro)
        return commonstringind[minindexsum]