import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  label?: string;
  labelStyle?: string;
}

const FormGroup: FC<Props> = ({ children, label, labelStyle }) => {
  return (
    <div className="mb-4">
      {label && (
        <label className={`${labelStyle} block text-nord-snowstorm-light mb-2`}>
          {label}
        </label>
      )}
      {children}
    </div>
  );
};

export default FormGroup;
