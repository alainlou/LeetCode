#include <iostream>
#include <vector>

std::vector<int> merge_it(std::vector<int> arr1, std::vector<int> arr2){
    std::vector<int> result;
    int iter1 = 0;
    int iter2 = 0;

    while(iter1 < arr1.size() && iter2 < arr2.size()){
        if(arr1[iter1] < arr2[iter2]){
            result.push_back(arr1[iter1]);
            ++iter1;
        }
        else{
            result.push_back(arr2[iter2]);
            ++iter2;
        }
    }
    while(iter1 < arr1.size()){
        result.push_back(arr1[iter1]);
        ++iter1;
    }
    while(iter2 < arr2.size()){
        result.push_back(arr2[iter2]);
        ++iter2;
    }

    return result;
}

void merge_sort(std::vector<int> &vec){
    if(vec.size() == 1){
       return;
    }
    else{
        int mid = vec.size()/2;
        std::vector<int> lhs;
        std::vector<int> rhs;
        for(int i = 0; i <= mid; ++i){
            lhs.push_back(vec[i]);
        }
        for(int j = mid+1; j < vec.size(); ++j){
            rhs.push_back(vec[j]);
        }
        merge_sort(lhs);
        merge_sort(rhs);
        vec = merge_it(lhs, rhs);
        return;
    }
}

int main(){
  return 0;
}
