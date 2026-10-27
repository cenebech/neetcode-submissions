class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        intersect = nums1 & nums2

        for num in intersect:
            result.append(num)

        return result