import { FC, useEffect } from "react";

interface Props {
  register: any;
  name: string;
  placeholder?: string;
  error?: string;
  autoComplete?: "on" | "off";
  transparent?: boolean;
  className?: string;
  noPaddingX?: boolean;
  bgColor?: string;
  borderColor?: string;
}

const CustomTextArea: FC<Props> = ({
  register,
  name,
  placeholder,
  error,
  autoComplete,
  className,
  bgColor = "bg-nord-polar-night-dark",
  borderColor,
}) => {
  const adjustHeight = (element: HTMLTextAreaElement | null) => {
    if (element) {
      element.style.height = "inherit";
      const scrollHeight = element.scrollHeight;
      element.style.height = scrollHeight + "px";
    }
  };

  const defaultStyle = `${bgColor} ${borderColor} rounded-md p-4 border-2 text-nord-snowstorm-light w-full focus:outline-none`;
  const borderStyle = error
    ? "focus:border-nord-aurora-red"
    : "focus:border-nord-meadow";

  return (
    <>
      <textarea
        placeholder={placeholder}
        className={`${defaultStyle} ${borderStyle} ${className} resize-none overflow-hidden`}
        {...register(name)} // <-- Use the spread syntax here
        onInput={(e) => adjustHeight(e.target)} // <-- Use the onInput event to adjust height
        autoComplete={autoComplete}
        autoFocus
      />
      <div className="h-3 mt-1">
        {error && <p className="text-sm text-nord-aurora-red">{error}</p>}
      </div>
    </>
  );
};

export default CustomTextArea;
