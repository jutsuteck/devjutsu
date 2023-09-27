import { NewState } from "@/models/projects";
import JutsuService from "../jutsu-service";

class StateService extends JutsuService {
  createState = async (data: NewState) => {
    try {
      const response = await this.api.post("/api/v1/states/new", { ...data });
      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };

  getStatesByWorkflowId = async (workflow_id: string) => {
    try {
      const response = await this.api.get(`/api/v1/states/${workflow_id}`);

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  updateState = async (state_id: string, name: string) => {
    try {
      const response = await this.api.patch(
        `/api/v1/states/update/${state_id}`,
        { name }
      );

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  deleteState = async (state_id: string) => {
    console.log(state_id);
    try {
      await this.api.delete(`/api/v1/states/delete/${state_id}`);
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const stateService = new StateService();

export default stateService;
