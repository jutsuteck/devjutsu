import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  maxSize?: "sm" | "md" | "lg" | "xl" | "2xl";
  transparent?: boolean;
  className?: string;
}

const Card: FC<Props> = ({
  children,
  maxSize = "md",
  transparent,
  className,
}) => {
  const baseClasses = "p-8 w-full rounded";
  const sizeClasses = {
    sm: "max-w-sm",
    md: "max-w-md",
    lg: "max-w-lg",
    xl: "max-w-xl",
    "2xl": "max-w-2xl",
  };

  const bgColor = transparent ? "" : "bg-nord-polar-night-light";

  const finalClasses = `${baseClasses} ${sizeClasses[maxSize]} ${bgColor} ${className}`;

  return <div className={finalClasses}>{children}</div>;
};

export default Card;
