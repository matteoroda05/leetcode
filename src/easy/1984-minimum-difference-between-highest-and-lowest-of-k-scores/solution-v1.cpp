class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if (k <= 1){ return 0;}
        int size = nums.size();
        std::sort(nums.begin(), nums.end());
        unsigned int res_min = -1;
        for (auto i = 0; i < nums.size() - k + 1; i++){
            unsigned int tmp = nums[i+ k - 1] - nums[i];
            res_min = std::min (res_min, tmp);
            if (tmp < res_min){
                res_min = tmp;
            }
        }
        return (int) res_min;
    }
};