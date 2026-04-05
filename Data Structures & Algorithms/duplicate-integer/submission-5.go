func hasDuplicate(nums []int) bool {
   values := make(map[int]struct{})
   for _, n := range nums {
        if _, ok := values[n]; ok {
            return true
        }
        values[n] = struct{}{}
   } 
   return false
}

// values = set()
// for n in nums:
//     if n in values:
//         return True
//     values.add(n)
// return False