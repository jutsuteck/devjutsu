import { FC, useState } from "react";
import { motion } from "framer-motion";

import Card from "@/components/ui/Card";

import { WorkItemType } from "@/models/projects";
import WorkItemDetailModal from "./WorkItemDetailModal";

interface Props {
  id: string;
  name: string;
  description: string | undefined;
  workItemType: WorkItemType;
  stateId: string;
  stateName: string;
  creationDate: Date;
}

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.5 } },
};

const WorkItemCard: FC<Props> = ({
  id,
  name,
  description,
  creationDate,
  workItemType,
  stateId,
  stateName,
}) => {
  const [showModal, setShowModal] = useState<boolean>(false);

  return (
    <>
      {showModal && (
        <WorkItemDetailModal
          id={id}
          name={name}
          description={description}
          effort={0}
          creationDate={creationDate}
          stateId={stateId}
          stateName={stateName}
          onClose={() => setShowModal(false)}
        />
      )}
      <motion.div initial="hidden" animate="visible" variants={fadeIn}>
        <Card
          className="mb-4 hover:cursor-pointer"
          boxShadow="shadow-md"
          onClick={() => setShowModal(true)}
        >
          <h1 className="text-md font-semibold">{name}</h1>
          <p>{description}</p>
          <span>{workItemType}</span>
        </Card>
      </motion.div>
    </>
  );
};

export default WorkItemCard;
