import { Workflow } from "@/models/projects";
import workflowService from "@/services/projects/WorkflowService";
import { useQuery } from "react-query";

const useCurrentWorkflow = (projectId: string) => {
  return useQuery<Workflow, Error>(["currentWorkflow", projectId], () =>
    workflowService.getCurrentWorfklow(projectId)
  );
};

export default useCurrentWorkflow;
