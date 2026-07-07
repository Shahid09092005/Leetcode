class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 ,n2, cnt=Counter(nums1),Counter(nums2),0
        # for nums1
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                prodUnderRoot = (nums1[i]*nums1[j])**(1/2)
                if prodUnderRoot==int(prodUnderRoot) and prodUnderRoot in nums2:
                    cnt+=n2[prodUnderRoot]
        # for nums2 
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                prodUnderRoot = (nums2[i]*nums2[j])**(1/2)
                if prodUnderRoot==int(prodUnderRoot) and prodUnderRoot in nums1:
                    cnt+=n1[prodUnderRoot]
        return cnt