func hasDuplicate(nums []int) bool {
   values := make(map[int]bool)
   for _, n := range nums {
        if _, ok := values[n]; ok {
            return true
        }
        values[n] = true
   } 
   return false
}

// values = set()
// for n in nums:
//     if n in values:
//         return True
//     values.add(n)
// return False