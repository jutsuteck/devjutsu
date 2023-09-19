import { NextPage } from "next";
import { useEffect, useState } from "react";

import { Project } from "@/models/projects";
import projectService from "@/services/projects/ProjectService";
import Container from "@/components/layout/Container";
import ProjectCard from "@/components/projects/ProjectCard";
import TopBar from "@/components/ui/TopBar";

const ProjectPage: NextPage = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const fetchProjects = await projectService.getAllProjects();

        setProjects(fetchProjects);
      } catch (error) {
        console.log(error);
      }
    })();
  }, []);

  return (
    <>
      <TopBar />
      <Container>
        <h1 className="text-4xl font-extrabold mb-8">My Projects</h1>
        {projects.map((project: Project) => (
          <ProjectCard
            key={project.id}
            nameKey={project.name_key}
            methodology={project.methodology}
            projectId={project.id}
          />
        ))}
      </Container>
    </>
  );
};

export default ProjectPage;
