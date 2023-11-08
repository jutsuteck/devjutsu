import { FC } from "react";

import BaseModal from "@/components/ui/BaseModal";
import WorkItemNameModalForm from "./WorkItemNameModalForm";
import WorkItemDescriptionModalForm from "./WorkItemDescriptionModalForm";

interface Props {
  id: string;
  name: string;
  description?: string;
  effort?: number;
  creationDate: Date;
  stateId: string;
  stateName: string;
  onClose: () => void;
}

const WorkItemDetailModal: FC<Props> = ({
  id,
  name,
  description,
  effort,
  creationDate,
  stateId,
  stateName,
  onClose,
}) => {
  return (
    <BaseModal
      onClose={onClose}
      fixedSize="w-1/2"
      className="border border-nord-polar-night-light"
    >
      <div className="flex">
        <div className="flex-grow flex-shrink">
          <WorkItemNameModalForm
            name={name}
            workItemId={id}
            stateId={stateId}
          />
          <WorkItemDescriptionModalForm
            description={description}
            workItemId={id}
            stateId={stateId}
          />
        </div>
        <div className="w-1/3 flex-shrink-0 flex flex-col ml-4">
          <span className="py-2 px-4 bg-nord-polar-night-light rounded">
            {stateName}
          </span>
          <div className="my-6 rounded border border-nord-polar-night-light">
            <div className="p-4 border-b border-nord-polar-night-light">
              <h1 className="text-md font-bold">Details</h1>
            </div>
            <div className="m-4 space-y-2">
              <div className="flex justify-between">
                <span className="font-bold">Assignee</span>
                <span>Assignee name</span>
              </div>
              <div className="flex justify-between">
                <span className="font-bold">Effort</span>
                <span>{effort}</span>
              </div>
              <div className="flex justify-between">
                <span className="font-bold">Ready for Development</span>
                <span></span>
              </div>
            </div>
          </div>

          <div className="mb-4 text-nord-polar-night-lightest">
            Created on {creationDate.toString()}
          </div>
        </div>
      </div>
    </BaseModal>
  );
};

export default WorkItemDetailModal;
