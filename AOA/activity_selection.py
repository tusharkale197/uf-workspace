
class ActivitySelection:

    def recursive_activity_select(self, start_time_list, finish_time_list, activity_index, total_activities):
        """
            Recursive implementation of the activity selection problem
        :param start_time_list:
        :param finish_time_list:
        :param activity_index:
        :param total_activities:
        :return:
        """
        try:

            act_ind = activity_index + 1
            # activity_index != -1 check making sure every solution includes the activity with least finish time
            while activity_index != -1 and activity_index < total_activities-1 and start_time_list[act_ind] <= finish_time_list[activity_index]:
                act_ind = act_ind + 1
            if activity_index < total_activities-1:
                return [act_ind] + [self.recursive_activity_select(start_time_list, finish_time_list, act_ind, total_activities)]
            else:
                return -1

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    start_list = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    fin_list = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    act = ActivitySelection()
    print(act.recursive_activity_select(start_time_list=start_list, finish_time_list=fin_list, activity_index=-1, total_activities=11))
