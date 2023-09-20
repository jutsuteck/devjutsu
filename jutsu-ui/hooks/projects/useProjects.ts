import { Project } from "@/models/projects";
import projectService from "@/services/projects/ProjectService";
import { useQuery } from "react-query";

const useProjects = () => {
  return useQuery<Project[], Error>(["projects"], () =>
    projectService.getAllProjects()
  );
};

export default useProjects;
