import useWorkflowStates from "@/hooks/projects/useWorkflowStates";
import { State } from "@/models/projects";
import { FC } from "react";
import StateContainer from "./StateContainer";

interface Props {
  workflowId: string;
}

const StateList: FC<Props> = ({ workflowId }) => {
  const {
    data: states,
    isLoading: statesIsLoading,
    isError: statesIsError,
  } = useWorkflowStates(workflowId);

  if (statesIsLoading) return <p>Loading...</p>;
  if (statesIsError) return <p>Error loading states</p>;
  if (!states || states.length === 0) return <p>No states available</p>;

  return (
    <div className="flex mt-10 space-x-8">
      {states.map((state: State) => (
        <StateContainer
          key={state.id}
          stateName={state.name}
          stateId={state.id}
          workflowId={workflowId}
        />
      ))}
    </div>
  );
};

export default StateList;
