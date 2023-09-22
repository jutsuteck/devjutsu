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
}

const Button: FC<Props> = ({
  text,
  fullWidth,
  icon,
  onClick,
  type = "button",
  polarNightMedium,
  bgFrost,
  className,
}) => {
  const wFull = fullWidth ? "w-full" : "";
  const baseStyle = "rounded-lg p-2 shadow-lg flex items-center font-bold mb-2";
  const polarNightMd =
    polarNightMedium && "bg-nord-polar-night-medium text-nord-snowstorm-light";
  const frost = bgFrost && "bg-nord-frost-medium text-nord-frost-dark";

  return (
    <button
      type={type}
      className={`${wFull} ${baseStyle} ${polarNightMd} ${frost} ${className}`}
      onClick={onClick}
    >
      {icon && <span className="mr-2">{icon}</span>}
      {text}
    </button>
  );
};

export default Button;
