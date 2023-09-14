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
  const defaultStyle =
    "bg-nord-polar-night-medium text-nord-snowstorm-light rounded-md px-4 py-2 w-full focus:outline-none border-nord-polar-night-light border-2";
  const borderStyle = error
    ? "focus:border-nord-aurora-red"
    : "focus:border-nord-meadow";

  return (
    <>
      <input
        placeholder={placeholder}
        className={`${defaultStyle} ${borderStyle}`}
        type={type}
        {...register(name)}
      />
      {error && <p className="text-nord-aurora-red mt-1">{error}</p>}
    </>
  );
};

export default CustomInput;
