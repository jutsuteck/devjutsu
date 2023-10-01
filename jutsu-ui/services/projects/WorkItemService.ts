import { UpdateWorkItem } from "@/models/projects";
import JutsuService from "../jutsu-service";

class WorkItemService extends JutsuService {
  createWorkItem = async (
    workflow_id: string,
    state_id: string,
    name: string
  ) => {
    try {
      const response = await this.api.post("/api/v1/work-items/new", {
        workflow_id: workflow_id,
        state_id: state_id,
        name: name,
      });
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  getWorkItemsByStateId = async (state_id: string) => {
    try {
      const response = await this.api.get(
        `/api/v1/work-items/state/${state_id}`
      );

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
  getWorkItem = async (work_item_id: string) => {
    try {
      const response = await this.api.post(
        `/api/v1/work-items/${work_item_id}`
      );
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
  updateWorkItemState = async (work_item_id: string, state_id: string) => {
    try {
      const response = await this.api.patch(
        `/api/v1/work-items/update-state/${work_item_id}`,
        { state_id }
      );
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
  updateWorkItem = async (work_item_id: string, data: UpdateWorkItem) => {
    try {
      const response = await this.api.patch(
        `/api/v1/work-items/update/${work_item_id}`,
        { ...data }
      );
      console.log("API: ", response.data);
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
  deleteWorkItem = async (work_item_id: string) => {
    try {
      const response = await this.api.delete(
        `/api/v1/work-items/delete/${work_item_id}`
      );
      return response;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
}

const workItemService = new WorkItemService();

export default workItemService;
