import { FC, ReactNode } from "react";

interface Props {
  text?: string;
  fullWidth?: boolean;
  icon?: ReactNode;
  transparent?: boolean;
  className?: string;
  type?: "button" | "submit" | "reset";
  onClick?: () => void;
  polarNightMedium?: boolean;
  bgFrost?: boolean;
  rounded?: "rounded-sm" | "rounded-md" | "rounded-lg" | "rounded-full";
  shadow?: "shadow-md" | "shadow-lg" | "shadow-xl";
}

const Button: FC<Props> = ({
  text,
  fullWidth,
  icon,
  onClick,
  transparent,
  polarNightMedium,
  bgFrost,
  className,
  shadow,
  type = "button",
  rounded = "rounded-lg",
}) => {
  const wFull = fullWidth && "w-full";
  const baseStyle = "p-2 flex items-center justify-center font-bold mb-2";
  const btnTransparent = transparent && "border-2 border-nord-frost-medium";
  const polarNightMd =
    polarNightMedium && "bg-nord-polar-night-medium text-nord-snowstorm-light";
  const frost = bgFrost && "bg-nord-frost-medium text-nord-frost-dark";

  return (
    <button
      type={type}
      className={`${wFull} ${baseStyle} ${polarNightMd} ${frost} ${className} ${btnTransparent} ${rounded} ${
        shadow && shadow
      }`}
      onClick={onClick}
    >
      {icon && <span className="mr-2">{icon}</span>}
      {text}
    </button>
  );
};

export default Button;
