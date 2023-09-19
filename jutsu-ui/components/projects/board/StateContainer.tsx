import { FC, useState } from "react";
import WorkItemCard from "./WorkItemCard";
import useStateWorkItems from "@/hooks/projects/useStateWorkItems";
import WorkItemNameForm from "./WorkItemNameForm";

interface Props {
  stateId: string;
  stateName: string;
  workflowId: string;
}

const StateContainer: FC<Props> = ({ stateId, stateName, workflowId }) => {
  const { data: workItems, isLoading, isError } = useStateWorkItems(stateId);

  console.log("StateContainer: ", stateId);

  return (
    <div className="w-72">
      <h1 className="text-lg font-semibold mb-4">{stateName}</h1>

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
