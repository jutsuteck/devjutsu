import JutsuService from "../jutsu-service";

class StateService extends JutsuService {
  createState = async (workflow_id: string, name: string) => {
    try {
      const response = await this.api.post("/api/v1/states/new", {
        name,
        workflow_id,
      });
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
}

const stateService = new StateService();

export default stateService;
