数组区间合并问题
class Solution
{
  public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval)
    {
        vector<Interval>::iterator it = intervals.begin();
        while (it != intervals.end())
        {
            if (newInterval.end < it->start)
            {
                intervals.insert(it, newInterval);
                return intervals;
            }
            else if (newInterval.start > it->end)
            {
                it++;
            }
            else
            {
                newInterval.start = min(newInterval.start, it->start);
                newInterval.end = max(newInterval.end, it->end);
                it = intervals.erase(it);
            }
        }
        intervals.insert(intervals.end(), newInterval);
        return intervals;