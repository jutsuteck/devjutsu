import { Project } from "@/models/projects";
import projectService from "@/services/projects/ProjectService";
import { useQuery } from "react-query";

const useProjectDetail = (projectId: string) => {
  return useQuery<Project, Error>(["projectDetail", projectId], () =>
    projectService.getProjectDetail(projectId)
  );
};

export default useProjectDetail;
