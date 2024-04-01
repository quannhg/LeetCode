class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        
        min_heap, visited_pairs, smallest_pairs = [], set(), []
        
        heappush(min_heap, (nums1[0] + nums2[0], 0, 0)) # (sum, idx_1, idx_2)
        visited_pairs.add((0,0)) # (idx_1, idx_2)
        
        while len(smallest_pairs) < k and min_heap:
            _min_sum, nums1_idx, nums2_idx = heappop(min_heap)
            smallest_pairs.append((nums1[nums1_idx], nums2[nums2_idx]))
            
            if nums1_idx + 1 < len(nums1) and (nums1_idx + 1, nums2_idx) not in visited_pairs:
                heappush(min_heap, (nums1[nums1_idx + 1] + nums2[nums2_idx], nums1_idx + 1, nums2_idx))
                visited_pairs.add((nums1_idx + 1, nums2_idx))
                
            if nums2_idx + 1 < len(nums2) and (nums1_idx, nums2_idx + 1) not in visited_pairs:
                heappush(min_heap, (nums1[nums1_idx] + nums2[nums2_idx + 1], nums1_idx, nums2_idx + 1))
                visited_pairs.add((nums1_idx, nums2_idx + 1))
                
        return smallest_pairs

            
        
