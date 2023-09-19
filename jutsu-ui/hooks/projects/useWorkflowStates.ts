import { State } from "@/models/projects";
import stateService from "@/services/projects/StateService";
import { useQuery } from "react-query";

const useWorkflowStates = (workflow_id: string) => {
  return useQuery<State[], Error>(["states", workflow_id], () =>
    stateService.getStatesByWorkflowId(workflow_id)
  );
};

export default useWorkflowStates;
