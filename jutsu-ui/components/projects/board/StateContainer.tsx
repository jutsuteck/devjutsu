import { FC } from "react";
import WorkItemCard from "./WorkItemCard";
import useStateWorkItems from "@/hooks/projects/useStateWorkItems";
import WorkItemNameForm from "./WorkItemNameForm";

import { BiTrash } from "react-icons/bi";
import { useMutation, useQueryClient } from "react-query";
import stateService from "@/services/projects/StateService";

interface Props {
  stateId: string;
  stateName: string;
  workflowId: string;
}

const StateContainer: FC<Props> = ({ stateId, stateName, workflowId }) => {
  const { data: workItems, isLoading, isError } = useStateWorkItems(stateId);

  const queryClient = useQueryClient();

  const mutation = useMutation((state_id: string) =>
    stateService.deleteState(state_id)
  );

  const onClick = () => {
    console.log("clicked");
    const data = {
      state_id: stateId,
    };
    mutation.mutate(data.state_id, {
      onSuccess: () => {
        queryClient.invalidateQueries(["states", workflowId]);
      },
      onError: (error: any) => {
        console.log(error);
      },
    });
  };

  return (
    <div className="w-72 border-dotted border-2 border-nord-polar-night-medium hover:cursor-pointer rounded-md p-4">
      <h1 className="text-lg font-semibold mb-4 flex items-center justify-between">
        {stateName}
        <button onClick={onClick}>
          <BiTrash />
        </button>
      </h1>

      <WorkItemNameForm workflowId={workflowId} stateId={stateId} />

      {workItems?.map((item) => (
        <>
          <WorkItemCard
            key={item.id}
            name={item.name}
            description={item?.description}
            workItemType={item.work_item_type}
          />
        </>
      ))}
    </div>
  );
};

export default StateContainer;
