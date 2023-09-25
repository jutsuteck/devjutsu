export interface User {
  id: string;
  name?: string;
  email: string;
  tenant: Tenant;
  is_onboarded: boolean;
  is_verified: boolean;
  is_active: boolean;
}

export interface Tenant {
  id: string;
  name: string;
  members: User[];
}

export type UpdateTenant = Partial<Pick<Tenant, "name" | "members">>;

export type UpdateUser = Partial<Pick<User, "name" | "email" | "is_onboarded">>;
