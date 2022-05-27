class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0

        for (i in 1..n) {
            if (lost.contains(i)) {
                // 체육복을 도난당한 학생
                if (reserve.contains(i)) {
                    // 여분을 가져왔을 때
                    answer += 1
                } else {
                    // 여분을 가져오지 않았을 때
                    if (!lost.contains(i - 1) && reserve.contains(i - 1)) {
                        answer += 1
                    } else if (!lost.contains(i + 1) && reserve.contains(i + 1)) {
                        answer += 1
                        val temp_index = reserve.indexOf(i + 1)
                        reserve[temp_index] = -1
                    }
                }
            } else {
                // 체육복을 도난당하지 않은 학생
                answer += 1
            }
        }

        return answer
    }
}