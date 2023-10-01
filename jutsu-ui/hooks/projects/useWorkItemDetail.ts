import { WorkItem } from "@/models/projects";
import workItemService from "@/services/projects/WorkItemService";
import { useQuery } from "react-query";

const useWorkItemDetail = (workItemId: string) => {
  return useQuery<WorkItem, Error>(
    ["workItem", workItemId],
    () => workItemService.getWorkItem(workItemId),
    { staleTime: 0 }
  );
};

export default useWorkItemDetail;
