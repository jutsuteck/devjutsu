import { Methodology } from "@/core/models/project";
import JutsuService from "../jutsu-service";

class ProjectService extends JutsuService {
  createProject = async (
    name: string,
    description: string,
    methodology: Methodology
  ) => {
    try {
      const response = await this.api.post("/api/v1/projects/new", {
        name,
        description,
        methodology,
      });

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };

  getAllProjects = async () => {
    try {
      const response = await this.api.get("/api/v1/projects");

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const projectService = new ProjectService();

export default projectService;
