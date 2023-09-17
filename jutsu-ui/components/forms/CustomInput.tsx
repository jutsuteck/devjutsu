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
    "bg-nord-polar-night-medium text-nord-snowstorm-light rounded-md px-4 py-2 w-full focus:outline-none border-nord-polar-night-medium border-2";
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
      <div className="h-3 mt-1">
        {error && <p className="text-sm text-nord-aurora-red">{error}</p>}
      </div>
    </>
  );
};

export default CustomInput;
