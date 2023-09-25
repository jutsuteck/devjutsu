import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  icon?: string | ReactNode;
  label?: string;
  labelStyle?: string;
}

const FormGroup: FC<Props> = ({ children, icon, label, labelStyle }) => {
  return (
    <div className="mb-4">
      {label && (
        <label
          className={`${labelStyle} flex items-center block text-nord-snowstorm-light mb-2`}
        >
          {icon && icon}
          <span className={`${icon && "ml-2"}`}>{label}</span>
        </label>
      )}
      {children}
    </div>
  );
};

export default FormGroup;
