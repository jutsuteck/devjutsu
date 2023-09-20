import { Methodology, SecurityLevel } from "@/models/projects";
import JutsuService from "../jutsu-service";

class ProjectService extends JutsuService {
  createProject = async (name: string, description?: string) => {
    try {
      const response = await this.api.post("/api/v1/projects/new", {
        name: name,
        description: description,
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

  getProjectDetail = async (project_id: string) => {
    try {
      const response = await this.api.get(`/api/v1/projects/${project_id}`);

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const projectService = new ProjectService();

export default projectService;
