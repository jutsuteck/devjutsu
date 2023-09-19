import { NewWorkflow, UpdateWorkflow } from "@/models/projects";
import JutsuService from "../jutsu-service";

class WorkflowService extends JutsuService {
  createWorkflow = async (data: NewWorkflow) => {
    try {
      const response = await this.api.post("/api/v1/worfklow/new", {
        data,
      });
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  getAllWorkflows = async (project_id: string) => {
    try {
      const response = await this.api.get("/api/v1/workflow/all", {
        project_id,
      });

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  getCurrentWorfklow = async (project_id: string) => {
    try {
      const response = await this.api.get(
        `/api/v1/workflow/current/${project_id}`
      );
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  patchWorkflow = async (data: UpdateWorkflow) => {
    try {
      const response = await this.api.patch("/api/workflow/update", {
        data,
      });

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
}

const workflowService = new WorkflowService();

export default workflowService;
