import { FC, useState } from "react";
import { GrAdd } from "react-icons/gr";
import { motion } from "framer-motion";

import Button from "./Button";

import { AiOutlineTeam } from "react-icons/ai";
import NewClanModal from "./NewClanModal";
import NewProjectModal from "../projects/NewProjectModal";

const CreateButton: FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [showClanModal, setShowClanModal] = useState<boolean>(false);
  const [showProjectModal, setShowProjectModal] = useState<boolean>(false);

  const buttonVariants = {
    open: { y: -10, opacity: 1 },
    closed: { y: 0, opacity: 0 },
  };

  const backgroundVariants = {
    open: { opacity: 0.5, backdropFilter: "blur(5px)" },
    closed: { opacity: 0, backdropFilter: "blur(0px)" },
  };

  return (
    <>
      {showClanModal && (
        <NewClanModal onClose={() => setShowClanModal(false)} />
      )}
      {showProjectModal && (
        <NewProjectModal
          onClose={() => {
            setShowProjectModal(false);
            setIsMenuOpen(false);
          }}
        />
      )}
      {isMenuOpen && (
        <motion.div
          className="fixed inset-0 bg-nord-polar-night-medium z-40"
          initial="closed"
          animate={isMenuOpen ? "open" : "closed"}
          variants={backgroundVariants}
          onClick={() => setIsMenuOpen(false)}
        ></motion.div>
      )}

      <div className="fixed bottom-10 right-10 z-50">
        {isMenuOpen && (
          <motion.div
            className="mt-2 absolute bottom-16 right-0 w-48"
            initial="closed"
            animate={isMenuOpen ? "open" : "closed"}
            variants={buttonVariants}
          >
            <div className="py-1 space-y-4">
              <Button
                text="Create clan"
                fullWidth
                polarNightMedium
                onClick={() => {
                  setShowClanModal(true);
                  setIsMenuOpen(false);
                }}
              />
              <Button
                text="Create project"
                fullWidth
                polarNightMedium
                onClick={() => {
                  setShowProjectModal(true);
                  setIsMenuOpen(false);
                }}
              />
              <Button text="Create work item" fullWidth polarNightMedium />
            </div>
          </motion.div>
        )}

        <button
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="rounded-full p-4 shadow-xl bg-nord-frost-medium"
        >
          <GrAdd />
        </button>
      </div>
    </>
  );
};

export default CreateButton;
