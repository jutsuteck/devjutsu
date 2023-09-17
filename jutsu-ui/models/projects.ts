export enum Methodology {
  SCRUM = "Scrum",
  KANBAN = "Kanban",
}

export enum SecurityLevel {
  LEVEL_1 = "Level 1",
  LEVEL_2 = "Level 2",
  LEVEL_3 = "Level 3",
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
  /* workflows?: Workflow[]; */
}
