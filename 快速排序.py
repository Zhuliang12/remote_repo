#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/11/14 10:39

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less_than_pivot = [x for x in arr[1:] if x <= pivot]
#         greater_than_pivot = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
#         # 递归调用quick_sort


class Solution(object):

    def quick_sort(self, arr):
        '''
        :param arr:
        :return:
        '''
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x <= pivot]
            more_than_pivot = [x for x in arr[1:] if x > pivot]

            return Solution().quick_sort(less_than_pivot) + [pivot] + Solution().quick_sort(more_than_pivot)

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m < 1:
            sub_list1 = []
        else:
            sub_list1 = nums1[0:m]

        sub_list1 += nums2[0:n]

        if len(sub_list1) <= 1:

            nums1[:] = sub_list1

            return nums1

        else:
            new_list = Solution.quick_sort(sub_list1)

            nums1[:] = new_list

            return nums1


# 示例
my_list = [3, 6, 4, 10, 1, 2, 1]
print(Solution().merge(nums1=[0], m=0, nums2=[1], n=1))
