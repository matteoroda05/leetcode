double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int tot = nums1Size + nums2Size;
    int left = (tot - 1)/2;
    int right = tot/2;
    int i = 0, j = 0, idx = 0, value;
    double lres, rres;
    while (idx < tot){
        if (i < nums1Size && (j >= nums2Size || nums1[i] <= nums2[j])){
            value = nums1[i];
            if (i < nums1Size){ i++;}
        } else {
            value = nums2[j];
            if (j < nums2Size ){j++;}
        }
        if (idx == left){
            lres = (double) value;
        } 
        if (idx == right){
            rres = (double) value;
            break;
        }
        idx++;
    }
    return (lres + rres)/2;
}