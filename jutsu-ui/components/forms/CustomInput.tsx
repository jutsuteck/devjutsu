import { FC } from "react";

interface Props {
  register: any;
  name: string;
  placeholder?: string;
  type?: string;
  error?: string;
}

const CustomInput: FC<Props> = ({
  register,
  name,
  placeholder,
  type = "text",
  error,
}) => {
  return (
    <>
      <input
        placeholder={placeholder}
        className="input"
        type={type}
        {...register(name)}
      />
      {error && <p className="text-nord-aurora-red mt-1">{error}</p>}
    </>
  );
};

export default CustomInput;
