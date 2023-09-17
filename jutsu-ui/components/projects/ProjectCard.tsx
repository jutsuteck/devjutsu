import { FC } from "react";
import { Methodology } from "@/models/projects";
import { motion } from "framer-motion";

import Card from "../ui/Card";
import Link from "next/link";

interface Props {
  nameKey: string;
  methodology: Methodology;
}

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.8 } },
};

const ProjectCard: FC<Props> = ({ nameKey, methodology }) => {
  const iconSrc =
    methodology === Methodology.SCRUM
      ? "/icons/scrum.svg"
      : "/icons/kanban.png";

  return (
    <Link href={`/projects/${nameKey}/journal`}>
      <motion.div initial="hidden" animate="visible" variants={fadeIn}>
        <Card
          maxSize="fit"
          className="hover:cursor-pointer hover:shadow-xl transition-shadow duration-200"
        >
          <div className="flex flex-col justify-between h-full items-center">
            <h2 className="text-xl font-bold mb-2 text-center">{nameKey}</h2>
            <img src={iconSrc} alt={methodology} className="w-40 h-40" />
          </div>
        </Card>
      </motion.div>
    </Link>
  );
};

export default ProjectCard;
