import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  label?: string;
}

const FormGroup: FC<Props> = ({ children, label }) => {
  return (
    <div className="mb-4">
      {label && (
        <label className="block text-nord-snowstorm-light mb-2">{label}</label>
      )}
      {children}
    </div>
  );
};

export default FormGroup;
