import { WorkItem } from "@/models/projects";
import workItemService from "@/services/projects/WorkItemService";
import { useQuery } from "react-query";

const useStateWorkItems = (state_id: string) => {
  console.log("use stateId: ", state_id);
  return useQuery<WorkItem[], Error>(["stateWorkItems", state_id], () =>
    workItemService.getWorkItemsByStateId(state_id)
  );
};

export default useStateWorkItems;
