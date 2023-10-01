import { FC } from "react";

import BaseModal from "@/components/ui/BaseModal";
import WorkItemNameModalForm from "./WorkItemNameModalForm";
import WorkItemDescriptionModalForm from "./WorkItemDescriptionModalForm";

interface Props {
  id: string;
  name: string;
  description?: string;
  effort?: number;
  stateId: string;
  stateName: string;
  onClose: () => void;
}

const WorkItemDetailModal: FC<Props> = ({
  id,
  name,
  description,
  effort,
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
        <div className="w-1/3 flex-shrink-0 flex ml-4">
          <span className="py-2 px-4 bg-nord-frost-medium rounded">
            {stateName}
          </span>
        </div>
      </div>
    </BaseModal>
  );
};

export default WorkItemDetailModal;
