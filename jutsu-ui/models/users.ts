export interface User {
  id: string;
  first_name?: string;
  last_name?: string;
  email: string;
  is_verified: boolean;
  is_active: boolean;
}

export type UpdateUser = Partial<
  Pick<User, "first_name" | "last_name" | "email">
>;
