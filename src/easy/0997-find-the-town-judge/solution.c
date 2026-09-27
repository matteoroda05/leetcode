int findJudge(int n, int** trust, int trustSize, int* trustColSize) {
    if (n == 1) return 1;
    if (n - 1 > trustSize) return -1;
    int trusted[n], trusting[n];
    for (int i = 0; i < n; i++){
        trusted[i] = 0;
        trusting[i] = 0;
    }
    for (int i = 0; i < trustSize; i++){
        trusted[trust[i][1]-1] += 1;
        trusting[trust[i][0]-1] += 1;
    }
    for (int i = 0; i < n; i++){
        if (trusted[i] == n-1 && trusting[i] == 0) return i+1;
    }
    return -1;

}