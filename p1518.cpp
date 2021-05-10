class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans = 0;

        int empty = 0;

        while(numBottles > 0) {
            ans += numBottles;
            int tmp = numBottles + empty;
            numBottles = tmp/numExchange;
            empty = tmp%numExchange;
        }

        return ans;
    }
};
