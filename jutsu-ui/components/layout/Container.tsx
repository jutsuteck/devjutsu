import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  flexCol?: boolean;
  centered?: boolean;
}

const Container: FC<Props> = ({ children, flexCol, centered }) => {
  const centeredContainer = centered
    ? "items-center justify-center"
    : "w-full max-w-screen-lg mx-auto"; // Adjusted width here

  return (
    <div
      className={`min-h-screen flex p-4 ${centeredContainer} ${
        flexCol ? "flex-col" : ""
      }`}
    >
      {children}
    </div>
  );
};

export default Container;
