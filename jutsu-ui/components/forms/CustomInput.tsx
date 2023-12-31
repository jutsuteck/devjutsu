import { FC } from "react";

interface Props {
  register: any;
  name: string;
  placeholder?: string;
  type?: string;
  error?: string;
  autoComplete?: "on" | "off";
  className?: string;
  bgColor?:
    | "bg-nord-polar-night-darkest"
    | "bg-nord-polar-night-dark"
    | "bg-nord-polar-night-medium"
    | "bg-nordr-polar-night-light";
  borderColor?: string;
  noHeight?: boolean;
}

const CustomInput: FC<Props> = ({
  register,
  name,
  placeholder,
  type = "text",
  error,
  autoComplete,
  className,
  borderColor = "border-nord-polar-night-light",
  bgColor = "bg-nord-polar-night-dark",
  noHeight,
}) => {
  const defaultStyle = `${bgColor} ${borderColor} border p-2 rounded-md w-full focus:outline-none`;
  const borderStyle = error
    ? "focus:border-nord-aurora-red"
    : "focus:border-nord-meadow";
  const hasHeight = noHeight ? "" : "h-3 mt-1";

  return (
    <>
      <input
        placeholder={placeholder}
        className={`${defaultStyle} ${borderStyle} ${className}`}
        type={type}
        name={name}
        {...register(name)}
        autoFocus
        autoComplete={autoComplete}
      />
      <div className={`${hasHeight}`}>
        {error && <p className="text-sm text-nord-aurora-red">{error}</p>}
      </div>
    </>
  );
};

export default CustomInput;
