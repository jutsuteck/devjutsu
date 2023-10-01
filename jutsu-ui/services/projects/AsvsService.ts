import JutsuService from "../jutsu-service";

class AsvsService extends JutsuService {
  getCategories = async () => {
    try {
      const response = await this.api.get("/api/v1/asvs/categories");

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };
}

const asvsService = new AsvsService();

export default asvsService;
