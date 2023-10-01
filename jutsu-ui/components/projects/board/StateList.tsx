import { State } from "@/models/projects";
import { FC } from "react";
import { DndContext } from "@dnd-kit/core";

import StateContainer from "./StateContainer";

import useWorkflowStates from "@/hooks/projects/useWorkflowStates";
import workItemService from "@/services/projects/WorkItemService";

interface Props {
  workflowId: string;
}

const StateList: FC<Props> = ({ workflowId }) => {
  const {
    data: states,
    isLoading: statesIsLoading,
    isError: statesIsError,
  } = useWorkflowStates(workflowId);

  const handleDragEnd = async (event) => {};

  if (statesIsLoading) return <p>Loading...</p>;
  if (statesIsError) return <p>Error loading states</p>;
  if (!states || states.length === 0) return <p>No states available</p>;

  return (
    <DndContext onDragEnd={handleDragEnd}>
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
    </DndContext>
  );
};

export default StateList;
