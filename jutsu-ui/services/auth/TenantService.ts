import JutsuService from "../jutsu-service";

class TenantService extends JutsuService {
  createTenant = async (name: string, member_ids: string[] = []) => {
    try {
      const response = await this.api.post("/api/v1/tenant/new", {
        name,
        member_ids,
      });

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const tenantService = new TenantService();

export default tenantService;
