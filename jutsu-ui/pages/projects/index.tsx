import { NextPage } from "next";
import { useState } from "react";
import { IoMdAdd } from "react-icons/io";

import { Project } from "@/models/projects";
import ProjectCard from "@/components/projects/ProjectCard";
import TopBar from "@/components/ui/TopBar";
import Button from "@/components/ui/Button";
import useProjects from "@/hooks/projects/useProjects";
import NewProjectModal from "@/components/projects/NewProjectModal";

const ProjectPage: NextPage = () => {
  const [showModal, setShowModal] = useState<boolean>(false);
  const { data: projects, isLoading, isError } = useProjects();

  return (
    <>
      {showModal && <NewProjectModal onClose={() => setShowModal(false)} />}
      <TopBar />
      <div className="py-4 px-8">
        <Button
          icon={<IoMdAdd />}
          text="New Project"
          onClick={() => setShowModal(true)}
          polarNightMedium
          className="mb-4"
        />
        <div className="flex flex-row space-x-4">
          {projects?.map((project: Project) => (
            <ProjectCard
              key={project.id}
              nameKey={project.name_key}
              methodology={project.methodology}
              projectId={project.id}
            />
          ))}
        </div>
      </div>
    </>
  );
};

export default ProjectPage;
