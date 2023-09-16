import projectService from "@/services/projects/ProjectService";
import { NextPage } from "next";
import { useEffect, useState } from "react";

const ProjectPage: NextPage = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const fetchProjects = await projectService.getAllProjects();

        setProjects(fetchProjects);

        console.log(fetchProjects);
      } catch (error) {
        console.log(error);
      }
    })();
  }, []);

  return (
    <>
      <h1>{projects}</h1>
    </>
  );
};

export default ProjectPage;
