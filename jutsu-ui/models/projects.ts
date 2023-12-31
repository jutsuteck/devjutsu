import { List } from "postcss/lib/list";

export enum Methodology {
  SCRUM = "Scrum",
  KANBAN = "Kanban",
}

export enum SecurityLevel {
  LEVEL_1 = "Level 1",
  LEVEL_2 = "Level 2",
  LEVEL_3 = "Level 3",
}

export enum WorkItemType {
  BUG = "Bug",
  USER_STORY = "User Story",
  WORK_ITEM = "Work Item",
}

export interface Project {
  id: string;
  name: string;
  name_key: string;
  description: string;
  methodology: Methodology;
  security_level: SecurityLevel;
  created_on?: Date;
  /* epics?: Epic[]; */
  workflows?: Workflow[];
}

export interface State {
  id: string;
  name: string;
  workflow_id: string;
  work_items: WorkItem[];
}

export interface WorkItem {
  id: string;
  name: string;
  description?: string;
  effort?: number;
  ready_for_development: boolean;
  created_on: Date;
  work_item_type: WorkItemType;
  workflow: Workflow;
  workflow_id: string;
  state_id: string;
  epic_id: string;
  state: State;
}

export interface Workflow {
  id: string;
  name: string;
  goal: string;
  is_active: boolean;
  start_date: Date;
  end_date: Date;
  project_id: string;
  states: State[];
}

export interface AsvsCategory {
  id: string;
  name: string;
  objective?: string;
  sub_categories: AsvsSubCategory[];
}

export interface AsvsSubCategory {
  id: string;
  name: string;
  objective?: string;
  security_requirements: AsvsRequirement[];
}

export interface AsvsRequirement {
  id: string;
  requirement_id: string;
  description: string;
  levels: string;
  objective?: string;
  value?: string;
}

export type NewState = Pick<State, "name" | "workflow_id">;

export type NewProject = Pick<Project, "name" | "description" | "methodology">;

export type NewWorkItem = Pick<WorkItem, "workflow_id" | "state_id" | "name">;

export type UpdateWorkItem = Partial<
  Pick<
    WorkItem,
    | "name"
    | "description"
    | "effort"
    | "ready_for_development"
    | "work_item_type"
    | "state_id"
    | "epic_id"
  >
>;

export type NewWorkflow = Pick<
  Workflow,
  "project_id" | "name" | "goal" | "start_date" | "end_date"
>;

export type UpdateWorkflow = {
  id: string;
} & Partial<
  Pick<Workflow, "name" | "goal" | "is_active" | "start_date" | "end_date">
>;
