import Card from "@/components/ui/Card";
import { WorkItemType } from "@/models/projects";
import { FC } from "react";
import { motion } from "framer-motion";

interface Props {
  name: string;
  description: string | undefined;
  workItemType: WorkItemType;
}

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.5 } },
};

const WorkItemCard: FC<Props> = ({ name, description, workItemType }) => {
  return (
    <motion.div initial="hidden" animate="visible" variants={fadeIn}>
      <Card>
        <h1 className="text-md font-semibold">{name}</h1>
        <p>{description}</p>
      </Card>
    </motion.div>
  );
};

export default WorkItemCard;
