import * as yup from "yup";

export const projectSchema = yup.object().shape({
  name: yup.string().required("Project name is required."),
  description: yup.string(),
  methodology: yup.string().required("Methodology is required"),
});
